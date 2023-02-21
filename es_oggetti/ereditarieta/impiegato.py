from dipendente import dipendente
class impiegato(dipendente):
    def __init__(self, nome,indirizzo,sesso,ufficio):
        super().__init__(nome,indirizzo,sesso)
        self.__ufficio=ufficio
    
    def getUfficio(self):
        return self.__ufficio

    def setUfficio(self,ufficio):   
        self.__ufficio = ufficio
    
    def __str__(self):
        return super().__str__()+" ufficio: "+self.__ufficio 














































