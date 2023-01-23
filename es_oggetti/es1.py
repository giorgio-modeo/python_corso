class atleta:
#   funzione costruttore (inizzializza l'oggetto con questi parametri)
    def __init__(self,nome,cognome,altezza):
#       self.__nome     (attributo privato)
#       self.nome       (attributo pubblico)
        self.__nome= nome
        self.__cognome= cognome
        self.__altezza=altezza
        self.__squadra=""
        self.__visitamedica=False

    def getNome(self):
        return self.__nome
    def getCognome(self):
        return self.__cognome
    def getAltezza(self):
        return self.__altezza
    def getSquadra(self):
        return self.__squadra
    def getVisitaedica(self):
        return self.__visitamedica

    def setNome(self,nome):
        self.__nome=nome
    def setCognome(self,cognome):
        self.__cognome=cognome
    def setAltezza(self,altezza):
        self.__altezza=altezza
    def setSquadra(self,squadra):
        self.__squadra=squadra
    def setVisitamedica(self,visitamedica):
        self.__visitamedica=visitamedica

#metoto privato che viene richiamato automatico con il print e da le informazzioni del oggetto 
    def __str__(self):
#                                                                                       "\" per continuare a scrivere nello stesso comando in una nuova riga
        st = "Nome: "+self.__nome+" Cognome: "+self.__cognome+" sqadra: "+self.__squadra\
            + " altezza: "+str(self.__altezza)+" visita medica: " +str(self.__visitamedica)
        return st
def main():
#   utilizzo con attributi pubblici 
#   Delpiero =atleta("alessandro","delpiero")
#   print(Delpiero.nome)

#   utilizzo con attributi privati
#     totti=atleta("francesco","totti",170,"roma",True)
#     print(totti.getNome(),totti.getCognome())
#   per stampare tutto utilizziamo __str__
#     print(totti)
    nome = str(input("inserisci nome"))  
    cognome = str(input("inserisci cognome"))  
    altezza = inpnumero("inserisci altezza")  
    squadra = str(input("inserisci squadra"))
    a1=atleta(nome,cognome,altezza)
    a1.setSquadra(squadra)
    a1.setVisitamedica(True)
    print(a1)

def inpnumero(stringa):
    while True:
        try:
            n = int(input(stringa))
            break
        except:
            print("input errato!")
    return n
main()