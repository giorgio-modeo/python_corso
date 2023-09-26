class veicolo():
    def __init__(self,marca,targa,costo):
        self.__marca = marca
        self.__targa = targa
        self.__costo = costo
    
    def getMarca(self):
        return self.__marca
    def getTarga(self):
        return self.__targa
    def getCosto(self):
        return self.__costo
    
    def setMarca(self,marca):
        self.__marca = marca
    def setTarga(self,targa):
        self.__targa = targa
    def setCosto(self,costo):
        self.__costo = costo
    
    def __str__(self):
        return f"Marca {self.__marca}\nTarga {self.__targa}\nCosto {self.__costo}"
a =veicolo("a", "a", "a")
a.setTarga("b")
print(a)