from impiegato import impiegato
from docente import docente
from gest_dipen import gest_dipen

menu ="""
1.Aggiunta di un nuovo dipendente (Impiegato o Docente)
2.Eliminazione di un dipendente a partire dal nome
3.Ricerca di un dipendente a partire dal nome
4.Visualizzazione di tutti i dipendenti
5.Stampa del numero totale dei dipendenti
6.Eliminazione di tutti i dipendenti
7. Esci
"""

def istr(st):
    a = str(input(st))
    return a


s = int(input(menu+"\n: "))
match s:
    case 1:
        s=int(input("1) Impiegato \n2) Docente\n: "))
        if s == 1:
            dipe=impiegato(istr("inserisci il nome: "),istr("inserisci l'indirizzo: "),istr("inserisci il sesso(M,F,O): "),istr("inserisci l'ufficio: "))
        elif s == 2:    
            dipe=docente(istr("inserisci il nome: "),istr("inserisci l'indirizzo: "),istr("inserisci il sesso(M,F,O): "),istr("inserisci la disciplina: "),istr("inserisci il ruolo: "))
        else:print("input errato")
    case 2:
        gest_dipen.aggiungidipendente("marco","strada","M")




























