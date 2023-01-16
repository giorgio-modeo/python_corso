import os,datetime,time
#                                                                                   + main
def main():
    squadra,allenatore = {},{}
    os.system("cls")
    switch(squadra,allenatore)


#                                                                                   + menu
def menu():
    m = """
        +----------------------------------------------------------------------------------+
        |                                  MENÙ                                            |
        +----------------------------------------------------------------------------------+
        | 1. Inserimento dati delle squadre                                                |
        | 2. Stampare la classifica delle squadre in ordine decrescente di punteggio       |
        | 3. Modificare i punti di una squadra con input da tastiera                       |
        | 4. Stampare classifica titoli degli allenatori in ordine decrescente di titoli   |
        | 5. Numero totale di allenatori che hanno vinto Y titoli                          |
        | 6. Stampa squadre con più di Y punti in classifica                               |
        | 7. Stampare squadre con allenatori che hanno vinto più di Y titoli               |
        |                                                                                  |
        |                                                                                  |
        | 8. ==>  uscita                                                                   |
        |                                                                                  |
        +----------------------------------------------------------------------------------+
        """
    print(m)
#                                                                                   + switch
def switch(squadra,allenatore):
    a,k = True,False
    while a:
        menu()
        selezzione = inp_int("inserisci scelta: ")
        match selezzione:
            case 1:
                os.system("cls")
                print("Inserimento dati delle squadre")
                ins_in_squadra(squadra,allenatore)
                k =True
                input("premi per continuare...")
            case 2:
                os.system("cls")
                print("Stampare la classifica delle squadre in ordine decrescente di punteggio")
                if k== True:
                    clas_ord_decre(squadra)
                else:
                    print("inserisci prina una squadra")
                input("premi per continuare...")
            case 3:
                os.system("cls")
                print("Modificare i punti di una squadra con input da tastiera")
                if k== True:
                    mod_punti(squadra)
                else:
                    print("inserisci prina una squadra")
                input("premi per continuare...")
            case 4:
                os.system("cls")
                print("Stampare classifica titoli degli allenatori in ordine decrescente di titoli")
                if k== True:
                    ord_titoli(allenatore,squadra)
                else:
                    print("inserisci prina una squadra")
                input("premi per continuare...")
            case 5:
                os.system("cls")
                print("Numero totale di allenatori che hanno vinto Y titoli")
                if k== True:
                    vin_titoli(allenatore)
                else:
                    print("inserisci prina una squadra")
                input("premi per continuare...")
            case 6:
                os.system("cls")
                print("Stampa squadre con più di Y punti in classifica")
                if k== True:
                    y_punti(squadra)
                else:
                    print("inserisci prina una squadra")
                input("premi per continuare...")
            case 7:
                os.system("cls")
                print("Stampare squadre con allenatori che hanno vinto più di Y titoli")
                if k== True:
                    y_titoli_squadra(allenatore,squadra)
                else:
                    print("inserisci prina una squadra")
                input("premi per continuare...")
            case _:
                a = False
                print("arrivederci")
                time.sleep(3)
        os.system("cls")

#                                                                                   + inserimento in squadra e allenatore
def ins_in_squadra(squadra,allenatore):
    nome, colore_maglia, punteggio =inp_str("nome della squadra: "),inp_str("clore della maglia: "),inp_int("punteggio: ")
    nome_allenatore, co_n_all, titolivinti = inp_str("nome dell allenatore: "),inp_str("cognome dell allenatore: "),inp_int("numero titoli vinti dal allenatore: ")
    squadra.update({nome: [colore_maglia,punteggio,nome_allenatore]})
    allenatore.update({nome_allenatore: [co_n_all,titolivinti]})
    print("inserimento completato correttamente")



#                                                                                   + classifica per punteggio ordine decrescente
def clas_ord_decre(squadra):
    a= dict(sorted(squadra.items(),key=lambda x: x[1][1],reverse=True))
    print(f'-----Stampa classifica-----{"SQUADRA":15}{"PUNTI":10}{"COLORE MAGLIA":20}')
    for key in a:
        print(f"{key:>25}{a[key][1]:>15}{a[key][0]:>10}")
#key :[val1,val2]

#                                                                                   + modifica il punteggio
def mod_punti(squadra):
    sq= inp_str("inserisci la il nome della squadra con il punteggio da modificare: ")
    if sq in squadra:
        v_pun = squadra[sq][1]
        n_pun =inp_int("inserisci il nuovo punteggio: ")
        squadra[sq][1] = n_pun
        print(f"il punteggio della squadra {sq} e stato cambiato da {v_pun} a {n_pun}")
    else:
        print("la squadra non esiste")

#                                                                                   + ordina in base hai titoli vinti dall allenatore
def ord_titoli(allenatore,squadra):

    a= dict(sorted(allenatore.items(),key=lambda x: x[1][1],reverse=True))
    print(f'{"ALLENATORE COGNOME":<20} {"NOME":10} {"TITOLI VINTI":15} {"SQUADRA":<12}')
    for k in a:
        for key in squadra:
            if squadra[key][2] == k:
                print(f'{a[k][0]:<20} {k:<10} {a[k][1]:<15} {key:<12}')

#                                                                                   + numero di allenatori cheha vinto n titoli
def vin_titoli(allenatore):
    b=0
    a = inp_int("numero di titoli vinti dal allenatore: ")
    for key in allenatore:
        if a == allenatore[key][1]:
            b+=1
    print(f"gli allenatori che hanno vinto {a} in totale sono {b}")

#                                                                                   + squadra che ha n punti 
def y_punti(squadra):
    a = inp_int("inserisci quanti punti per la squadra: ")
    print(f'{"squadra":<10}{"punti":<15}')
    for key in squadra:
        if a == squadra[key][1]:
            print(f"{key:<10}{squadra[key][1]:<15}")

#                                                                                   + squadra che ha l'allenatore con n titoli vinti
def y_titoli_squadra(allenatore,squadra):
    a = inp_int("numero di titoli vinti dal allenatore: ")
    print(f'{"squadra":<20} {"allenatore":10} {"TITOLI VINTI":15}')
    for key in squadra:
        for k in allenatore:
            if (squadra[key][2] == k) and (allenatore[k][1] == a):
                print(f'{key:<20} {allenatore[k][0]:<10} {allenatore[k][1]:<15} ')

#                                                                                   + input interi
#                                                                                      questa funzione controlla che l'input passato sia un numero intero
def inp_int(strin):
    while True:
        try:
            i = int(input(strin))
            break
        except:
            print("input errato")
    return i

#                                                                                   + input float
#                                                                                      questa funzione controlla che l'input passato sia un numero con o senza virgola
def inp_flt(strin):
    while True:
        try:
            f = float(input(strin))
            break
        except:
            print("input errato")
    return f

def inp_str(strin):
    s = str(input(strin))
    return s

main()