class CDMusicale():
    def __init__(self,nome,artista):
        self.__nome=nome
        self.__artista=artista
        self.__brani=[]
        self.__prezzo=0

    def getNome(self):
        return self.__nome
    def getArtista(self):
        return self.__artista
    def getBrani(self):
        return self.__brani
    def getPrezzo(self):
        return self.__prezzo

    def setNome(self,nome):
        self.__nome=nome
    def setArtista(self,artista):
        self.__artista=artista
    def setBrani(self,brani):
        self.__brani=brani
    def setPrezzo(self,prezzo):
        self.__prezzo=prezzo
    
    def __str__(self):
    #                                                                                       "\" per continuare a scrivere nello stesso comando in una nuova riga
        st = "Nome: "+self.__nome+" Artista: "+self.__artista+" brani: "+str(self.__brani)\
            + " prezzo: "+str(self.__prezzo)
        return st

def main():
    cd=[]
    while True:
        brani=[]
        nome= str(input("inserisci il nome dell' cd musicale"))
        artista= str(input("inserisci il nome dell' artista"))
        nBrani=inp_int("inserisci il numero di brani presenti nel cd: ")
        for i in range(nBrani):
            brani.append(str(input("inserisci il nome della canzone")))
        prezzo= inp_int("inserisci il prezzo")
        cdn=CDMusicale(nome,artista)
        cdn.setBrani(brani)
        cdn.setPrezzo(prezzo)
        cd.append(cdn)
        print(cd)
    

def inp_int(st):
    while True:
        try:
            n=int(input(st))
            break
        except:
            print("input errato!")
    return n
main()