#Giorgio Bruno Modeo
import os

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
autovettura=[]
inp=[]
def main():
    while a:
        del inp[:]
        menu()
        
def menu():
    scelta = input(f"{autosalone}\ninserire la scelta: ")
    match scelta:
        case "1":
            os.system("cls")
            inserimento()
        case "2":
            os.system("cls")
            print("cilindrata")
            sup1500()
        case "3":
            os.system("cls")
            print("totale auto")

        case "4":
            os.system("cls")
            print("cilindrata")

        case "5":
            os.system("cls")
            print("cilindrata")

        case _:
            os.system("cls")
            global a
            a = False
def inserimento():
    while True:
        try:
            inp.append(int(input("inserire l'anno della vettura: ")))

            inp.append(str(input("inserire la marca della vettura: ")))
            inp.append(int(input("inserire la cilindrata della vettura: ")))
            inp.append(str(input("inserire il proprio nome: ")))
            inp.append(str(input("inserire il proprio cognome: ")))
            break
        except:
            os.system("cls")
            print("hai sbagliato input reinserisci i dati\n")
    autovettura.append( {inp[0]:{inp[1]:[inp[2],inp[3],inp[4]]}} )
    print(autovettura)

def sup1500():
    print("I clienti che hanno un autovettura con cilindrata superiore a 1500 sono")
    i =1
    for i in autovettura:
        for ch in autovettura[0]:
            for key in autovettura[0][ch]:
                print(autovettura)
                print(autovettura[i])
                print(autovettura[0][ch])
                print(autovettura[0][ch][key])
                print(autovettura[0][ch][key][0])
                if autovettura[0][ch][key][0] >= 0:
                    print(f"    {autovettura[0][ch][key][2]}")
        i =+1
        print(i)

def tot_auto():
    scelta = int(input("in"))
main()