def txt():

    import qrcode as qr 
    import os 
    import datetime
    now = datetime.datetime.now()
    data = input ("enter your text or number data to make qr code:")
    qr = qr.make(data)
    save=r"D:\repositories\qr_code_maker\qr_codes"
    file_path = os.path.join(save,f"{now}.png")
    qr.save(file_path)
    print("qr code made successfully")

