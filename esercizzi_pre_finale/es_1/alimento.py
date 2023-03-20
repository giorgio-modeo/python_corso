from prodotto import prodotto
class Alimento(prodotto):
    def __init__(self,nome,descrizione,prezzo,quantita,scadenza,sconto):
        super().__init__(nome,descrizione,prezzo,quantita)
        self._scadenza = scadenza
        self._sconto = sconto
    
    def getScadenza(self):
        return self._scadenza
    def getSconto(self):
        return self._sconto
    
    def setSconto(self,sconto):
        if self._quantita <= 5:
            self._sconto = self._prezzo - self._prezzo * 0.1
    def __str__(self):
        return super().__str__() + "Scadenza: " + str(self._scadenza) + " \nSconto: " + str(self._sconto)
# a = prodotto( "test", "test", 100, 1)
# a = alimento( "test2", "test2", 100, 1, "13-12-2024", 0.1)
# print(a)

