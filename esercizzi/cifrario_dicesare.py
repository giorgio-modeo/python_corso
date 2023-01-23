text=input("inserisci testo: ")
n=int(input("inserisci numero: "))
crypto = ""
st=""
for ch in text:
    codice=ord(ch)+n
    st=st+chr(codice)

print("frase cyptografata: ", st)
st1=""
for ch in st:
    codice=ord(ch)-n
    st1=st1+chr(codice)

print("frase decyptografata: ", st1)