#generatore di psw
import random
cicle = 0
menu= """
>>GENERATORE DI PSW<<
 
Scegli uno dei seguenti input: 1, 2 o 3:
  1. Caratteri alfabetici maiuscoli e minuscoli
  2. Caratteri alfanumerici maiuscoli e minuscoli
  3. Caratteri alfanumerici maiuscoli e minuscoli piu caratteri speciali
 
"""
 
ch1 = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
ch2 = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                 '0123456789')
ch3 = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                 '!£$%#&=?0123456789')
#inserisci quante psw vuoi inserire
nP=int(input("Quante password vuoi generare?Fai attenzione hai a disposizione un range che va da 1 a 50:  "))

if (nP <= 50 and nP >= 1):
    #scegli la lunghezza delle psw
    lP=int(input("Quanto vuoi che siano lunghe le password generate? Fai attenzione hai a disposizione un range che va da 10 a 20: "))
    if (lP >=10 and lP <=20):
        #scegli la tipologia di psw
        print(menu)
        tipo=input("Inserisci il tipo di password da creare: ")
        match tipo:
            case "1":
                while cicle<=nP:
                    password = ''
                    for i in range(lP):
                        password += random.choice(ch1)
                    print("La tua password criptata è: ", password )
                    cicle=cicle+1
            case "2":
                while cicle<=nP:
                    password = ''
                    for i in range(lP):
                        password += random.choice(ch2)
                    print("La tua password criptata è: ", password )
                    cicle=cicle+1
            case "3":
                while cicle<=nP:
                    password = ''
                    for i in range(lP):
                        password += random.choice(ch3)
                    print("La tua password criptata è: ", password )
                    cicle=cicle+1
   
            case _:
              print("Type Error...")
 
    else:
        print("Assicurati di inserire una lunghezza delle password pari a 10 o superiore ed inferiore alle 20")
else:
    print("Assicurati di inserire un numero di password che vada da 1 a 50.")
       
   

