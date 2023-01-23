stream = open("esercizzi_file/test.txt", mode="w", encoding="utf-8")
stream.write ("ciao Mondo\n")
stream.close ()
stream1 = open("esercizzi_file/test.txt", mode="r")
#print(stream1.read(1))
stream1.close ()

from platform import *
print("sistema utilizzato: ",platform())
print("Pc tipo: ",machine())
print("processore: ",processor())
print("sistema: ",system(),"\t\tversione w : ",version())
print("versione python: ",python_implementation(),python_version_tuple())
import os 
cartella=os.getcwd()
print(cartella)
for nome in os.listdir():
    print(nome)

try:
    os.mkdir("esercizzi_file/cartella_creata_con_py")
    #os.rmdir("esercizzi_file/cartella_creata_con_py")
except:
    print("la cartella esiste gia!")