#from sys import path
#path.append('model') # mettere la cartella nel path permette di fare import trovando i moduli
#print(path)
#se i file sono in una sottocartellla 'model' si richiamano con
# from model.Dirigente import Dirigente
from Dirigente import Dirigente
from FunzionarioSenior import FunzionarioSenior
from FunzionarioJunior import FunzionarioJunior
from TecnicoEleAut import TecnicoEleAut
from TecnicoInFTel import TecnicoInfTel

class GestioneProgetti(object):
    def __init__(self):
        self.__elenco=[]
    
    # aggiunta una persona al progetto
    def aggiungiPersona(self,p):
        self.__elenco.append(p)
    

    # elimina una persona dal progetto ricerca per nome
    def eliminaPersona(self,nominativo):
        trovato=False        
        for p in self.__elenco: 
            if p.getcognome()==nominativo:
                self.__elenco.remove(p)
                trovato=True
                break
        return trovato
    #cerca una persona per cognome e ritorna l'elemento    
    def cercaPersona(self,nome):
        trovato=False
        for elem in self.__elenco:
            #print(elem.getcognome())
            if elem.getcognome()==nome:
                trovato=True
                break
        return trovato,elem
    
    def elencoPersone(self):
    # elenco partecipanti al progetto
        persone = ""
        for p in self.__elenco:
            persone +=p.getcognome()+" "+p.getnome()+" "
            #print(type(p))
            if isinstance(p,Dirigente):
                persone +=" Dirigente \tMatricola: "+p.getmatricola() #+"\t\t\tCosto: "+str(p.getCostoC())
            if isinstance(p,FunzionarioSenior):
                persone +=" Funzionario senior Matricola: "+p.getmatricola() #+"\t\t\tCosto: "+str(p.getCostoC())
            if isinstance(p,FunzionarioJunior):
                persone +=" Funzionario junior Matricola: "+p.getmatricola() #+"\t\t\tCosto: "+str(p.getCostoC())
            if isinstance(p,TecnicoInfTel):
                persone +=" Tecnico Informatico Matricola: "+p.getmatricola() #+"\t\tCosto: "+str(p.getCostoC())
            if isinstance(p,TecnicoEleAut):
                persone +=" Tecnico Elettronico Matricola: "+p.getmatricola() #+"\t\tCosto: "+str(p.getCostoC())
            persone+="\r\n"
        return persone
    
    def getTotalePersone(self):
        return len(self.__elenco)

    # Calcola costi progetto
    def Costiprogetto(self,anno):
        totcosti=0;
        for pers in self.__elenco:
            totcosti=totcosti+pers.getCostoC(anno)
        return totcosti;

    # overriding metodo __eq__() per confronto di oggetti    
    def __eq__(self,progetto):
        if isinstance(progetto,GestioneProgetti):
            return progetto.getElenco() == self.__elenco
        else:
            return None
    # metodo necessario per confronto di due liste di persone partecipanti al progetto    
    def getElenco(self):
        return self.__elenco
    
    def __str__(self):
        return self.elencoPersone()
