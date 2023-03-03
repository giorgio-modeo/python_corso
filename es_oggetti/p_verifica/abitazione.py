from immobile import Immobile

class Abitazione(Immobile):
    def __init__(self,numStanze,tipo,mq,anno,giardino,indirizzo,città):
        super().__init__(numStanze,tipo,mq,anno,giardino,indirizzo,città)
        self._prezzo=12

    def __str__(self):
        return f"{super().__str__()} Prezzo: {self._prezzo}"

        
