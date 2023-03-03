from Persona import Persona

class FunzionarioSenior(Persona):
    costo=80     #variabile statica
    def __init__(self,nome, cognome, codice,anno,orelav):
        super().__init__(nome,cognome,codice,anno)
        self.__orelavorate=orelav

    def get_orelavorate(self):
        return self.__orelavorate
    
    def set_orelavorate(self,orelav):
        self.__orelavorate=orelav

    #metodo di classe (statico) per conoscere il costo orario dei funzionari
    @classmethod
    def getcosto(cls):
        return cls.costo
    
    #implementazione del metodo astratto
    def getCostoC(self,anno=None):
        return FunzionarioSenior.costo*self.__orelavorate;

    # overriding metodo __eq__() per confronto di oggetti
    def __eq__(self, funzionario):
        if isinstance(funzionario,FunzionarioSenior):
            return (super().__eq__(funzionario) and (funzionario.get_orelavorate()==self.__orelavorate))
        else:
            return None
    def __str__(self):
        return super().__str__()+" Ore lavorate: "+str(self.__orelavorate)


#t1=FunzionarioSenior("mario","rossi","a34",2000,50)

#print(t1,"\nCosto partecipazione progetto: ",t1.getCostoC())