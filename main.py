
try:
    import qrcode as qr
    choose = input ("enter what type of qr code you want to generate:\n"
                    "1.any text or number\n"
                    "2.for any phone number\n"
                    "3.for direct opening whatsapp chat\n"
                    "4.for any web link\n"
                    "5.for upi qr code\n"
                    "enter the number of what type of qr code you want to generate(1/2/3/4/5):")
    if choose == "1":

            import txt
            
            print (txt.txt())
            

    elif choose == "2":
        import ph 
        print (ph.ph())

    elif choose == "3":
        
        import wa 
        print (wa.what())
    elif choose == "4":
        import link
        print (link.link())
    elif choose == "5":
        
        import upi
        print (upi.upi())
    else :
        print ("choose a valid option")
except ModuleNotFoundError:
    print("qr code module is not found, please run the download.bat file ")