import tkinter as tk
from tkinter import ttk, messagebox
import qrcode
import datetime
now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
import os 



def txt_gui():
    def generate():
        upi_id = entry.get().strip()
        name=nentry.get().strip()
        amount=aentry.get().strip()
        currency=currency_dropdown.get().strip()
        upi_link = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu={currency}"
        if not upi_id:
            messagebox.showerror("Error", "Please enter the correct upi Id!")
            return

        try:
            img = qrcode.make(upi_link)
            save=r"D:\repositories\qr_code_maker\qr_codes"
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

    label = ttk.Label(win, text="Enter the upi Id or phone number:", font=("Arial", 17))
    label.pack(pady=10)

    entry = ttk.Entry(win, width=50)
    entry.pack(pady=5)

    label = ttk.Label(win, text="Enter the upi Id owner name:", font=("Arial", 17))
    label.pack(pady=10)

    nentry = ttk.Entry(win, width=50)
    nentry.pack(pady=5)
    label = ttk.Label(win, text="Enter the amount you want to pay:", font=("Arial", 17))
    label.pack(pady=10)

    aentry = ttk.Entry(win, width=15)
    aentry.pack(pady=5)
    # Currency Dropdown
    tk.Label(win, text="Select Currency Code:", font=("Arial", 12)).pack(pady=5)

    currency_var = tk.StringVar()
    currency_list = ["INR", "USD", "EUR", "GBP", "AUD", "CAD", "JPY"]

    currency_dropdown = ttk.Combobox(win, textvariable=currency_var, values=currency_list, state="readonly",
                                     font=("Arial", 12))
    currency_dropdown.pack()
    currency_dropdown.current(0)
    btn = ttk.Button(win, text="Generate QR Code", command=generate)
    btn.pack(pady=20)

    win.mainloop()


# Run this function
txt_gui()
