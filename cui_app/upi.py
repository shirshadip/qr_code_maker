def upi ():
    import qrcode as qr 
    import datetime
    import os 
    now = datetime.datetime.now()
    #upi payment info 
    upi_id = input("enter your upi id(eg. yourupiid@bank):") #your upi id 
    name = input("enter your name:") #your name
    amount = input("enter amount:") #optional
    currency = input("enter currency(eg. INR):")

    #upi link 
    upi_link = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu={currency}"

    #generate qr
    qr = qr.make(upi_link)
    save=r"D:\repositories\qr_code_maker\qr_codes"
    file_path = os.path.join(save,f"{now}.png")
    qr.save(file_path)
    

    print ("upi qr code generated succesfully")
