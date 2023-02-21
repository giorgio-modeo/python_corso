from dipendente import dipendente
class docente(dipendente):
    def __init__(self,nome,indirizzo,sesso,disciplina,ruolo):
        super().__init__(nome,indirizzo,sesso)
        self._disciplina=disciplina
        self._ruolo=ruolo
    
    def getDisciplina(self):
        return self._disciplina
    def getRuolo(self):
        return self._ruolo

    def setDisciplina(self,disciplina):   
        self._disciplina = disciplina
    def setRuolo(self,ruolo):   
        self._ruolo = ruolo

    def __str__(self):
        return super().__str__() +" Disciplina: "+self._disciplina+" Ruolo: "+self._ruolo        
