def what():
    import qrcode as qr 
    import os 
    import datetime
    now = datetime.datetime.now()
    data = input ("enter your direct opening whatsapp chat number(need to write with country code(eg.91 for india )):")
    text= input ("you can enter your msg automatically(for space you have to enter %20):")
    link= f"https://wa.me/{data}?text={text}"
    qr = qr.make(link)
    save=r"D:\repositories\qr_code_maker\qr_codes"
    file_path = os.path.join(save,f"{now}.png")
    qr.save(file_path)
    print ("qr code made successfully")