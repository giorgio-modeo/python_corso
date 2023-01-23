import os
menu ="""
***********************
    1. option 1
    2. option 2
    3. option 3
    4. option 4
    5. option 5
    0. end
***********************
""" 
scelta= -1
while scelta != 0:
    os.system("cls")
    print(menu)
    scelta=input("scegli: ")
    
    match scelta:
        #option 1
        case '1':
            print("option 1")
        #option 2
        case '2':
            print("option 2")
        #option 3
        case '3':
            print("option 3")
        #option 4
        case '4':
            print("option 4")
        #option 5
        case '5':
            print("option 5")
        #defoult
        case '0':
            print("fine")
        case _:
            print("fine")
    input("premi invio per continuare... ")