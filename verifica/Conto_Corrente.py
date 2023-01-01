#Giorgio Bruno Modeo
import os
from random import randint

cont_cor = """
            *********************************
            *         CONTO CORRENTE        *
            *********************************

            *********************************
            *   MENÙ UTENTE PRINCIPALE      *
            *********************************
            *   1 SALDO                     *
            *   2 PRELIEVO                  *
            *   3 VERSAMENTO                *
            *   4 STAMPA L'ULTIMO MOVIMENTO *
            *   5 ======> USCITA            *
            *********************************

"""
#                                                                                   definisco il saldo inizziale del conto
saldo = randint(50,1000)
#                                                                                   {um} mi servira per verificare l'ultimo movimento
um = ""
a = True

#                                                                                   + main
def main():
    while a:
        os.system("cls")
        menu()
        
#                                                                                   + menu
def menu():
#                                                                                      faccio sciegliere al utente l'azzione da fare
    scelta = input(f"{cont_cor}\ninserire la scelta: ")
    match scelta:
#                                                                                         prima scelta verificare il saldo inizziale
        case "1":
            os.system("cls")
            print(f"SALDO DISPONIBILE: {saldo} ")
            continua()
#                                                                                         seconda scelta prelievo dal conto
        case "2":
            os.system("cls")
            print("PRELIEVO\n")
            prelievo()
            continua()
#                                                                                         terza  scelta versamento sul conto 
        case "3": 
            os.system("cls")
            print("VERSAMENTO\n")
            versamento()
            continua()
#                                                                                         quarta  scelta stampa dell'ultimo movimento 
        case "4": 
            os.system("cls")
            print("ULTIMO MOVIMENTO\n")
            sta_ult_mov()
            continua()
#                                                                                         default uscita
        case _:
            print("Grazzie per aver utilizzato il programma")
            global a
            a = False
#                                                                                   + prelievo

def prelievo():
#   definisco queste variabili {saldo,um} globale in modo che una volta modificate in questa funzione vengano mantenute in tutto il codice
    global saldo,um
#                                                                                      faccio sciegliere al utente l'inporto da prelevare
    while True:
        try:
            prelievo = int(input(f"saldo disponibile: {saldo}\ninserisci il valore da prelevare: "))
            break
        except:
            print("reinserire il valore")
#                                                                                      verifico che l'inporto che il cliente vuole prelevare sia inferiore al saldo
    if prelievo > saldo:
#                                                                                         se l'inporto che il cliente vuole prelevare è superiore al saldo
#                                                                                         gli chiedo se vuole fare un debito con la banca
#                                                                                         se inserisce "s" addebito il prelievo altrimenti annullo l'operazzione
        s = input("Il prelievo che stai effettuando e superiore al saldo\nLo sconfinamento del saldo richiede interessi del 20%\nSei sicuro di voler svolgere l'operazzione? s=Si:  ")
        if s == "s":
            saldo = saldo - prelievo
            print(f"prelievo effettuato!! saldo aggiornato: {saldo} ")
            um = f"prelievo valore = {prelievo} "
        else: 
            print(f"prelievo annullato dall'utente!!  Saldo invariato {saldo}")
#                                                                                      se l'inporto che il cliente vuole prelevare è inferiore al saldo gli addebito il prelievo
    else:
        saldo = saldo - prelievo
        um = f"prelievo valore = {prelievo} "
        print(f"prelievo effettuato!! saldo aggiornato: {saldo} ")
#                                                                                   + versamento

def versamento():
#   definisco queste variabili {saldo,um} globale in modo che una volta modificate in questa funzione vengano mantenute in tutto il codice
    global saldo,um
#                                                                                      creo un ciclo in modo da permettere al utente di sbagliare e riprovare l'inserimento
    while True:
#                                                                                         provo a far inserire i dati al utente se sbaglia il comando try: 
#                                                                                         non fara restituire l'errore 
        try:
#                                                                                            faccio sciegliere al utente l'importo del versamento 
#                                                                                            e verifico che sia un importo valido o "0" per annullare
            versamento = int(input(f'saldo disponibile: {saldo}\ninserire "0" per annullare\ninserisci il valore da versare: '))
            if versamento > 0:
                saldo = saldo + versamento
                print(f"versamento effettuato!! nuovo saldo: {saldo}")
                um = f"versamento valore = {versamento}"
                break
            elif versamento == 0:
                print(f"versamento annullato: {saldo}")
                break
            else:
                print("inserimento errato")
        except:
            print("inserimento errato")
#                                                                                   + stampa ultimo movimento

def sta_ult_mov():
#                                                                                      verifico che l'utente abbia fatto almeno un movimento
    if um == "":
        print("effettuare prima un movimento")
#                                                                                      se l'ho ha fatto lo stampo
    else:
        print(um)   
       
#                                                                                   + continua
def continua():
    input("premere invio per continuare...")
main()
# 96 stringe compilate
# 30 commenti