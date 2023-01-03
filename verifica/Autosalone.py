#Giorgio Bruno Modeo
import os
from operator import itemgetter

autosalone = """
            *************************************************
            *                   AUTOSALONE                  *
            *************************************************

            *************************************************
            *             MENÙ UTENTE PRINCIPALE            *
            *************************************************
            *   1 INSERIMENTO AUTOVETTURA                   *
            *   2 ACQUIRENTI CILINDRATA SUPERIORE A 1500CC  *
            *   3 TOTALE AUTO                               *
            *   4 ORDINA ELENCO PER ANNO                    *
            *   5 STAMPA ELENCO                             *
            *   6 ======> USCITA                            *
            *************************************************

"""
a = True
autovettura,autovettura2=[],[]
inp=[]
def main():
    while a:
        os.system("cls")
        del inp[:]
        menu()
        
def menu():
    scelta = input(f"{autosalone}\ninserire la scelta: ")
    match scelta:
        case "1":
            os.system("cls")
            inserimento()
            continua()
        case "2":
            os.system("cls")
            print("cilindrata")
            sup1500()
            continua()
        case "3":
            os.system("cls")
            print("totale auto")
            tot_auto()
            continua()
        case "4":
            os.system("cls")
            print("ordina elenco")
            ordina()
            continua()

        case "5":
            os.system("cls")
            print("stampa l'elenco ordinato")
            stamp_ord()
            continua()

        case _:
            os.system("cls")
            print("arivederci")
            global a
            a = False
def inserimento():
    while True:
        try:
            inpint("inserire l'anno della vettura: ")
            inpstr("inserire la marca della vettura: ")
            inpint("inserire la cilindrata della vettura: ")
            inpstr("inserire il proprio nome: ")
            inpstr("inserire il proprio cognome: ")
            break
        except:
            os.system("cls")
            print("hai sbagliato input reinserisci i dati\n")
    autovettura.append([inp[0],inp[1],inp[2],inp[3],inp[4]])


    

def sup1500():
    print("I clienti che hanno un autovettura con cilindrata superiore a 1500 sono")
    for i in range(len(autovettura)):
        if autovettura[i][2] >= 1500:
            print(autovettura[i][4])

def tot_auto():
    inpint("inserire l'anno: ")
    count = 0
    for i in range(len(autovettura)):
        if autovettura[i][0] == inp[0]:
            count= count +1
    print(f"ci sono {count} auto inmatricolate nel {inp[0]}\n")

def inpint(stri):
    while True:
        try:
            inp.append(int(input(stri)))
            break
        except:
            os.system("cls")
            print("input errato")
        
def inpstr(stri):
     while True:
        try:
            inp.append(str(input(stri)))
            break
        except:
            os.system("cls")
            print("input errato")
def ordina():
    global autovettura2
    del autovettura2[:]
    while True:
        if len(autovettura)== 0:
            print("inserisci prima un autovettura\n")
            inserimento()
        else:
            autovettura2.extend(sorted(autovettura,key=itemgetter(0)))
            print("\nordinamento riusito\n")
            break
    

def stamp_ord():
    ordina()
    print("************** Auto immatricolate **************************")
    try:
        i=0
        for i in range(len(autovettura2)):
            if (autovettura2[i][0] == autovettura2[i-1][0]) and (i > 0):
                print(f"          {autovettura2[i][1]},{autovettura2[i][2]},{autovettura2[i][3]},{autovettura2[i][4]}" )
            else:
                print(f"  {autovettura2[i][0]}:\n          {autovettura2[i][1]},{autovettura2[i][2]},{autovettura2[i][3]},{autovettura2[i][4]}" )
    except:
        print("f")
    print("*********************************************************")   

 
def continua():
    input("premere invio per continuare...")
main()