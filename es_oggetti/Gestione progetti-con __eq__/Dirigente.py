from Persona import Persona

class Dirigente(Persona):
    costo=100     #variabile statica
    def __init__(self,nome, cognome, codice,anno:int,orelav:int):
        super().__init__(nome,cognome,codice,anno)
        self.__orelavorate=orelav

    def get_orelavorate(self):
        return self.__orelavorate
    
    def set_orelavorate(self,orelav):
        self.__orelavorate=orelav
        
    #metodo di classe (statico) per conoscere il costo orario dei dirigenti
    @classmethod
    def getcosto(cls):
        return cls.costo
    
    #implementazione del metodo astratto
    def getCostoC(self,anno=None ):
        return Dirigente.costo*self.__orelavorate;
    # overriding metodo __eq__() per confronto di oggetti
    def __eq__(self, dirigente):
        if isinstance(dirigente,Dirigente):
            return ((super().__eq__(dirigente)) and (dirigente.get_orelavorate()==self.__orelavorate))
        else:
            return None

    def __str__(self):
        return super().__str__()+" Ore lavorate: "+str(self.__orelavorate)


#d1=Dirigente("mario","rossi","a34",2000,50)
#print(d1)
#print(d1,"\nCosto partecipazione progetto: ",d1.getCostoC())
#print("costo orario: ",d1.getcosto())