#Giorgio Bruno Modeo

gest_scon = """
            ********************************
            *       GESTIONE SCONTRINO     *
            ********************************

            ********************************
            *   MENÙ UTENTE PRINCIPALE     *
            ********************************
            *   1 INSERIMENTO ARTICOLO     *
            *   2 APPLICA LO SCONTO        *
            *   3 STAMPA LO SCONTRINO      *
            *   4 ======> USCITA           *
            ********************************

"""

articolo = {}
inp = []
a = True
def main():
    while a:
        del inp[:]
        menu()


def menu():
        scelta = int(input(f"{gest_scon}\ninserire la scelta: "))
        match scelta:
            case 1:
                print("INSERIMENTO ARTICOLO")
                c_input()
            case 2:
                print("APPLICA LO SCONTO")
                sconto()
            case 3: 
                print("STAMPA LO SCONTRINO")
                scontrino()
            case _:
                print("exit")
                global a
                a = False
def c_input():
    while True:
        try:
            inp.append(str(input("inserisci il nome dell articolo: ")))
            inp.append(float(input("inserisci il prezzo: ")))
            inp.append(int(input("inserisci la quantità: ")))
            print(f"articolo inserito correttamente \n  nome {inp[0]} prezzo {inp[1]} quantità {inp[2]}")
            break
        except:
            print("dato sbagliato riprova!")
    articolo.update([(inp[0],[inp[1],inp[2],(inp[1] * inp[2])])])

def sconto():
    global b
    b = True
    if 50 <= articolo[inp[0]][2]:
        articolo.update([(f'{inp[0]}_scontato',[(articolo[inp[0]][2] - ((articolo[inp[0]][2]*2)/100))] )])
        print(f"\nsconto applicato 2%\n({articolo[inp[0]][2]} * 2)/100 \nprezzo scontato: {articolo[f'{inp[0]}_scontato'][0]}€")

        if 5 < articolo[inp[0]][1]:
            articolo[f'{inp[0]}_scontato'] += [round((articolo[f'{inp[0]}_scontato'][0] - ((articolo[f'{inp[0]}_scontato'][0]*7)/100)),2)]
            print(f"\nulteriore sconto applicato 7%\n({articolo[f'{inp[0]}_scontato'][0]} * 7) /100 \nnuovo totale: {articolo[f'{inp[0]}_scontato'][1]}€")

def scontrino():
        print("articolo:    prezzo:     QUANTITÀ:")
        for key in articolo:
            print(f"{key}           {articolo[key][0]}           {articolo[key][1]}   ")
        print(articolo)
main()
