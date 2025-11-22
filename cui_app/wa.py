def what():
    import qrcode as qr 
    data = input ("enter your direct opening whatsapp chat number(need to write with country code(eg.91 for india )):")
    text= input ("you can enter your msg automatically(for space you have to enter %20):")
    link= f"https://wa.me/{data}?text={text}"
    qr = qr.make(link)
    qr.save(f"{data}.png")
    print ("qr code made successfully")