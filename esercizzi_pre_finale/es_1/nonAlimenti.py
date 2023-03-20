from abc import ABC, abstractmethod
from prodotto import prodotto
class NonAlimento(prodotto):
    def __init__(self,nome,descrizione,prezzo,quantita,categoria,peso):
        super().__init__(nome,descrizione,prezzo,quantita)
        self._categoria = categoria
        self._peso = peso
        self._tassa = False

    
    def getCategoria(self):
        return self._categoria
    def getPeso(self):
        return self._peso
    def getTassa(self):
        return self._tassa
    
    def setCategoria(self,categoria):
        self._categoria = categoria
    def setPeso(self,peso):
        self._peso = peso
    def setTassa(self):
        if self._categoria == ("elettronica"or"Elettronica" or "libri"or "Libri"):
            self._tassa = True
        else:
            pass
    
    def tassa(self):
        if self._tassa: return f"tassa: {self._prezzo * 0.1}"
        else: return f"{self._nome} non è tassato"


    def __str__(self):
        return super().__str__() + "categoria: " + str(self._categoria) + " \npeso: " \
        +str(self._peso) + " \ntassa: " + str(self._tassa)+ "\n"+ self.tassa()

# a = NonAlimento( "test2", "test2", 100, 1, "elettronica", 0.5)
# a.setTassa()
# print(a,"\n",a.tassa())

