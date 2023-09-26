class GestioneVeicoli:
    def __init__(self):
        self.__elenco = []
    
    def aggiungiVeicolo(self, veicoli):
        self.__elenco.append(veicoli)
        return True
    
    def cancellaVeicolo(self, targa):
        for veicolo in self.__elenco:
            if veicolo.getTarga() == targa:
                self.__elenco.remove(veicolo)
                return True

    def cercaVeicolo(self, targa):
        for veicolo in self.__elenco:
            if veicolo.getTarga() == targa:
                print(veicolo)
                return True
        return False
    
    def ordinaVeicoli(self):
        self.__elenco.sort(key=lambda veicolo: veicolo.getTarga())
        return self.__elenco
    
    def stampaVeicolo(self):
        for veicolo in self.__elenco:
            print(veicolo,"\n")
    
    def totaleVeicoli(self):
        totale = len(self.__elenco)
        print(f"Il totale dei veicoli è: {totale}")
    
    def costoTotale(self):
        costo = 0
        for veicolo in self.__elenco:
            costo += veicolo.getCosto()
        print(f"Il costo totale è: {costo}")