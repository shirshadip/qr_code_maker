import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import qrcode
import datetime
import os

now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")


def txt_gui():
    def generate():
        upi_id = entry.get().strip()
        name = nentry.get().strip()
        amount = aentry.get().strip()
        currency = currency_dropdown.get().strip()
        upi_link = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu={currency}"

        if not upi_id:
            messagebox.showerror("Error", "Please enter the correct upi Id!")
            return

        try:
            img = qrcode.make(upi_link)
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
    win.title("UPI Payment QR Generator")
    win.geometry("1080x820")
    win.configure(bg="#f0f4f8")

    # Custom style
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("Custom.TCombobox",
                    fieldbackground="#ffffff",
                    background="#4a90e2",
                    borderwidth=1)

    # Main container with scrollable capability
    main_frame = tk.Frame(win, bg="#f0f4f8")
    main_frame.pack(expand=True, fill="both", padx=50, pady=30)

    # Header
    header_frame = tk.Frame(main_frame, bg="#4a90e2", height=100)
    header_frame.pack(fill="x", pady=(0, 30))
    header_frame.pack_propagate(False)

    title_label = tk.Label(header_frame,
                           text="💰 UPI Payment QR Generator",
                           font=("Segoe UI", 28, "bold"),
                           bg="#4a90e2",
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
                          highlightcolor="#4a90e2",
                          highlightbackground="#d0d0d0")
    entry_path.pack(side="left", ipady=6, padx=(0, 10))

    def create_browse_button(parent, command):
        btn = tk.Button(parent,
                        text="📂 Browse",
                        command=command,
                        font=("Segoe UI", 10, "bold"),
                        bg="#4a90e2",
                        fg="white",
                        activebackground="#357abd",
                        activeforeground="white",
                        relief="flat",
                        borderwidth=0,
                        padx=18,
                        pady=8,
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

    # UPI Details section
    upi_section = tk.Frame(content_frame, bg="#ffffff", relief="flat", bd=0)
    upi_section.pack(fill="x", pady=(0, 20), padx=20)

    upi_inner = tk.Frame(upi_section, bg="#ffffff")
    upi_inner.pack(padx=25, pady=20)

    # UPI ID
    label1 = tk.Label(upi_inner,
                      text="🆔 UPI ID or Phone Number",
                      font=("Segoe UI", 13, "bold"),
                      bg="#ffffff",
                      fg="#2c3e50")
    label1.pack(anchor="w", pady=(0, 8))

    entry = tk.Entry(upi_inner,
                     width=55,
                     font=("Segoe UI", 11),
                     relief="solid",
                     bd=1,
                     highlightthickness=1,
                     highlightcolor="#4a90e2",
                     highlightbackground="#d0d0d0")
    entry.pack(ipady=6, fill="x", pady=(0, 15))

    # Name
    label2 = tk.Label(upi_inner,
                      text="👤 Account Holder Name",
                      font=("Segoe UI", 13, "bold"),
                      bg="#ffffff",
                      fg="#2c3e50")
    label2.pack(anchor="w", pady=(0, 8))

    nentry = tk.Entry(upi_inner,
                      width=55,
                      font=("Segoe UI", 11),
                      relief="solid",
                      bd=1,
                      highlightthickness=1,
                      highlightcolor="#4a90e2",
                      highlightbackground="#d0d0d0")
    nentry.pack(ipady=6, fill="x", pady=(0, 15))

    # Amount and Currency frame
    amount_frame = tk.Frame(upi_inner, bg="#ffffff")
    amount_frame.pack(fill="x", pady=(0, 10))

    # Amount (left side)
    amount_left = tk.Frame(amount_frame, bg="#ffffff")
    amount_left.pack(side="left", fill="x", expand=True, padx=(0, 10))

    label3 = tk.Label(amount_left,
                      text="💵 Payment Amount",
                      font=("Segoe UI", 13, "bold"),
                      bg="#ffffff",
                      fg="#2c3e50")
    label3.pack(anchor="w", pady=(0, 8))

    aentry = tk.Entry(amount_left,
                      width=20,
                      font=("Segoe UI", 11),
                      relief="solid",
                      bd=1,
                      highlightthickness=1,
                      highlightcolor="#4a90e2",
                      highlightbackground="#d0d0d0")
    aentry.pack(ipady=6, fill="x")

    # Currency (right side)
    currency_right = tk.Frame(amount_frame, bg="#ffffff")
    currency_right.pack(side="left", fill="x", expand=True)

    label4 = tk.Label(currency_right,
                      text="💱 Currency",
                      font=("Segoe UI", 13, "bold"),
                      bg="#ffffff",
                      fg="#2c3e50")
    label4.pack(anchor="w", pady=(0, 8))

    currency_var = tk.StringVar()
    currency_list = ["INR", "USD", "EUR", "GBP", "AUD", "CAD", "JPY"]

    currency_dropdown = ttk.Combobox(currency_right,
                                     textvariable=currency_var,
                                     values=currency_list,
                                     state="readonly",
                                     font=("Segoe UI", 11),
                                     style="Custom.TCombobox")
    currency_dropdown.pack(fill="x", ipady=6)
    currency_dropdown.current(0)

    # Generate button
    def create_generate_button(parent, command):
        btn = tk.Button(parent,
                        text="🔲 Generate Payment QR Code",
                        command=command,
                        font=("Segoe UI", 15, "bold"),
                        bg="#27ae60",
                        fg="white",
                        activebackground="#229954",
                        activeforeground="white",
                        relief="flat",
                        borderwidth=0,
                        padx=35,
                        pady=16,
                        cursor="hand2")

        def on_enter(e):
            btn.config(bg="#229954")

        def on_leave(e):
            btn.config(bg="#27ae60")

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

        return btn

    generate_btn = create_generate_button(content_frame, generate)
    generate_btn.pack(pady=25)

    # Footer
    footer_label = tk.Label(main_frame,
                            text="Scan the QR code to make instant UPI payments",
                            font=("Segoe UI", 10),
                            bg="#f0f4f8",
                            fg="#7f8c8d")
    footer_label.pack(side="bottom", pady=5)

    win.mainloop()


# Run this function
txt_gui()