from Veicolo import veicolo
class AutoVettura(veicolo):
    def __init__(self,marca,targa,costo,posti):
        super().__init__(marca,targa,costo)
        self.__posti = posti
    def getPosti(self):
        return self.__posti
    def setPosti(self,posti):
        self.__posti = posti

    def __str__(self):
        return super().__str__() + "\nPosti: " + str(self.__posti)
