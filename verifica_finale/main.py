from GestioneVeicoli import GestioneVeicoli
from AutoVettura import AutoVettura
from Furgone import furgone
from tool import *


def main():
    scelta = -1
    veicoli = GestioneVeicoli()
    while True:
        cls()
        print(menu('gestore veicoli (utilizzare i numeri per selezzionare)',["Inserisci veicolo",
                                    "Cancella Veicolo per targa",
                                    "Cerca veicolo per targa",
                                    "Stampa elenco dei veicoli in ordine crescente di targa",
                                    "Stampa numero totale dei veicoli",
                                    "Stampa costo totale dei veicoli"]))
        scelta = controllo_int("inserisci l'operazione: ")
        match scelta:
            case 1:
                print(menu("tipi",["autovettura","furgone"]))
                print("funziona")
                scelta = controllo_int("quale tipo di veicolo vuoi aggiungere: ")
                match scelta:
                    case 1:
                        aggiungiAutovettura(veicoli)
                    case 2:
                        aggiungiFurgone(veicoli)
                a = True
            case 2:
                if a:
                    targa = input("Inserisci il targa da cancellare: ")
                    c = cancellaVeicoloTarga(veicoli,targa)
                    if c == True:
                        print(f"Veicolo con la targa {targa}cancellato")
                    else:
                        print("Nessun veicolo con quella targa.")
                else:print("prima inserisci un veicolo")
            case 3:
                if a:
                    cerca = input("Inserisci il targa : ")
                    c = cercaVeicoloTarga(veicoli,cerca)
                    if c == False:
                        print("Nessun veicolo con quella targa.")
                else:print("prima inserisci un veicolo")
            case 4:
                if a:
                    ordinaVeicoliPerTarga(veicoli)
                    stampaVeicoliPerTarga(veicoli)
                else:print("prima inserisci un veicolo")
            case 5:
                if a:
                    stampaTotaleVeicoli(veicoli)
                else:print("prima inserisci un veicolo")
            case 6:
                if a:
                    stampaTotale_costo(veicoli)
                else:print("prima inserisci un veicolo")
            case 7:
                print("arrivederci.")
                break
            case _:
                print("Input non valido.")
        input("Premi invio per continuare...")


def sceltaVeicoli(sceltaVeicolo, veicoli):
    if sceltaVeicolo == 1:
        aggiungiAutovettura(veicoli)
    elif sceltaVeicolo == 2:
        aggiungiFurgone(veicoli)
    else:
        return False

def aggiungiAutovettura(veicoli):
    marca = controllo_string("inserisci la Marca: ")
    targa = controllo_string("inserisci la Targa: ")
    costo = controllo_float("inserisci il Costo: ")
    posti = controllo_int("inserisci i posti: ")
    veicolo = AutoVettura(marca, targa, costo, posti)
    veicoli.aggiungiVeicolo(veicolo)

def aggiungiFurgone(veicoli):
    marca = controllo_string("inserisci la Marca: ")
    
    targa = controllo_string("inserisci la Targa: ")
    costo = controllo_float("inserisci il Costo: ")
    capacita = controllo_int("inserisci la Capacita: ")
    veicolo = furgone(marca, targa, costo, capacita)
    veicoli.aggiungiVeicolo(veicolo)

    
def cancellaVeicoloTarga(veicoli,targa):
    controllo = veicoli.cancellaVeicolo(targa)
    if controllo == True:
        return True

def cercaVeicoloTarga(veicoli,cerca):
    controllo = veicoli.cercaVeicolo(cerca)
    if not controllo == True:
        return False
    
def ordinaVeicoliPerTarga(veicoli):
    veicoli.ordinaVeicoli()

def stampaVeicoliPerTarga(veicoli):
    veicoli.stampaVeicolo()

def stampaTotaleVeicoli(veicoli):
    veicoli.totaleVeicoli()

def stampaTotale_costo(veicoli):
    veicoli.costoTotale()


main()