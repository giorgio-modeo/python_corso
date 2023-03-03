#from model import  Dirigente,Persona,FunzionarioJunior,FunzionarioSenior,TecnicoEleAut,TecnicoInFTel
from GestioneProgetti import GestioneProgetti
from Dirigente import Dirigente
from FunzionarioSenior import FunzionarioSenior
from FunzionarioJunior import FunzionarioJunior
from TecnicoEleAut import TecnicoEleAut
from TecnicoInFTel import TecnicoInfTel
from datetime import date

''' in fondo al main c'è la parte di confronto con gli oggetti'''

def Main():
    ANNO=date.today().year

    # creo progetto
    Progetto1=GestioneProgetti()
    print("Creo partecipanti al progetto: ")
    
    dirig1=Dirigente("Mario","Bianchi","123",2010,200)
#    dirig2=Dirigente("Mario","Bianchi","124",2011,150)
    FunzS1=FunzionarioSenior("Paolo","Rossi","221",2012, 100)
    FunzJ1=FunzionarioJunior("Marco","Verde","222", 2013, 92)
    TecI2=TecnicoInfTel("Davide","corti","301",2010,35,False)        
    TecE1=TecnicoEleAut("Giorgio","Marek","401",2008,28,True)
        #// inserimento persone al progetto
    Progetto1.aggiungiPersona(TecE1)
    print(TecE1.getcognome()+" "+TecE1.getnome(), " aggiunto al progetto: ")
    Progetto1.aggiungiPersona(TecI2);
    print(TecI2.getcognome()+" "+TecI2.getnome(), " aggiunto al progetto: ")    
    Progetto1.aggiungiPersona(dirig1);
    print(dirig1.getcognome()+" "+dirig1.getnome(), " aggiunto al progetto: ")     
    Progetto1.aggiungiPersona(FunzS1);
    print(FunzS1.getcognome()+" "+FunzS1.getnome(), " aggiunto al progetto: ")     
    Progetto1.aggiungiPersona(FunzJ1);
    print(FunzJ1.getcognome()+" "+FunzJ1.getnome(), " aggiunto al progetto: ")     
    print("Elenco partecipanti al progetto completato!!\n")
    print("Costi del progetto anno: ",ANNO)    
        #// stampa elenco partecipanti progetto
    print("Elenco partecipanti Progetto: \n"+Progetto1.elencoPersone()+"Totali Persone: ",Progetto1.getTotalePersone())
        # calcolo costi complessivi progetto
    print("costi totali progetto:  ",Progetto1.Costiprogetto(ANNO));
        #// cerco una persona che partecipa al progetto
    pers="Verd"
    print("\ncerco se esiste la persona <"+pers+"> nei partecipanti al prgetto")
    trovato,pers = Progetto1.cercaPersona(pers);
    if trovato==True : 
        print("Persona trovata: "+pers.getcognome())
    else:
        print("Persona non trovata");
      
        #// stampa elenco partecipanti progetto
    print("\nElenco partecipanti Progetto: \n"+Progetto1.elencoPersone()+"Totali Persone: ",Progetto1.getTotalePersone())
    print("costi totali progetto:  ",Progetto1.Costiprogetto(ANNO));
           
    # eliminazione di una Persona dal progetto e stampa nuova lista elenco membri progetto
    cognome ="Rossi"
    print("\nCancellazione della persona : "+cognome+"  dal progetto")
    trovato=Progetto1.eliminaPersona(cognome)
    if trovato==True : 
        print("Persona Eliminata: "+cognome);
    else: 
        print("Persona non trovata")            
    print("nuova lista Elenco membri del progetto:")
    print("\nElenco partecipanti Progetto: \n"+Progetto1.elencoPersone()+"Totali Persone: ",Progetto1.getTotalePersone())
    
    # calcolo nuovi costi complessivi progetto
    print("Nuovi costi totali progetto:  ",Progetto1.Costiprogetto(ANNO))        
    #print(Progetto1)
    
    '''  **************************** realizzazione esercizio confronto di progetti
        1) Creazione progetto
        2) Confronto di due progetti
        3) Stampa progetti in ordine di costo totale
    '''
    #creo un elenco pe conservare i progetti; mi serve per stampare i progetti in rdine di costo totale
    elenco=[]
    #creo il primo progetto 
    ProgettoSoftware=GestioneProgetti()
    #print("Creo persone partecipanti al progetto: ")
    dirig1=Dirigente("Mario","Bianchi","123",2010,200)
    FunzS1=FunzionarioSenior("Paolo","Rossi","221",2012, 100)
    FunzJ1=FunzionarioJunior("Marco","Verde","222", 2013, 92)
    TecI2=TecnicoInfTel("Davide","corti","301",2010,35,False)        
    TecE1=TecnicoEleAut("Giorgio","Marek","401",2008,28,True)
    #aggiungo persone al progetto
    ProgettoSoftware.aggiungiPersona(TecE1)
    ProgettoSoftware.aggiungiPersona(TecI2)
    ProgettoSoftware.aggiungiPersona(dirig1)  
    ProgettoSoftware.aggiungiPersona(FunzS1) 
    ProgettoSoftware.aggiungiPersona(FunzJ1)
    #creo il secondo progetto 
    ProgettoSviluppo=GestioneProgetti()
    #aggiungo le stesse persone al secondo progetto
    ProgettoSviluppo.aggiungiPersona(TecE1)
    ProgettoSviluppo.aggiungiPersona(TecI2)
    ProgettoSviluppo.aggiungiPersona(dirig1)  
    ProgettoSviluppo.aggiungiPersona(FunzS1) 
    ProgettoSviluppo.aggiungiPersona(FunzJ1)
    #confronto i due progetti ; se sono le stesse persone con gli stessi costi dovrebbe risultare che sono uguali
    if ProgettoSoftware == ProgettoSviluppo:
        print("\nProgetti ProgettoSoftware e ProgettoSviluppo sono uguali")
    else:
        print("\nProgetti ProgettoSoftware e ProgettoSviluppo sono diversi")
    #elimino dal secondo progetto "Mario Bianchi"
    trovato=ProgettoSviluppo.eliminaPersona("Bianchi")
    if trovato==True : 
        print("Persona Eliminata: ")
    else: 
        print("Persona non trovata")            
    #confronto di nuovo i progetti; in questo caso dovrebbero risultare diversi perchè il secondo progetto ha una pesona in meno
    if ProgettoSoftware == ProgettoSviluppo:
        print("\nProgetti ProgettoSoftware e ProgettoSviluppo sono uguali")
    else:
        print("\nProgetti ProgettoSoftware e ProgettoSviluppo sono diversi")
    elenco.append(ProgettoSoftware)
    elenco.append(ProgettoSviluppo)
    #eordino elenco in odine di costo totale  progetto usando una lambda che valuta il costo totale del progetto con il metodo Costiprogetto()
    elenco.sort(key=lambda x: x.Costiprogetto(2023),reverse =True) #ordine decrescente
    #stampo costi progetto per verificare se funzione
    for i,progetto in enumerate(elenco):
        print("costo progetto "+str(i+1)+": ",progetto.Costiprogetto(2023))

Main()
