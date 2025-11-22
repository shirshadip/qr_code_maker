def link():

    import qrcode as qr 
    data = input ("paste or write down your link: ")
    qr=qr.make(data)
    qr.save(f"link.png")
    print("qr code made successfully")
