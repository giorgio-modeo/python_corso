#Giorgio Bruno Modeo
import os
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
articolo,articolo_s = {},{}
#                                                                                   definisco una lista in modo da poter chiedere piu articoli 
inp = []
a,b = True,0
#                                                                                   + main
def main():
#                                                                                      faccio un ciclo in modo che l'applicazzione possa essere ripetuta
#                                                                                      cancello la vecchia interfaccia grafica e la vecchia lista in modo da non dover
#                                                                                      chiudere l'app per inserire più dati 
    while a:
        os.system("cls")
        del inp[:]
        menu()

#                                                                                   + menu
def menu():
#                                                                                      faccio sciegliere al utente l'azzione da fare
    scelta = int(input(f"{gest_scon}\ninserire la scelta: "))
    match scelta:
#                                                                                         prima scelta inserimento degli articoli
        case 1:
            print("INSERIMENTO ARTICOLO")
            c_input()
#                                                                                         seconda scelta sconto degli articoli possibili
        case 2:
            print("APPLICA LO SCONTO")
            sconto()
#                                                                                         terza  scelta stampa dello scontrino
        case 3: 
            print("STAMPA LO SCONTRINO")
            scontrino()
#                                                                                         default uscita
        case _:
            print("exit")
            global a
            a = False
#                                                                                   + input degli articoli
def c_input():
#   definisco questa variabile {b} globale in modo che una volta modificata in questa funzione venga mantenuta in tutto il codice
    global b
#                                                                                      creo un ciclo in modo da permettere al utente di sbagliare e riprovare l'inserimento
    while True:
#                                                                                         provo a far inserire i dati al utente se sbaglia il comando try: 
#                                                                                         non fara restituire l'errore 
        try:
#                                                                                            chiedo al utente i dati
            inp.append(str(input("inserisci il nome dell articolo: ")))
            inp.append(float(input("inserisci il prezzo: ")))
            inp.append(int(input("inserisci la quantità: ")))
#                                                                                            stampo i dati inseriti in modo che l'utente possa verificare la correttezza di essi
            print(f"articolo inserito correttamente \n  nome {inp[0]} prezzo {inp[1]} quantità {inp[2]}")
            b = 1
            break
#                                                                                         al posto dell errore cancella i dati e ti fa riprovare l'inserimento del dato 
        except:
            print("dato sbagliato riprova!")
            del inp[:]
#                                                                                      una volta che finito tutto salvo gli input nel dizzionari
    articolo.update([(inp[0],[inp[1],inp[2],(inp[1] * inp[2])])])
    input("premere invio per continuare...")
    
#                                                                                   + sconto
def sconto():
#                                                                                      verifico che sia stato inserito almeno un dato
    if b == 1:
#                                                                                         eseguo un controllo per verificare quali articoli hanno uno sconto 
#                                                                                         per ogni chiave nel dizzionario 
        for key in articolo:
#                                                                                            sconto per il prezzo
            if 50 <= articolo[key][2]:
                s2 = ((articolo[key][2]*2)/100)
                articolo_s.update([(f'{key}_scontato',[(articolo[key][2] - s2 )] )])
                print(f"\nsconto applicato 2%\n({articolo[key][2]} * 2)/100 \nprezzo scontato: {articolo_s[f'{key}_scontato'][0]}€")
#                                                                                               salvo i soldi scontati
                articolo_s[f'{key}_scontato'] += [round(s2,2)]

#                                                                                               sconto per la quantità
                if 5 < articolo[key][1]:
                    s7 = ((articolo_s[f'{key}_scontato'][0]*7)/100)
                    articolo_s[f'{key}_scontato'] += [round((articolo_s[f'{key}_scontato'][0] - s7),2)]
#                                                                                                  modifico i soldi scontati in modo da non avere dati inutili
                    articolo_s[f'{key}_scontato'][1] = [round((s2 + s7),2)]
                    print(f"ulteriore sconto applicato 7%\n({articolo_s[f'{key}_scontato'][0]} * 7) /100 \nnuovo totale: {articolo_s[f'{key}_scontato'][0]}€\n")
#                                                                                            se l'articolo non puo essere scontato          
            else:
                print(f"\n{key}: non ha sconti applicabili\n")
#                                                                                      se non sono stati inseriti dati ne forzo l'inserimento
    else:    
        print("nessun articolo inserito!! Inserire prima l'articolo")
        c_input()
    input("premere invio per continuare...")
#                                                                                   + scontrino
def scontrino():
#                                                                                      verifico che sia stato inserito almeno un dato
    if b == 1:
        print("ARTICOLO    PREZZO     QUANTITÀ     SCONTO APPLICATO     TOTALE SCONTATO")
        for key in articolo:
            try:
                try:
#                                                                                               se l'articolo ha sia lo sconto del 2% che da 7%
                    print(f"{key}           {articolo[key][0]}€           {articolo[key][1]}           {articolo_s[f'{key}_scontato'][1][0]}€          {articolo_s[f'{key}_scontato'][0]}€")
                except:
#                                                                                            se l'articolo ha lo sconto del 2% 
                    print(f"{key}           {articolo[key][0]}€           {articolo[key][1]}           {articolo_s[f'{key}_scontato'][1]}€             {articolo_s[f'{key}_scontato'][0]}€")
            except:
#                                                                                               se l'articolo non ha sconto
                print(f"{key}           {articolo[key][0]}           {articolo[key][1]}                                                             {articolo[key][2]} ")
#                                                                                      se non sono stati inseriti dati ne forzo l'inserimento
    else:    
        print("nessun articolo inserito!! Inserire prima l'articolo")
        c_input()
        
    input("premere invio per continuare...")
main()
