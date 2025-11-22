def link():

    import qrcode as qr 
    import os
    import datetime
    now = datetime.datetime.now()
    

    data = input ("paste or write down your link: ")
    qr=qr.make(data)
    save=r"D:\repositories\qr_code_maker\qr_codes"
    file_path = os.path.join(save,f"{now}.png")
    qr.save(file_path)
    print("qr code made successfully at :",file_path)
