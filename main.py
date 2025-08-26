import qrcode as qr
choose = input ("enter what type of qr code you want to generate:\n"
                "1.any text or number\n"
                "2.for any phone number\n"
                "3.for direct opening whatsapp chat\n"
                "4.for any web link\n"
                "5.for upi qr code\n"
                "enter the number of what type of qr code you want to generate(1/2/3/4/5):")
if choose == "1":

    data = input ("enter your text or number data to make qr code:")
    qr = qr.make(data)
    qr.save(f"{data}.png")
    print("qr code made successfully")

elif choose == "2":
    data = input ("enter your phone number data to make qr code:")
    phone = "tel:" + data
    qr = qr.make(phone)
    qr.save(f"{data}.png")
    print ("qr code made successfully")

elif choose == "3":
    data = input ("enter your direct opening whatsapp chat(need to write with country code(eg.91 for india )):")
    text= input ("you can enter your msg automatically(for space you have to enter %20):")
    link= f"https://wa.me/{data}?text={text}"
    qr = qr.make(link)
    qr.save(f"{data}.png")
    print ("qr code made successfully")

elif choose == "4":
    data = input ("paste or write down your link: ")
    qr=qr.make(data)
    qr.save(f"link.png")
    print("qr code made successfully")

elif choose == "5":
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

else :
    print ("choose a valid option")



