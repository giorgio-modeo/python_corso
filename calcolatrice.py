#___________________________________________________________________Giorgio Modeo
import os
risP = ""
risR = ""
def potenza():
    numeri.append(float(input("Inserire la potenza: ")))
    risP = pow(numeri[0],numeri[2])
    print(ris,risP)
def radice():
    numeri.append(float(input("Inserire la radice: ")))
    risR = pow(numeri[0],numeri[2])
    print(ris,risR)
def result():
    print(ris,risultato)
    
menu ="""
***********************
    Gli operatori sono:
    +. addizzione
    -. sottrazzione
    *. moltiplicazzione
    /. divisione
    ^. potenza
    r. radice
***********************
"""
risultato = ""
ris = "Il risultato e: "
while True:
    os.system("cls")
    print(menu)
    numeri=[]
    x = 0
    for x in range(0,3):
        if x == 1:
            numeri.append(input("Inserire l'operatore: "))
            if numeri[1] == "^":
                potenza()
                break
            elif numeri[1] == "r":
                radice()
                break
        else:
            numeri.append(float(input("Inserire i numeri con cui vuoi fare le operazzioni: ")))
    match numeri[1]:
        case"+":
            risultato = numeri[0] + numeri[2]
            result()
        case"-":
            risultato = numeri[0] - numeri[2]
            result()
        case"*":
            risultato = numeri[0] * numeri[2]
            result()
        case"/":
            risultato = numeri[0] / numeri[2]
            result()

    if (risultato == "") and ((risP == "")or(risR == "")):
        print("\nHai fatto un errore riprova")
    input("\nPremi invio per continuare... ")
    

