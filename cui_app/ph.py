def ph ():
    import qrcode as qr
    import os
    import datetime
    now = datetime.datetime.now()
    data = input ("enter your phone number data to make qr code:")
    phone = "tel:" + data
    save=r"D:\repositories\qr_code_maker\qr_codes"
    file_path = os.path.join(save,f"{now}.png")
    qr = qr.make(phone)
    qr.save(file_path)
    print ("qr code made successfully at:",file_path)