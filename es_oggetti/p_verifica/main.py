from immobile import Immobile
from abitazione import Abitazione

# immobile=Immobile(input("tipo del immobile: "),input("metri quadrati: "),input("anno di costruzzione: "),input("avente giardino (0=no 1=si)"))
immobile=Abitazione("si","cia","to","ciao",200,2000,1)
Immobile.-immobile.prezzo()

print(immobile)
