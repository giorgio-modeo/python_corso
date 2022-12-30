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
#                                                                                   definisco i dizzionari vuoti che poi verranno riempiti dal utente
#                                                                                   definisco una lista in modo da 
articolo,articolo_s = {},{}
inp = []
a,b = True,0
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
    global b
    while True:
        try:
            inp.append(str(input("inserisci il nome dell articolo: ")))
            inp.append(float(input("inserisci il prezzo: ")))
            inp.append(int(input("inserisci la quantità: ")))
            print(f"articolo inserito correttamente \n  nome {inp[0]} prezzo {inp[1]} quantità {inp[2]}")
            b = 1
            break
        except:
            print("dato sbagliato riprova!")
            del inp[:]
    articolo.update([(inp[0],[inp[1],inp[2],(inp[1] * inp[2])])])
    input("premere invio per continuare...")
    
def sconto():
    if b == 1:
        for key in articolo:
            if 50 <= articolo[key][2]:
                articolo_s.update([(f'{key}_scontato',[(articolo[key][2] - ((articolo[key][2]*2)/100))] )])
                print(f"\nsconto applicato 2%\n({articolo[key][2]} * 2)/100 \nprezzo scontato: {articolo_s[f'{key}_scontato'][0]}€")

                if 5 < articolo[key][1]:
                    articolo_s[f'{key}_scontato'] += [round((articolo_s[f'{key}_scontato'][0] - ((articolo_s[f'{key}_scontato'][0]*7)/100)),2)]
                    print(f"ulteriore sconto applicato 7%\n({articolo_s[f'{key}_scontato'][0]} * 7) /100 \nnuovo totale: {articolo_s[f'{key}_scontato'][1]}€\n")
            else:
                print(f"{key}: non ha sconti applicabili\n")
    else:    
        print("nessun articolo inserito!! Inserire prima l'articolo")
        c_input()
    input("premere invio per continuare...")
    
def scontrino():
    if b == 1:
        print("ARTICOLO:    PREZZO:     QUANTITÀ:     PREZZO SCONTATO")
        for key in articolo:
            try:
                print(f"{key}           {articolo[key][0]}           {articolo[key][1]}           {articolo_s[f'{key}_scontato'][1]}")
            except:
                print(f"{key}           {articolo[key][0]}           {articolo[key][1]}           {articolo[key][2]}")
    else:    
        print("nessun articolo inserito!! Inserire prima l'articolo")
        c_input()
        
    input("premere invio per continuare...")
main()
