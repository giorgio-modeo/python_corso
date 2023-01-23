nomi =set()
nomi= {"luigi","mario","davide"}
nomi.add("giovanni")

print(nomi)
#se l'elemento non esiste non fa nulla 
nomi.discard("renato")

#se l'elemento non esiste ritorna errore
if "renato" in nomi:
    nomi.remove("renato")
else:
    print("non esiste")
print(nomi)

alunni = {"mario", "luigi"}
#se nomi contiene alunni 
print(alunni.issubset(nomi))

#se nomi e contenuto in alunni 
print(nomi.issuperset(alunni))

# unione dei due set()
persona=nomi.union(alunni)
print(persona)

persone=nomi.intersection(alunni)
print("intersezzione = ", persone)
persone=nomi.difference(alunni)
print("differenza =", persone)
nomi.clear()
numeri =set(range(10))
print(numeri)
