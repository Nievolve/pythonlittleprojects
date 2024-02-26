
        #Funktion för att presentera menyn
def menu(start_menu):
    start_menu = ["Menu", "Välj ett alternativ", "1. Beräkna Skatt", "2. Avsluta program"]
    for formenu in start_menu:
        print(formenu)
        ##

        #Funktion som beräknar skatt och returnerar skatte uträkningen
def taxes_calc(taxes):
    nedre_grans = 438_900
    ovre_grans = 638_500
    avdrag = 13_100
    real_taxes = 0
    rest_taxes = 0
    taxes = taxes -avdrag
            #If elif satser som kontrollerar värdet på årsinkomsten
    if taxes < nedre_grans:
        print("Ingen statlig skatt kommer dras." )
    elif nedre_grans <= taxes <= ovre_grans:

        real_taxes = taxes * 0.8
        rest_taxes = taxes - real_taxes

        print("Statliga skatten blir " + str(rest_taxes))
        print("Netto blir " + str(real_taxes))


    elif taxes >= ovre_grans:
        real_taxes = taxes * 0.75
        rest_taxes = taxes - real_taxes

        print("Statliga skatten blir " + str(rest_taxes) + " kr")
        print("Netto blir " + str(real_taxes) + " kr")



        ##







start_menu = []
while True:
    menu(start_menu)
    menu_button = int(input(": "))
    if menu_button ==1:
        print("Vad är årsinkomsten?")
        taxes = int(input(": "))
        taxes_calc(taxes)

    elif menu_button == 2:
        print("Avslutar program...")
        quit()










