import tkinter as tk
from tkinter import ttk, messagebox
import qrcode


def txt_gui():
    def generate():
        data = entry.get().strip()
        text=entry2.get().strip()
        link= f"https://wa.me/{data}?text={text}"
        if not data:
            messagebox.showerror("Error", "Please enter some text or number!")
            return

        try:
            img = qrcode.make(link)
            img.save(f"{data}.png")
            messagebox.showinfo("Success", f"QR code saved as {data}.png")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create QR code:\n{e}")

    # GUI Window
    win = tk.Tk()
    win.title("Whatsapp Number QR Generator")
    win.geometry("1080x720")
    # win.resizable(False, False)

    label = ttk.Label(win, text="Enter the whatsapp number with country code:", font=("Arial", 12))
    label.pack(pady=20,padx=20)

    entry = ttk.Entry(win, width=35)
    entry.pack(pady=5)
    label = ttk.Label(win, text="Enter a whatsapp message for the whatsapp number:", font=("Arial", 12))
    label.pack(pady=20, padx=20)
    entry2 = ttk.Entry(win, width=50)
    entry2.pack(pady=5)

    btn = ttk.Button(win, text="Generate QR Code", command=generate)
    btn.pack(pady=20)

    win.mainloop()


# Run this function
txt_gui()
