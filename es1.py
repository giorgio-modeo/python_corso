import os,datetime
#                                                                                   + main
def main():
    scontrino,scontrino_s = {},{}
    a = True
    while a:
        os.system("cls")
        menu()
        a = switch(scontrino,scontrino_s)
#                                                                                   + menu
def menu():
    m = """
        +---------------------------------------------------------------------+
        |                                  MENÙ                               |
        +---------------------------------------------------------------------+
        | 1. Inserimento articolo                                             |
        | 2. Totale Articoli venduti                                          |
        | 3. Totale degli sconti effettuati                                   |
        | 4. Stampa scontrino senza sconto                                    |
        | 5. Stampa scontrino con lo sconto                                   |
        | 6. Stampa scontrino con sconto ordinato per prezzo o per quantità   |
        |                                                                     |
        |                                                                     |
        | 7. ==>  uscita                                                      |
        |                                                                     |
        +---------------------------------------------------------------------+
        """
    print(m)
#                                                                                   + switch
def switch(scontrino,scontrino_s):
    a = True
    selezzione = inp_int("inserisci scelta: ")
    match selezzione:
        case 1:
            ins_in_scontrino(scontrino)
            input("premi per continuare...")
        case 2:
            
            tot_art(scontrino)
            input("premi per continuare...")

        case 3:
            
            tot_sconti(scontrino,scontrino_s)
            input("premi per continuare...")
        case 4:
            ss_scontrino(scontrino)
            input("premi per continuare...")
        case 5:
            s_scontrino(scontrino_s,scontrino)
            input("premi per continuare...")
        case 6:
            scontrino_ord(scontrino,scontrino_s)
            input("premi per continuare...")
        case _:
            a = False
    return a
#                                                                                   + inserimento nel scontrinozionario
def ins_in_scontrino(scontrino):
    nome,prezzo,quantita =inp_str("nome articolo: "), inp_flt("inserisci il prezzo: "), inp_int("inserisci la quantità: ")
    scontrino.update({nome: [prezzo,quantita,(prezzo*quantita)]})
    print(scontrino)

def tot_art(scontrino):
    n_art=0
    for key in scontrino:
        n_art = n_art + scontrino[key][1]
    print("il totale degli articoli e: ",n_art)

def tot_sconti(scontrino,scontrino_s):
    print(f"lo sconto e di: {sconto(scontrino,scontrino_s)}€")


def sconto(scontrino,scontrino_s):
    t_sco,s1,s2 = 0,0,0
    for key in scontrino:
        list = scontrino[key]
        if (list[2] >= 50):
            s1 = (list[2]*0.1)
            scontrino_s.update({key: [(list[2] - s1), list[1]]})
        else:
            scontrino_s.update({key: [list[2], list[1]]})

        if list[1] > 5:
            s2 = (scontrino_s[key][0]*0.05)
            scontrino_s.update({key: [(scontrino_s[key][0] - s2), list[1]]})
        t_sco =t_sco+(s1 + s2)
        scontrino_s[key].append(t_sco)
    return t_sco

def ss_scontrino(scontrino):
    data_ora =datetime.datetime.now().strftime("%d/%m/%Y %H:%M%S")
    print(f'scontrino:\ndata: {data_ora}\n{"articolo":>10}{"prezzo":>10}{"quantita":>10}{"totale":>20}\n')
    for key in scontrino:
        list=scontrino[key]
        print(f'{key:>10}{list[0]:>10}{list[1]:>10}{list[2]:>20}')


def s_scontrino(scontrino_s,scontrino):
    data_ora =datetime.datetime.now().strftime("%d/%m/%Y %H:%M%S")
    while True:
        try:
            sconto(scontrino,scontrino_s)
            break
        except:
            ins_in_scontrino(scontrino)
    print(f'scontrino:\ndata: {data_ora}\n{"articolo":>10}{"prezzo":>10}{"quantita":>10}{"totale":>20}{"sconto":>10}\n')
    for key in scontrino:
        list=scontrino[key]
        print(f'{key:>10}{list[0]:>10}{list[1]:>10}{list[2]:>20}{scontrino_s[key][2]:10}')


def scontrino_ord(scontrino,scontrino_s):
    s = inp_int('per cosa vuoi ordinare 1 = "prezzo" o 2 = "quantita": ')
    a= dict(sorted(scontrino.items(),key=lambda x: x[1][s-1]))
    s_scontrino(scontrino_s,scontrino)




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

#                                                                                   + input interi
#                                                                                      questa funzione controlla che l'input passato sia un numero 
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