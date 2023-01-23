#modeo giorgio

# quota fissa = mq * n_persone
# quota fissa + quota variabile 
#  m    € a persona     tot     tar fissa 
# 100 * 1,23764     = 123,764 + 49,92488

tari = []

def main():
    f_menu()
    print(tari)


#                                                                               menu prima categoria
def f_menu():
    m = """ 

        1. Inserimento dati

        2. Stampa informazioni TARI

        3. Uscita
    """
    menu = input(m +": ")

    match menu:
        case "1":
            print("inserimento dati")
        case "2":
            print("stampa informazzioni")
        case _:
            print("uscita")  



#                                                                               imput per la prima categoria
def imp_cat_1():
    a = True
    while True:
        if a:
            print("inserisci i metri quadrati della casa: ")
            Con_Inp()
            a =False
        else:
            print("inserisci i componenti della famiglia: ")
            Con_Inp()
            break
        
    match tari[1]:
        case 1:
            cas1()
        case 2:
            tari.append(1.45422)
        case _:
            tari.append(1.62440)


#                                                                               controllo imput
def Con_Inp():
    try:
        tari.append(float(input("   ")))
    except:
        print("hai sbagliato input reinserisci il dato")
        
def cas1():
    tari.append(1.23764)
    tari.append(round((tari[0]*tari[2]),5))
    tari.append(49.92488)
    tari.append(round((tari[3] + tari[4]),5))

main()

