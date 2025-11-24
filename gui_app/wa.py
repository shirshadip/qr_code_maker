import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import qrcode
import datetime
import os

now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")


def txt_gui():
    def generate():
        data = entry.get().strip()
        text = entry2.get().strip()
        link = f"https://wa.me/{data}?text={text}"

        if not data:
            messagebox.showerror("Error", "Please enter some text or number!")
            return

        try:
            img = qrcode.make(link)
            save = entry_path.get().strip()
            file_path = os.path.join(save, f"{now}.png")
            img.save(file_path)
            messagebox.showinfo("Success", f"QR code saved as {now}.png at :{file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create QR code:\n{e}")

    def select_folder():
        path = filedialog.askdirectory()
        entry_path.delete(0, tk.END)
        entry_path.insert(0, path)

    # GUI Window
    win = tk.Tk()
    win.title("WhatsApp Number QR Generator")
    win.geometry("1080x820")
    win.configure(bg="#f0f4f8")

    # Custom style
    style = ttk.Style()
    style.theme_use('clam')

    # Main container
    main_frame = tk.Frame(win, bg="#f0f4f8")
    main_frame.pack(expand=True, fill="both", padx=50, pady=30)

    # Header with WhatsApp green theme
    header_frame = tk.Frame(main_frame, bg="#25D366", height=100)
    header_frame.pack(fill="x", pady=(0, 30))
    header_frame.pack_propagate(False)

    title_label = tk.Label(header_frame,
                           text="💬 WhatsApp QR Generator",
                           font=("Segoe UI", 28, "bold"),
                           bg="#25D366",
                           fg="white")
    title_label.pack(pady=25)

    # Content frame
    content_frame = tk.Frame(main_frame, bg="#f0f4f8")
    content_frame.pack(expand=True, pady=10)

    # Folder selection section
    folder_section = tk.Frame(content_frame, bg="#ffffff", relief="flat", bd=0)
    folder_section.pack(fill="x", pady=(0, 20), padx=20)

    folder_inner = tk.Frame(folder_section, bg="#ffffff")
    folder_inner.pack(padx=25, pady=20)

    head_path = tk.Label(folder_inner,
                         text="📁 Select Folder to Save QR Code",
                         font=("Segoe UI", 13, "bold"),
                         bg="#ffffff",
                         fg="#2c3e50")
    head_path.pack(anchor="w", pady=(0, 8))

    path_frame = tk.Frame(folder_inner, bg="#ffffff")
    path_frame.pack(fill="x", pady=5)

    entry_path = tk.Entry(path_frame,
                          width=50,
                          font=("Segoe UI", 11),
                          relief="solid",
                          bd=1,
                          highlightthickness=1,
                          highlightcolor="#25D366",
                          highlightbackground="#d0d0d0")
    entry_path.pack(side="left", ipady=6, padx=(0, 10))

    def create_browse_button(parent, command):
        btn = tk.Button(parent,
                        text="📂 Browse",
                        command=command,
                        font=("Segoe UI", 10, "bold"),
                        bg="#25D366",
                        fg="white",
                        activebackground="#1ea952",
                        activeforeground="white",
                        relief="flat",
                        borderwidth=0,
                        padx=18,
                        pady=8,
                        cursor="hand2")

        def on_enter(e):
            btn.config(bg="#1ea952")

        def on_leave(e):
            btn.config(bg="#25D366")

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

        return btn

    browse_btn = create_browse_button(path_frame, select_folder)
    browse_btn.pack(side="left")

    # WhatsApp Details section
    wa_section = tk.Frame(content_frame, bg="#ffffff", relief="flat", bd=0)
    wa_section.pack(fill="x", pady=(0, 20), padx=20)

    wa_inner = tk.Frame(wa_section, bg="#ffffff")
    wa_inner.pack(padx=25, pady=20)

    # Phone Number
    label1 = tk.Label(wa_inner,
                      text="📱 WhatsApp Number (with country code)",
                      font=("Segoe UI", 13, "bold"),
                      bg="#ffffff",
                      fg="#2c3e50")
    label1.pack(anchor="w", pady=(0, 8))

    entry = tk.Entry(wa_inner,
                     width=55,
                     font=("Segoe UI", 11),
                     relief="solid",
                     bd=1,
                     highlightthickness=1,
                     highlightcolor="#25D366",
                     highlightbackground="#d0d0d0")
    entry.pack(ipady=6, fill="x", pady=(0, 5))

    # Helper text for phone
    helper_phone = tk.Label(wa_inner,
                            text="Example: 919876543210 (country code + number, no + or spaces)",
                            font=("Segoe UI", 9),
                            bg="#ffffff",
                            fg="#7f8c8d")
    helper_phone.pack(anchor="w", pady=(0, 15))

    # Message
    label2 = tk.Label(wa_inner,
                      text="✉️ Pre-filled Message (optional)",
                      font=("Segoe UI", 13, "bold"),
                      bg="#ffffff",
                      fg="#2c3e50")
    label2.pack(anchor="w", pady=(0, 8))

    entry2 = tk.Entry(wa_inner,
                      width=55,
                      font=("Segoe UI", 11),
                      relief="solid",
                      bd=1,
                      highlightthickness=1,
                      highlightcolor="#25D366",
                      highlightbackground="#d0d0d0")
    entry2.pack(ipady=6, fill="x", pady=(0, 5))

    # Helper text for message
    helper_msg = tk.Label(wa_inner,
                          text="This message will appear when someone scans the QR code",
                          font=("Segoe UI", 9),
                          bg="#ffffff",
                          fg="#7f8c8d")
    helper_msg.pack(anchor="w", pady=(0, 10))

    # Generate button
    def create_generate_button(parent, command):
        btn = tk.Button(parent,
                        text="🔲 Generate WhatsApp QR Code",
                        command=command,
                        font=("Segoe UI", 15, "bold"),
                        bg="#25D366",
                        fg="white",
                        activebackground="#1ea952",
                        activeforeground="white",
                        relief="flat",
                        borderwidth=0,
                        padx=35,
                        pady=16,
                        cursor="hand2")

        def on_enter(e):
            btn.config(bg="#1ea952")

        def on_leave(e):
            btn.config(bg="#25D366")

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

        return btn

    generate_btn = create_generate_button(content_frame, generate)
    generate_btn.pack(pady=25)

    # Footer
    footer_label = tk.Label(main_frame,
                            text="Scan the QR code to start a WhatsApp conversation instantly",
                            font=("Segoe UI", 10),
                            bg="#f0f4f8",
                            fg="#7f8c8d")
    footer_label.pack(side="bottom", pady=5)

    win.mainloop()


# Run this function
txt_gui()