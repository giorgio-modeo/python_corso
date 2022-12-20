"""
scrivere una funzione che si comporta come il metodo 
    split()
-accettare una stringa e restituire un elenco di parole create dalla stringa dagli spazi
"""
def str_to_split(stringa):
    lista=[]
    if stringa=="" or stringa.isspace():
        return lista
    word=''
    inword=not stringa[0].isspace()
    for x in stringa:
        if inword:
            if not x.isspace():
                word=word+x
            else:
                lista.append(word)
                inword=False
        else:
            if not x.isspace():
                inword=True
    if inword:
        lista.append(word)
    return lista

def main():
    

        
stringa = str(input("inserisci la parola o frase"))