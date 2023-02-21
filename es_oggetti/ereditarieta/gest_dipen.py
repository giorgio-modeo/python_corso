from dipendente import dipendente
from main import istr

class gest_dipen():
    def __init__(self):
        self._elenco=[]

    def aggiungidipendente(self,dipendente):
        self._elenco.append(dipendente(istr("inserisci il nome: "),istr("inserisci l'indirizzo: "),istr("inserisci il sesso(M,F,O): ")))
        print(self._elenco)