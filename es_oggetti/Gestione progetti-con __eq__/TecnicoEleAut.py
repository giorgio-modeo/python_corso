from Persona import Persona

class TecnicoEleAut(Persona):
    costo=50
    def __init__(self,nome:str,cognome:str,codice:str,annoInizio:int,orelav:int,interno:bool):
        super().__init__(nome,cognome,codice,annoInizio)
        self.__orelavorate=orelav
        self.__interno=interno

    def getorelavorate(self):
        return self.__orelavorate
    
    def set_orelavorate(self,orelav):
        self.__orelavorate=orelav
        
    def getinterno(self):
        return self.__interno
    def setinterno(self,interno:bool):
        self.__interno=interno

    #metodo di classe (statico) per conoscere il costo orario del tecnico
    @classmethod
    def getcosto(cls):
        return cls.costo
    
    def getCostoC(self,anno=None):
        #anni=Persona.ANNOATTUALE-self._annoassunz;
        anni=anno-self.getannoassunz()
        if self.__interno==True:
            risultato=(TecnicoEleAut.costo*self.__orelavorate)+anni*self.__orelavorate;
        else:
            risultato=TecnicoEleAut.costo*self.__orelavorate;
        return risultato;

    # overriding metodo __eq__() per confronto di oggetti    
    def __eq__(self, tecnico):
        if isinstance(tecnico,TecnicoEleAut):
            return ((super().__eq__(tecnico)) and (tecnico.getorelavorate()==self.__orelavorate) and (tecnico.getinterno()==self.__interno))
        else:
            return None

    def __str__(self):
        st="INTERNO " if self.__interno==True else " ESTERNO "
        return super().__str__()+" Ore lavorate: "+str(self.__orelavorate)+ " "+st


#t1=TecnicoEleAut("mario","rossi","a34",2000,50,True)
#print(t1)
#print(t1,"\nCosto partecipazione progetto: ",t1.getCostoC())