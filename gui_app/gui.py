import tkinter as tk

def import_txt():
    import txt

root = tk.Tk()
entry = tk.Entry(root, width=30)
entry.pack(pady=40)

btn = tk.Button(root, text="open activity", command=import_txt)
btn.pack()

root.mainloop()
