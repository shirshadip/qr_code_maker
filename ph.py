def ph ():
    import qrcode as qr
    data = input ("enter your phone number data to make qr code:")
    phone = "tel:" + data
    qr = qr.make(phone)
    qr.save(f"{data}.png")
    print ("qr code made successfully")