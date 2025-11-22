"""
D:\repositories\qr_code_maker\gui_app> pyinstaller --onefile --windowed --icon=icon.ico "qrcode maker.py"


command to update exe 


"""

import os

os.makedirs(r"D:\repositories\qr_code_maker\qr_codes", exist_ok=True)


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
root.title ("QR code maker app")
root.geometry("1080x720")
# options
label = tk.Label(root,text="Select which type of qr code you want to make",font=("Arial",17))
label.pack(pady=50,padx=50)
options = ["plain text qr code or plain numbers","mobile number qr code","whatsapp number qr code", "web link qr code","upi payment qr code"]


combobox = ttk.Combobox(root, values=options,font=("Arial",23),width=55,state="readonly")
combobox.current(0)  # set default option
combobox.pack(pady=50,padx=120)

def on_select(event):
    if combobox.get() == "plain text qr code or plain numbers":
        btn = tk.Button(root, text="open the window to create plain text qr code", command=import_txt,font=("Arial",18))
        btn.pack()
    elif combobox.get() == "mobile number qr code":
        btn2= tk.Button(root, text="open the window to create mobile number qr code", command=import_ph,font=("Arial",18))
        btn2.pack()
    elif combobox.get() == "whatsapp number qr code":
        btn3 = tk.Button(root, text="open the window to create whatsapp number qr code", command=import_wa,font=("Arial",18))
        btn3.pack()
    elif combobox.get() == "web link qr code":
        btn3 = tk.Button(root, text="open the window to create web link qr code", command=import_link,font=("Arial",18))
        btn3.pack()
    elif combobox.get() == "upi payment qr code":
        btn4 = tk.Button(root, text="open the window to create upi payment qr code", command=import_upi,font=("Arial",18))
        btn4.pack()

combobox.bind("<<ComboboxSelected>>", on_select)



root.mainloop()
