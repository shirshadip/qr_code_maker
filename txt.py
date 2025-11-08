def txt():

    import qrcode as qr 
    data = input ("enter your text or number data to make qr code:")
    qr = qr.make(data)
    qr.save(f"{data}.png")
    print("qr code made successfully")

