from abc import ABC, abstractmethod
class prodotto():

    def __init__(self,nome,descrizione,prezzo,quantita):
        self._code = 0
        self._nome = nome
        self._descrizione = descrizione
        self._prezzo = prezzo
        self._quantita = quantita

    def getCode(self):
        return self._code
    def getNome(self):
        return self._nome
    def getDescrizione(self):
        return self._descrizione
    def getPrezzo(self):
        return self._prezzo
    def getQuantita(self):
        return self._quantita
    
    def setCode(self,code):
        self._code = code +1
    def setNome(self,nome):
        self._nome = nome
    def setDescrizione(self,descrizione):
        self._descrizione = descrizione
    def setPrezzo(self,prezzo):
        self._prezzo = prezzo
    def setQuantita(self,quantita):
        self._quantita = quantita
    
    def __str__(self):
        return "Codice: " + str(self.getCode()) + "\nNome: " + self.getNome() + "\nDescrizione: " \
            + self.getDescrizione() + "\nPrezzo: " + str(self.getPrezzo()) + "\nQuantita: " + str(self.getQuantita()) + "\n"
    @abstractmethod
    def tassa(self):
        pass

# a = prodotto( "test", "test", 100, 1)
# while True: 
#     print(a)
#     if a.getCode() >= 2:
#         break
#     else:
#         a.setCode(a.getCode())
        