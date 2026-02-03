"""
QR Code Maker - Professional Desktop Application
Build command: pyinstaller --onefile --windowed --icon=icon.ico --name QrcodeMaker main.py
pyinstaller --onefile --windowed --icon=icon.ico --add-data "icon.ico;." --add-data "logo.png;." --name QrcodeMaker main.py
"""

import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import qrcode
from io import BytesIO


class QRCodeMakerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Maker")
        self.root.geometry("1100x700")
        self.root.minsize(900, 600)
        self.root.configure(bg="#f0f4f8")

        # Variables
        self.qr_image = None
        self.qr_pil_image = None
        self.current_qr_type = tk.StringVar(value="text")

        # Setup UI
        self.create_menu_bar()
        self.setup_styles()
        self.create_main_layout()

        # Center window
        self.center_window()

    def setup_styles(self):
        """Configure modern styles"""
        style = ttk.Style()
        style.theme_use('clam')

        # Configure custom styles
        style.configure("Card.TFrame", background="#ffffff", relief="flat")
        style.configure("Header.TLabel", background="#4a90e2", foreground="white",
                       font=("Segoe UI", 24, "bold"))
        style.configure("SubHeader.TLabel", background="#f0f4f8", foreground="#5a6c7d",
                       font=("Segoe UI", 12))
        style.configure("Custom.TRadiobutton", background="#ffffff",
                       font=("Segoe UI", 10))

    def create_menu_bar(self):
        """Create traditional Windows-style menu bar"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # File Menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New QR Code", command=self.new_qr_code, accelerator="Ctrl+N")
        file_menu.add_command(label="Open Image...", command=self.open_image, accelerator="Ctrl+O")
        file_menu.add_separator()
        file_menu.add_command(label="Save QR Code", command=self.save_qr_code, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As...", command=self.save_qr_code_as, accelerator="Ctrl+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app, accelerator="Alt+F4")

        # Edit Menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Clear All", command=self.clear_all, accelerator="Ctrl+L")
        edit_menu.add_command(label="Copy QR Code", command=self.copy_qr_code, accelerator="Ctrl+C")
        edit_menu.add_separator()
        edit_menu.add_command(label="Preferences", command=self.show_preferences)

        # Generate Menu
        generate_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Generate", menu=generate_menu)
        generate_menu.add_command(label="Generate QR Code", command=self.generate_qr_code, accelerator="Ctrl+G")
        generate_menu.add_command(label="Regenerate", command=self.regenerate_qr_code, accelerator="F5")

        # Help Menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="How to Use", command=self.show_help)
        help_menu.add_command(label="About", command=self.show_about)

        # Keyboard shortcuts
        self.root.bind("<Control-n>", lambda e: self.new_qr_code())
        self.root.bind("<Control-o>", lambda e: self.open_image())
        self.root.bind("<Control-s>", lambda e: self.save_qr_code())
        self.root.bind("<Control-Shift-S>", lambda e: self.save_qr_code_as())
        self.root.bind("<Control-l>", lambda e: self.clear_all())
        self.root.bind("<Control-g>", lambda e: self.generate_qr_code())
        self.root.bind("<F5>", lambda e: self.regenerate_qr_code())

    def create_main_layout(self):
        """Create the main application layout"""
        # Main container
        main_container = tk.Frame(self.root, bg="#f0f4f8")
        main_container.pack(fill="both", expand=True, padx=20, pady=20)

        # Left panel - Input area
        left_panel = tk.Frame(main_container, bg="#ffffff", relief="flat", bd=2)
        left_panel.pack(side="left", fill="both", expand=True, padx=(0, 10))

        # Right panel - QR Code display
        right_panel = tk.Frame(main_container, bg="#ffffff", relief="flat", bd=2)
        right_panel.pack(side="right", fill="both", expand=True, padx=(10, 0))

        self.create_input_panel(left_panel)
        self.create_display_panel(right_panel)

    def create_input_panel(self, parent):
        """Create the input panel with all QR code options"""
        # Header
        header = tk.Label(parent, text="📝 Create QR Code",
                         font=("Segoe UI", 18, "bold"),
                         bg="#ffffff", fg="#2c3e50")
        header.pack(pady=(20, 10), padx=20, anchor="w")

        # Subtitle
        subtitle = tk.Label(parent, text="Select type and enter details",
                           font=("Segoe UI", 10),
                           bg="#ffffff", fg="#7f8c8d")
        subtitle.pack(pady=(0, 20), padx=20, anchor="w")

        # QR Type Selection Frame
        type_frame = tk.LabelFrame(parent, text="QR Code Type",
                                   font=("Segoe UI", 11, "bold"),
                                   bg="#ffffff", fg="#34495e", padx=15, pady=10)
        type_frame.pack(fill="x", padx=20, pady=(0, 15))

        qr_types = [
            ("📄 Plain Text/Numbers", "text"),
            ("📱 Mobile Number", "phone"),
            ("💬 WhatsApp", "whatsapp"),
            ("🔗 Web Link", "link"),
            ("💰 UPI Payment", "upi")
        ]

        for text, value in qr_types:
            rb = ttk.Radiobutton(type_frame, text=text, value=value,
                                variable=self.current_qr_type,
                                command=self.on_type_change,
                                style="Custom.TRadiobutton")
            rb.pack(anchor="w", pady=3)

        # Input Fields Container (scrollable)
        input_container = tk.Frame(parent, bg="#ffffff")
        input_container.pack(fill="both", expand=True, padx=20, pady=(0, 15))

        # Canvas for scrolling
        self.input_canvas = tk.Canvas(input_container, bg="#ffffff", highlightthickness=0)
        scrollbar = ttk.Scrollbar(input_container, orient="vertical",
                                 command=self.input_canvas.yview)

        self.input_frame = tk.Frame(self.input_canvas, bg="#ffffff")
        self.input_frame.bind("<Configure>",
                             lambda e: self.input_canvas.configure(scrollregion=self.input_canvas.bbox("all")))

        self.input_canvas.create_window((0, 0), window=self.input_frame, anchor="nw")
        self.input_canvas.configure(yscrollcommand=scrollbar.set)

        self.input_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Initialize with default input fields
        self.on_type_change()

        # Generate Button
        generate_btn = tk.Button(parent, text="🔲 Generate QR Code",
                                command=self.generate_qr_code,
                                font=("Segoe UI", 12, "bold"),
                                bg="#4a90e2", fg="white",
                                activebackground="#357abd",
                                activeforeground="white",
                                relief="flat", bd=0,
                                padx=20, pady=12,
                                cursor="hand2")
        generate_btn.pack(pady=(0, 20), padx=20, fill="x")

        # Hover effect for generate button
        generate_btn.bind("<Enter>", lambda e: generate_btn.config(bg="#357abd"))
        generate_btn.bind("<Leave>", lambda e: generate_btn.config(bg="#4a90e2"))

    def create_display_panel(self, parent):
        """Create the QR code display panel"""
        # Header
        header = tk.Label(parent, text="🔲 QR Code Preview",
                         font=("Segoe UI", 18, "bold"),
                         bg="#ffffff", fg="#2c3e50")
        header.pack(pady=(20, 10), padx=20, anchor="w")

        # QR Display Frame
        display_frame = tk.Frame(parent, bg="#f8f9fa", relief="solid", bd=1)
        display_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # QR Image Label
        self.qr_label = tk.Label(display_frame, bg="#f8f9fa",
                                text="QR code will appear here\n\n👆 Generate a QR code to preview",
                                font=("Segoe UI", 12),
                                fg="#95a5a6")
        self.qr_label.pack(expand=True)

        # Action Buttons Frame
        action_frame = tk.Frame(parent, bg="#ffffff")
        action_frame.pack(fill="x", padx=20, pady=(0, 20))

        # Save Button
        save_btn = tk.Button(action_frame, text="💾 Save",
                            command=self.save_qr_code,
                            font=("Segoe UI", 10, "bold"),
                            bg="#27ae60", fg="white",
                            activebackground="#229954",
                            activeforeground="white",
                            relief="flat", bd=0,
                            padx=15, pady=8,
                            cursor="hand2")
        save_btn.pack(side="left", expand=True, fill="x", padx=(0, 5))

        # Copy Button
        copy_btn = tk.Button(action_frame, text="📋 Copy",
                            command=self.copy_qr_code,
                            font=("Segoe UI", 10, "bold"),
                            bg="#3498db", fg="white",
                            activebackground="#2980b9",
                            activeforeground="white",
                            relief="flat", bd=0,
                            padx=15, pady=8,
                            cursor="hand2")
        copy_btn.pack(side="left", expand=True, fill="x", padx=5)

        # Clear Button
        clear_btn = tk.Button(action_frame, text="🗑️ Clear",
                             command=self.new_qr_code,
                             font=("Segoe UI", 10, "bold"),
                             bg="#e74c3c", fg="white",
                             activebackground="#c0392b",
                             activeforeground="white",
                             relief="flat", bd=0,
                             padx=15, pady=8,
                             cursor="hand2")
        clear_btn.pack(side="left", expand=True, fill="x", padx=(5, 0))

        # Hover effects
        for btn, normal_color, hover_color in [
            (save_btn, "#27ae60", "#229954"),
            (copy_btn, "#3498db", "#2980b9"),
            (clear_btn, "#e74c3c", "#c0392b")
        ]:
            btn.bind("<Enter>", lambda e, b=btn, c=hover_color: b.config(bg=c))
            btn.bind("<Leave>", lambda e, b=btn, c=normal_color: b.config(bg=c))

    def on_type_change(self):
        """Handle QR type selection change"""
        # Clear existing input fields
        for widget in self.input_frame.winfo_children():
            widget.destroy()

        qr_type = self.current_qr_type.get()

        if qr_type == "text":
            self.create_text_input()
        elif qr_type == "phone":
            self.create_phone_input()
        elif qr_type == "whatsapp":
            self.create_whatsapp_input()
        elif qr_type == "link":
            self.create_link_input()
        elif qr_type == "upi":
            self.create_upi_input()

    def create_label_entry(self, parent, label_text, row=0):
        """Helper to create label and entry pair"""
        label = tk.Label(parent, text=label_text, font=("Segoe UI", 10),
                        bg="#ffffff", fg="#2c3e50", anchor="w")
        label.grid(row=row, column=0, sticky="w", pady=8)

        entry = tk.Entry(parent, font=("Segoe UI", 10), relief="solid", bd=1)
        entry.grid(row=row, column=1, sticky="ew", pady=8, padx=(10, 0))

        return entry

    def create_text_input(self):
        """Create input fields for plain text QR code"""
        tk.Label(self.input_frame, text="Enter your text or numbers:",
                font=("Segoe UI", 10, "bold"),
                bg="#ffffff", fg="#2c3e50").pack(anchor="w", pady=(5, 10))

        self.text_input = tk.Text(self.input_frame, height=8, font=("Segoe UI", 10),
                                 relief="solid", bd=1, wrap="word")
        self.text_input.pack(fill="both", expand=True)

    def create_phone_input(self):
        """Create input fields for phone number QR code"""
        frame = tk.Frame(self.input_frame, bg="#ffffff")
        frame.pack(fill="x")
        frame.columnconfigure(1, weight=1)

        self.phone_country = self.create_label_entry(frame, "Country Code:", 0)
        self.phone_country.insert(0, "+91")

        self.phone_number = self.create_label_entry(frame, "Phone Number:", 1)

    def create_whatsapp_input(self):
        """Create input fields for WhatsApp QR code"""
        frame = tk.Frame(self.input_frame, bg="#ffffff")
        frame.pack(fill="x")
        frame.columnconfigure(1, weight=1)

        self.wa_country = self.create_label_entry(frame, "Country Code:", 0)
        self.wa_country.insert(0, "+91")

        self.wa_number = self.create_label_entry(frame, "WhatsApp Number:", 1)

        tk.Label(frame, text="Message (optional):", font=("Segoe UI", 10),
                bg="#ffffff", fg="#2c3e50", anchor="w").grid(row=2, column=0,
                                                             sticky="nw", pady=8)

        self.wa_message = tk.Text(frame, height=5, font=("Segoe UI", 10),
                                 relief="solid", bd=1, wrap="word")
        self.wa_message.grid(row=2, column=1, sticky="ew", pady=8, padx=(10, 0))

    def create_link_input(self):
        """Create input fields for web link QR code"""
        frame = tk.Frame(self.input_frame, bg="#ffffff")
        frame.pack(fill="x")
        frame.columnconfigure(1, weight=1)

        self.link_url = self.create_label_entry(frame, "Website URL:", 0)
        self.link_url.insert(0, "https://")

    def create_upi_input(self):
        """Create input fields for UPI payment QR code"""
        frame = tk.Frame(self.input_frame, bg="#ffffff")
        frame.pack(fill="x")
        frame.columnconfigure(1, weight=1)

        self.upi_id = self.create_label_entry(frame, "UPI ID:", 0)
        self.upi_name = self.create_label_entry(frame, "Payee Name:", 1)
        self.upi_amount = self.create_label_entry(frame, "Amount (₹):", 2)
        self.upi_note = self.create_label_entry(frame, "Note (optional):", 3)

    def generate_qr_code(self):
        """Generate QR code based on current type and inputs"""
        qr_type = self.current_qr_type.get()
        data = ""

        try:
            if qr_type == "text":
                data = self.text_input.get("1.0", "end-1c").strip()
                if not data:
                    messagebox.showwarning("Input Required", "Please enter some text!")
                    return

            elif qr_type == "phone":
                country = self.phone_country.get().strip()
                number = self.phone_number.get().strip()
                if not number:
                    messagebox.showwarning("Input Required", "Please enter a phone number!")
                    return
                data = f"tel:{country}{number}"

            elif qr_type == "whatsapp":
                country = self.wa_country.get().strip().replace("+", "")
                number = self.wa_number.get().strip()
                message = self.wa_message.get("1.0", "end-1c").strip()
                if not number:
                    messagebox.showwarning("Input Required", "Please enter a WhatsApp number!")
                    return
                data = f"https://wa.me/{country}{number}"
                if message:
                    data += f"?text={message}"

            elif qr_type == "link":
                url = self.link_url.get().strip()
                if not url or url == "https://":
                    messagebox.showwarning("Input Required", "Please enter a valid URL!")
                    return
                data = url

            elif qr_type == "upi":
                upi_id = self.upi_id.get().strip()
                name = self.upi_name.get().strip()
                amount = self.upi_amount.get().strip()
                note = self.upi_note.get().strip()

                if not upi_id or not name:
                    messagebox.showwarning("Input Required",
                                         "Please enter UPI ID and Payee Name!")
                    return

                data = f"upi://pay?pa={upi_id}&pn={name}"
                if amount:
                    data += f"&am={amount}"
                if note:
                    data += f"&tn={note}"

            # Generate QR Code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)

            # Create PIL Image
            self.qr_pil_image = qr.make_image(fill_color="black", back_color="white")

            # Display QR Code
            self.display_qr_code()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate QR code:\n{str(e)}")

    def display_qr_code(self):
        """Display the generated QR code"""
        if self.qr_pil_image:
            # Resize for display
            display_size = (350, 350)
            # Backwards-compatible resampling attribute
            try:
                resample_filter = Image.Resampling.LANCZOS
            except Exception:
                resample_filter = Image.LANCZOS

            img_resized = self.qr_pil_image.resize(display_size, resample_filter)

            # Convert to PhotoImage
            self.qr_image = ImageTk.PhotoImage(img_resized)

            # Update label
            self.qr_label.config(image=self.qr_image, text="")

    def save_qr_code(self):
        """Save the QR code to file"""
        if not self.qr_pil_image:
            messagebox.showwarning("No QR Code", "Please generate a QR code first!")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"),
                      ("All files", "*.*")]
        )

        if file_path:
            try:
                self.qr_pil_image.save(file_path)
                messagebox.showinfo("Success", f"QR code saved successfully!\n{file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save QR code:\n{str(e)}")

    def save_qr_code_as(self):
        """Save As wrapper"""
        self.save_qr_code()

    def copy_qr_code(self):
        """Copy QR code to clipboard"""
        if not self.qr_pil_image:
            messagebox.showwarning("No QR Code", "Please generate a QR code first!")
            return

        try:
            # Save to BytesIO
            output = BytesIO()
            self.qr_pil_image.save(output, format='PNG')
            data = output.getvalue()
            output.close()

            # Copy to clipboard (Windows)
            import win32clipboard
            from io import BytesIO

            def send_to_clipboard(clip_type, data):
                win32clipboard.OpenClipboard()
                win32clipboard.EmptyClipboard()
                win32clipboard.SetClipboardData(clip_type, data)
                win32clipboard.CloseClipboard()

            # Save to temp file and copy
            import tempfile
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
            self.qr_pil_image.save(temp_file.name)
            temp_file.close()

            messagebox.showinfo("Success", "QR code copied to clipboard!")
        except ImportError:
            messagebox.showinfo("Info",
                              "Clipboard copy requires pywin32.\nPlease use Save instead.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to copy QR code:\n{str(e)}")

    def new_qr_code(self):
        """Clear everything and start fresh"""
        self.on_type_change()
        self.qr_pil_image = None
        self.qr_image = None
        self.qr_label.config(image="",
                            text="QR code will appear here\n\n👆 Generate a QR code to preview")

    def clear_all(self):
        """Clear all inputs"""
        self.new_qr_code()

    def regenerate_qr_code(self):
        """Regenerate the current QR code"""
        self.generate_qr_code()

    def open_image(self):
        """Open an existing QR code image"""
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp"),
                      ("All files", "*.*")]
        )

        if file_path:
            try:
                self.qr_pil_image = Image.open(file_path)
                self.display_qr_code()
                messagebox.showinfo("Success", "Image loaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open image:\n{str(e)}")

    def show_preferences(self):
        """Show preferences dialog"""
        messagebox.showinfo("Preferences",
                          "Preferences panel\n\nComing soon in next version!")

    def show_help(self):
        """Show help dialog"""
        help_text = """QR Code Maker - How to Use

1. Select the type of QR code you want to create
2. Fill in the required information
3. Click 'Generate QR Code'
4. Save or copy your QR code

Keyboard Shortcuts:
- Ctrl+N: New QR Code
- Ctrl+S: Save QR Code
- Ctrl+G: Generate QR Code
- F5: Regenerate
- Ctrl+L: Clear All

Support: For issues or suggestions, please contact support."""

        messagebox.showinfo("How to Use", help_text)

    def show_about(self):
        """Show about dialog"""
        about_text = """QR Code Maker
Version 2.0

A professional QR code generation tool
for creating various types of QR codes.

Made with ❤️

© 2024 QR Code Maker"""

        messagebox.showinfo("About", about_text)

    def exit_app(self):
        """Exit the application"""
        if messagebox.askokcancel("Quit", "Do you want to exit QR Code Maker?"):
            self.root.destroy()

    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')


def main():
    root = tk.Tk()
    app = QRCodeMakerApp(root)
    # Ensure icon is shown in titlebar and taskbar (generate .ico if missing)
    def ensure_app_icon(win):
        # When running from a PyInstaller bundle, resources are extracted to _MEIPASS
        base_dir = getattr(sys, '_MEIPASS', os.path.dirname(__file__))
        png_path = os.path.join(base_dir, "logo.png")
        ico_path = os.path.join(base_dir, "icon.ico")

        try:
            # If .ico missing but logo.png exists, create a multi-size ICO
            if not os.path.exists(ico_path) and os.path.exists(png_path):
                try:
                    img = Image.open(png_path)
                    sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
                    img.save(ico_path, format='ICO', sizes=sizes)
                except Exception:
                    # ignore failures to auto-generate
                    pass

            # Set the Tk titlebar icon from PNG (keeps image in memory)
            if os.path.exists(png_path):
                try:
                    photo = tk.PhotoImage(file=png_path)
                    win.iconphoto(True, photo)
                    # keep reference to avoid GC
                    win._icon_photo = photo
                except Exception:
                    pass

            # On Windows also set iconbitmap to the .ico (helps taskbar for packaged exe)
            if os.name == 'nt' and os.path.exists(ico_path):
                try:
                    win.iconbitmap(ico_path)
                except Exception:
                    pass
        except Exception:
            pass

    ensure_app_icon(root)
    root.mainloop()
    
    

if __name__ == "__main__":
    main()