class dipendente:
    def __init__(self,nome,indirizzo,sesso):
        self._nome=nome
        self._indirizzo=indirizzo
        self._sesso=sesso
    
    def getNome(self):
        return self._nome
    def getIndirizzo(self):
        return self._indirizzo
    def getSesso(self):
        return self._sesso
    
    def setNome(self,nome):
        self._nome=nome
    def setIndirizzo(self,indirizzo):
        self._indirizzo=indirizzo
    def setSesso(self,sesso):
        self._sesso=sesso
    
    def __str__(self):
        return "Nome: "+self._nome+" Indirizzo: "+self._indirizzo+" Sesso: "+self._sesso
    
    

