from abc import ABC, abstractmethod
#from datetime import date
#creo classe astratta
class Persona(ABC):
    #annoattuale=date.today().year
    #ANNOATTUALE=date.today().year
    def __init__(self, nome:str,cognome:str,matricola:str,annoassunz:int):
        self.__nome= nome    
        self.__cognome=cognome
        self.__matricola=matricola
        self.__annoassunz=annoassunz
       
    def getnome(self):
        return self.__nome
    def getcognome(self):
        return self.__cognome
    def getmatricola(self):
        return self.__matricola
    def getannoassunz(self):
        return self.__annoassunz
    
    def setnome(self, nome):
        self.__nome=nome
    def setcognome(self, cognome):
        self.__cognome=cognome
    def setmatricola(self, mat):
        self.__matricola=mat
    def setannoaasunz(self, anno):
        self.__annoassunz=anno
    # overriding metodo __eq__() per confronto di oggetti
    def __eq__(self,p):
        if isinstance(p,Persona):
            return ((p.getnome()==self.__nome) and (p.getcognome()==self.__cognome) and (p.getannoassunz()==self.__annoassunz) and (p.getmatricola()==self.__matricola))
        else:
            return None
    # overriding
    def __str__(self):
        return "Nome: "+self.__nome+"\nCognome: "+self.__cognome+"\nMatricola: "+self.__matricola+"\nAnno assunzione: "+str(self.__annoassunz)
    
    @abstractmethod #metodo astratto che calcola il costo di partecipazione al progetto. Non implementato   
    def getCostoC(self,anno=None):
        pass
    
# p1=Persona("mario","rossi","a34",2000)
# print(p1)