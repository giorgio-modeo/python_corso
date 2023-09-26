from Veicolo import veicolo
class furgone(veicolo):
    def __init__(self,marca,targa,costo,capacita):
        super().__init__(marca,targa,costo)
        self.__capacita = capacita
    def getCapacita(self):
        return self.__capacita
    def setCapacita(self,capacita):
        self.__capacita = capacita
    
    def __str__(self):
        return super().__str__()+ "\nCapacita" + str(self.__capacita)
        