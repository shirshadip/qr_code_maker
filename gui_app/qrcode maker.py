"""
D:\repositories\qr_code_maker\gui_app> pyinstaller --onefile --windowed --icon=icon.ico "qrcode maker.py"


command to update exe 


"""

import tkinter as tk
from tkinter import ttk


def import_txt():
    import txt


def import_ph():
    import ph


def import_wa():
    import wa


def import_link():
    import link


def import_upi():
    import upi


root = tk.Tk()
root.title("QR Code Maker App")
root.geometry("1080x720")
root.configure(bg="#f0f4f8")

# Custom style configuration
style = ttk.Style()
style.theme_use('clam')

# Configure combobox style
style.configure("Custom.TCombobox",
                fieldbackground="#ffffff",
                background="#4a90e2",
                foreground="#2c3e50",
                borderwidth=2,
                relief="flat")

# Main container frame with padding
main_frame = tk.Frame(root, bg="#f0f4f8")
main_frame.pack(expand=True, fill="both", padx=40, pady=40)

# Header frame with gradient effect (simulated with frame)
header_frame = tk.Frame(main_frame, bg="#4a90e2", height=120)
header_frame.pack(fill="x", pady=(0, 30))
header_frame.pack_propagate(False)

# Title label with modern styling
title_label = tk.Label(header_frame,
                       text="🔲 QR Code Maker",
                       font=("Segoe UI", 32, "bold"),
                       bg="#4a90e2",
                       fg="white")
title_label.pack(pady=25)

# Subtitle label
subtitle_label = tk.Label(main_frame,
                          text="Select the type of QR code you want to create",
                          font=("Segoe UI", 16),
                          bg="#f0f4f8",
                          fg="#5a6c7d")
subtitle_label.pack(pady=(0, 30))

# Combobox frame for better control
combo_frame = tk.Frame(main_frame, bg="#f0f4f8")
combo_frame.pack(pady=20)

options = ["plain text qr code or plain numbers",
           "mobile number qr code",
           "whatsapp number qr code",
           "web link qr code",
           "upi payment qr code"]

combobox = ttk.Combobox(combo_frame,
                        values=options,
                        font=("Segoe UI", 14),
                        width=45,
                        state="readonly",
                        style="Custom.TCombobox")
combobox.current(0)
combobox.pack(ipady=8)

# Button container frame
button_frame = tk.Frame(main_frame, bg="#f0f4f8")
button_frame.pack(pady=40)

# Store button reference to update it
current_button = None


def create_styled_button(parent, text, command):
    """Create a modern styled button"""
    btn = tk.Button(parent,
                    text=text,
                    command=command,
                    font=("Segoe UI", 14, "bold"),
                    bg="#4a90e2",
                    fg="white",
                    activebackground="#357abd",
                    activeforeground="white",
                    relief="flat",
                    borderwidth=0,
                    padx=30,
                    pady=15,
                    cursor="hand2")

    # Hover effects
    def on_enter(e):
        btn.config(bg="#357abd")

    def on_leave(e):
        btn.config(bg="#4a90e2")

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

    return btn


def on_select(event):
    global current_button

    # Remove previous button if exists
    if current_button:
        current_button.destroy()

    selection = combobox.get()

    if selection == "plain text qr code or plain numbers":
        current_button = create_styled_button(button_frame,
                                              "📝 Create Plain Text QR Code",
                                              import_txt)
        current_button.pack()
    elif selection == "mobile number qr code":
        current_button = create_styled_button(button_frame,
                                              "📱 Create Mobile Number QR Code",
                                              import_ph)
        current_button.pack()
    elif selection == "whatsapp number qr code":
        current_button = create_styled_button(button_frame,
                                              "💬 Create WhatsApp QR Code",
                                              import_wa)
        current_button.pack()
    elif selection == "web link qr code":
        current_button = create_styled_button(button_frame,
                                              "🔗 Create Web Link QR Code",
                                              import_link)
        current_button.pack()
    elif selection == "upi payment qr code":
        current_button = create_styled_button(button_frame,
                                              "💰 Create UPI Payment QR Code",
                                              import_upi)
        current_button.pack()


combobox.bind("<<ComboboxSelected>>", on_select)

# Footer label
footer_label = tk.Label(main_frame,
                        text="Made with ❤️",
                        font=("Segoe UI", 10),
                        bg="#f0f4f8",
                        fg="#95a5a6")
footer_label.pack(side="bottom", pady=10)

root.mainloop()