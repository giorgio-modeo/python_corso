from abitazione import *
class Immobile():
    def __init__(self,numStanze,tipo,mq,anno,giardino,indirizzo,città):
        self._numStanze = numStanze
        self._tipo = tipo
        self._mq = mq
        self._anno = anno
        self._giardino = giardino
        self._indirizzo = indirizzo
        self._città = città

    def prezzo(self):
        return self._tipo * Abitazione._prezzo()f
        

    def __str__(self):
        st= f"tipo di immobile={self._tipo},metri quadrati={self._mq},anno di costruzzione={self._anno}"
        if self._giardino == "1":
            st+=f"avente giardino"
        else:
            st+=f"non avente giardino"
        return st
