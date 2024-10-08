'''
#-----------------------#
Programm: 		Einheitenumrechner
Version: 		V1.0

Programmierer: 	Eberlei
Datum:			20.08.2024
#-----------------------#
'''
   
def input_check ():
    check = False				                    #Variable für while Schleife wird deffiniert
    
    while not check:
        user_inp = input("\nInput: ")
        user_inp = user_inp.replace("," , ".")
        
        try:
            user_inp = float(user_inp)	            #versucht Input in float umzuwandeln
            check_return = True	                    #wenn möglich, wird der Input zurückgegeben
            
        except ValueError:			                #wenn nicht möglich, wird Fehlermeldung rausgegeben
            check_return = False


        if check_return:							#nur wenn die Umwandlung erfolgreich war, enhält user_inp einen Wert größer 0
            check = True 
            
        else:
            check = False 
            print("\nInput can't include letters, try again")
            
    return user_inp


def digit_num ():                                   #kann auch über "match" Funktion  realisiert werden, Fehlermeldung ist aber ungenau
    list_digit = False
    menu_opt = [1,2,3,4,5,6]                        #Liste, die alle Zahlen der Menüoptionen beinhaltet
    while not list_digit:

        user_inp = input("Unit number: ")
        
        if user_inp.__len__() == 1:                 #Leitet Eingabe nur weiter, wenn sie aus max. 1 Wert besteht

            if user_inp.isdigit():
                user_inp = int(user_inp)            #funktion .isdigit muss ein string sein, zum abgleich der Liste wird ein integer benötigt

                if user_inp in menu_opt:            #Durchsucht die Liste nach einer übereinstimmung
                    list_digit = True
                    return user_inp
                else:
                    print("invalid input. Must between 1-6")
                    
            else:
                print("invalid input. Must be a number, without dezimal characters")

        else:
            print("invalid input. Must be only one character")
            

while True:
    print(
        "\nChoose unit you want do transfer:\n"

        "------------\n" #12x -
        "1. cm to inch \n"
        "2. km to eng. mile / international seemile \n"
        "3. liter to beer \n"
        "4. kg to pound \n"
        "5. Celsius to Kelvin \n"
        "6. Exit Programm \n"
        "------------"
        )
    

    unit_num = digit_num()                                  #checks input if it is a single, int character

    if unit_num == 6:
        print("\nHave a nice day :)\n"
              "\n-- programm closed --\n")
        break
                   
    checked_inp = float(input_check())                      #checks, if the input include letters    


    match unit_num:

        case 1 :
            inch = round(checked_inp / 2.54, 3)			    #inch = 2.54cm 
            print(f"\n{checked_inp}cm are {inch} inch.")
                  
        case 2 :
            eng_mile = round(checked_inp / 1.60934, 3) 		#englisch mile = 1.60934 km
            seemile = round(checked_inp / 1.852, 3)			#international seemile = 1.852 km
            print(f"\n{checked_inp}km are {eng_mile} englisch miles or {seemile} international seemiles.")
                  
        case 3 :
            beer = round(checked_inp / 0.33, 2)             #one beer has 330ml
            complete_beer = int(beer // 1) 			
            print(f"\n{checked_inp} liter are {beer} beers, roundet {complete_beer} complete 0,33l beer.") 
                  
        case 4 :
            pound = round(checked_inp / 0.5, 2)				#Pound = 500g
            print(f"\n{checked_inp}kg are {pound} pound.") 
                  
        case 5 :
            kelvin = round(273.15 + checked_inp, 2) 		#Kelvin starts at -273.15°C. 273.15 Kelvin is equal to 0°C
            print(f"\n{checked_inp}°C are {kelvin} Kelvin.")
            
        case _:
            print("\ninvalid unit number. Muste be a single character number")
            
    
              
              