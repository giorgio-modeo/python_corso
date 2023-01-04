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

#                                                                                   + main
def main():
    while a:
        os.system("cls")
        del inp[:]
        menu()

#                                                                                   + menu
def menu():
#                                                                                      faccio sciegliere al utente l'azzione da fare
    scelta = input(f"{autosalone}\ninserire la scelta: ")
    match scelta:
#                                                                                         prima scelta inserire i dati dell autovettura
        case "1":
            os.system("cls")
            inserimento()
            continua()
#                                                                                         seconda scelta visualizzare il cognome degli acquirenti con un veicolo che supera i 1500cc 
        case "2":
            os.system("cls")
            print("cilindrata")
            sup1500()
            continua()
#                                                                                         terza scelta numero totale di auto immatricolate in un anno richiesto
        case "3":
            os.system("cls")
            print("totale auto")
            tot_auto()
            continua()
#                                                                                         quarta scelta ordinare l’elenco in base all’anno di immatricolazione 
        case "4":
            os.system("cls")
            print("ordina elenco")
            ordina()
            continua()
#                                                                                         quinta scelta stampare l’elenco ordinato
        case "5":
            os.system("cls")
            print("stampa l'elenco ordinato")
            stamp_ord()
            continua()
#                                                                                         default uscita
        case _:
            os.system("cls")
            print("arivederci")
            global a
            a = False

#                                                                                   + inserimento dati autovettura
def inserimento():
#                                                                                         faccio inserire al utente i dati controllandoli uno per uno
    inpint("inserire l'anno della vettura: ")
    inpstr("inserire la marca della vettura: ")
    inpint("inserire la cilindrata della vettura: ")
    inpstr("inserire il proprio nome: ")
    inpstr("inserire il proprio cognome: ")
#                                                                                         inserisco i dati in una lista di liste 
    autovettura.append([inp[0],inp[1],inp[2],inp[3],inp[4]]) 

#                                                                                   + superiore a 1500cc
def sup1500():
#                                                                                         verifico le autovetture con la cilindrata superiore a 1500cc e lo stampo
    print("I clienti che hanno un autovettura con cilindrata superiore a 1500 sono")
    for i in range(len(autovettura)):
        if autovettura[i][2] >= 1500:
            print(autovettura[i][4])

#                                                                                   + totale auto
def tot_auto():
#                                                                                         faccio inserire l'anno desiderato e verifico le autovetture
#                                                                                         con la data di immatricolazione uguale a quello impostato dal utente
    inpint("inserire l'anno: ")
    count = 0
    for i in range(len(autovettura)):
        if autovettura[i][0] == inp[0]:
            count= count +1
    print(f"ci sono {count} auto inmatricolate nel {inp[0]}\n")

#                                                                                   + ordinamento in base al anno
def ordina():
#   definisco questa variabile {autovettura2} globale in modo che una volta modificata in questa funzione venga mantenuta in tutto il codice
    global autovettura2
#   elimino la variabile {autovettura2} in modo che non i dati non si ripetano nel caso in cui l'utente decida di ordinare la lista e poi inserire ulteriori dati
    del autovettura2[:]
#                                                                                         verifico che l'utente abbia inserito almeno un autovettura 
#                                                                                         altrimenti ne forzo l'inserimento
    while True:
        if len(autovettura)== 0:
            print("inserisci prima un autovettura\n")
            inserimento()
        else:
            autovettura2.extend(sorted(autovettura,key=itemgetter(0)))
            print("\nordinamento riusito\n")
            break

#                                                                                   + stampa la lista ordinata 
def stamp_ord():
#                                                                                         verifico che lutente abbia ordinato la lista altrimenti ne forzo l'inserimento
    ordina()
    print("************** Auto immatricolate **************************")
#                                                                                         stampo ogni autovettura
    for i in range(len(autovettura2)):
#                                                                                            verifico che l'anno dal autovettura sia uguale a quello del precedente
#                                                                                            quindi non ci sara bisogni di stamparlo
        if (autovettura2[i][0] == autovettura2[i-1][0]) and (i > 0):
            print(f"          {autovettura2[i][1]},{autovettura2[i][2]},{autovettura2[i][3]},{autovettura2[i][4]}" )
#                                                                                            invece se l'anno non e mai comparso precedentemente lo stampo insieme agli altri dati
        else:
            print(f"  {autovettura2[i][0]}:\n          {autovettura2[i][1]},{autovettura2[i][2]},{autovettura2[i][3]},{autovettura2[i][4]}" )
    print("*********************************************************")   
#                                                                                   + input dedicato agli interi
def inpint(stri):
    while True:
        try:
            inp.append(int(input(stri)))
            break
        except:
            os.system("cls")
            print("input errato")
#                                                                                   + input dedicato alle stringhe
def inpstr(stri):
     while True:
        try:
            inp.append(str(input(stri)))
            break
        except:
            os.system("cls")
            print("input errato")
#                                                                                   + continua      
def continua():
    input("premere invio per continuare...")
main()
# 117 stringe compilate
# 32 commenti