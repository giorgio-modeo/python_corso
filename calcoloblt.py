#calcolo dell'anno bisesto
print("L'output riferirsce all'utente se l'anno inserito in input è bisestile o no")
anno = input("Inserisci anno da verificre: ")
if anno.isdigit():
    anno1=int(anno)
    if anno1%4 == 0 and anno1%100 != 0 or anno1%400 == 0:
        print("Sì, l'anno è bisestile")
    else:
        print("No, l'anno non è bisestile")

else: 
    print(">Assicurati di inserire solo cifre numeriche\n--Hai inserito: ", anno )