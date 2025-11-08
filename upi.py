def upi ():
    import qrcode as qr 
    #upi payment info 
    upi_id = input("enter your upi id(eg. yourupiid@bank):") #your upi id 
    name = input("enter your name:") #your name
    amount = input("enter amount:") #optional
    currency = input("enter currency(eg. INR):")

    #upi link 
    upi_link = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu={currency}"

    #generate qr
    qr = qr.make(upi_link)
    qr.save(f"{name}.png")

    print ("upi qr code generated succesfully")
