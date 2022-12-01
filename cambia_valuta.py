valuta = str(input("inserisci la tua valuta l lire e euro d dollari: "))
quantita = float(input("inserisci la quantita: "))
if valuta == "e":
    lire = quantita * 1936.27
    dollari = quantita * 1.033
    print("euro in lire: ",lire,"£ \n","euro in dollari: ", dollari,"$")

elif valuta == "l":
    euro = quantita / 1936.27
    dollari = quantita /1936.30
    print("lire in euro: ",euro,"€ \n","lire in dollari: ", dollari,"$")
    
elif valuta == "d":
    euro = quantita / 1.033
    lire = quantita * 1936.30
    print("dollari in lire: ",lire,"£ \n","dollari in euro: ", euro,"€")
