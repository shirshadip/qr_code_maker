# def txt():

#     import qrcode as qr 
#     data = input ("enter your text or number data to make qr code:")
#     qr = qr.make(data)
#     qr.save(f"{data}.png")
#     print("qr code made successfully")

import tkinter as tk
from tkinter import ttk, messagebox
import qrcode
import datetime
now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
import os 


def txt_gui():
    def generate():
        data = entry.get().strip()

        if not data:
            messagebox.showerror("Error", "Please enter some text or number!")
            return

        try:
            img = qrcode.make(data)
            save=r"D:\qr_code_maker\qr_codes"
            file_path = os.path.join(save,f"{now}.png")
            img.save(file_path)
            messagebox.showinfo("Success", f"QR code saved as {now}.png at : {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create QR code:\n{e}")

    # GUI Window
    win = tk.Tk()
    win.title("Text/Number QR Generator")
    win.geometry("1080x720")
    # win.resizable(False, False)

    label = ttk.Label(win, text="Enter text or number:", font=("Arial", 12))
    label.pack(pady=10)

    entry = ttk.Entry(win, width=35)
    entry.pack(pady=5)

    btn = ttk.Button(win, text="Generate QR Code", command=generate)
    btn.pack(pady=20)

    win.mainloop()


# Run this function
txt_gui()
