import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import qrcode
import datetime
import os

now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")


def txt_gui():
    def generate():
        data = entry.get().strip()

        if not data:
            messagebox.showerror("Error", "Please enter some text or number!")
            return

        try:
            img = qrcode.make(data)
            save = entry_path.get().strip()
            file_path = os.path.join(save, f"{now}.png")
            img.save(file_path)
            messagebox.showinfo("Success", f"QR code saved as {now}.png at : {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create QR code:\n{e}")

    def select_folder():
        path = filedialog.askdirectory()
        entry_path.delete(0, tk.END)
        entry_path.insert(0, path)

    # GUI Window
    win = tk.Tk()
    win.title("Text/Number QR Generator")
    win.geometry("1080x720")
    win.configure(bg="#f0f4f8")

    # Custom style
    style = ttk.Style()
    style.theme_use('clam')

    # Main container
    main_frame = tk.Frame(win, bg="#f0f4f8")
    main_frame.pack(expand=True, fill="both", padx=50, pady=40)

    # Header
    header_frame = tk.Frame(main_frame, bg="#4a90e2", height=100)
    header_frame.pack(fill="x", pady=(0, 40))
    header_frame.pack_propagate(False)

    title_label = tk.Label(header_frame,
                           text="📝 Text/Number QR Generator",
                           font=("Segoe UI", 28, "bold"),
                           bg="#4a90e2",
                           fg="white")
    title_label.pack(pady=25)

    # Content frame
    content_frame = tk.Frame(main_frame, bg="#f0f4f8")
    content_frame.pack(expand=True, pady=20)

    # Folder selection section
    folder_section = tk.Frame(content_frame, bg="#ffffff", relief="flat", bd=0)
    folder_section.pack(fill="x", pady=(0, 30), padx=20)

    folder_inner = tk.Frame(folder_section, bg="#ffffff")
    folder_inner.pack(padx=25, pady=25)

    head_path = tk.Label(folder_inner,
                         text="📁 Select Folder to Save QR Code",
                         font=("Segoe UI", 14, "bold"),
                         bg="#ffffff",
                         fg="#2c3e50")
    head_path.pack(anchor="w", pady=(0, 10))

    path_frame = tk.Frame(folder_inner, bg="#ffffff")
    path_frame.pack(fill="x", pady=5)

    entry_path = tk.Entry(path_frame,
                          width=50,
                          font=("Segoe UI", 12),
                          relief="solid",
                          bd=1,
                          highlightthickness=1,
                          highlightcolor="#4a90e2",
                          highlightbackground="#d0d0d0")
    entry_path.pack(side="left", ipady=8, padx=(0, 10))

    def create_browse_button(parent, command):
        btn = tk.Button(parent,
                        text="📂 Browse",
                        command=command,
                        font=("Segoe UI", 11, "bold"),
                        bg="#4a90e2",
                        fg="white",
                        activebackground="#357abd",
                        activeforeground="white",
                        relief="flat",
                        borderwidth=0,
                        padx=20,
                        pady=10,
                        cursor="hand2")

        def on_enter(e):
            btn.config(bg="#357abd")

        def on_leave(e):
            btn.config(bg="#4a90e2")

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

        return btn

    browse_btn = create_browse_button(path_frame, select_folder)
    browse_btn.pack(side="left")

    # Text/Number input section
    text_section = tk.Frame(content_frame, bg="#ffffff", relief="flat", bd=0)
    text_section.pack(fill="x", pady=(0, 30), padx=20)

    text_inner = tk.Frame(text_section, bg="#ffffff")
    text_inner.pack(padx=25, pady=25)

    label = tk.Label(text_inner,
                     text="✏️ Enter Text or Number",
                     font=("Segoe UI", 14, "bold"),
                     bg="#ffffff",
                     fg="#2c3e50")
    label.pack(anchor="w", pady=(0, 10))

    entry = tk.Entry(text_inner,
                     width=50,
                     font=("Segoe UI", 12),
                     relief="solid",
                     bd=1,
                     highlightthickness=1,
                     highlightcolor="#4a90e2",
                     highlightbackground="#d0d0d0")
    entry.pack(ipady=8, fill="x")

    # Helper text
    helper_text = tk.Label(text_inner,
                           text="Enter any text, number, or data you want to encode",
                           font=("Segoe UI", 9),
                           bg="#ffffff",
                           fg="#7f8c8d")
    helper_text.pack(anchor="w", pady=(5, 0))

    # Generate button
    def create_generate_button(parent, command):
        btn = tk.Button(parent,
                        text="🔲 Generate QR Code",
                        command=command,
                        font=("Segoe UI", 16, "bold"),
                        bg="#27ae60",
                        fg="white",
                        activebackground="#229954",
                        activeforeground="white",
                        relief="flat",
                        borderwidth=0,
                        padx=40,
                        pady=18,
                        cursor="hand2")

        def on_enter(e):
            btn.config(bg="#229954")

        def on_leave(e):
            btn.config(bg="#27ae60")

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

        return btn

    generate_btn = create_generate_button(content_frame, generate)
    generate_btn.pack(pady=30)

    # Footer
    footer_label = tk.Label(main_frame,
                            text="Perfect for creating QR codes with plain text, numbers, or any custom data",
                            font=("Segoe UI", 10),
                            bg="#f0f4f8",
                            fg="#7f8c8d")
    footer_label.pack(side="bottom", pady=10)

    win.mainloop()


# Run this function
txt_gui()