#Giorgio Bruno Modeo

# quota fissa = mq * n_persone
# quota fissa + quota variabile 
#  m    € a persona     tot     tar fissa 
# 100 * 1,23764     = 123,764 + 49,92488
import os

#                                                                                   definisco un dizzionario con tutti i miei dati
tari={
    'abit_uso': {
        1:[1.23764,49.92488],
        2:[1.45422,134.17313],
        3:[1.62440,160.38370]
    },
    'all_disp':{
        1:[1.23764,39.93990],
        2:[1.45422,107.33850],
        3:[1.62440,128.30696]
    },
    'box':[0.34758,0.35771],
    'tot' : []
}

#                                                                                   definisco alcune variabili in modo da rendermi il lavoro più facile 
inp=[]
utilizzata,affitto = tari['abit_uso'],tari['all_disp']
i=0

#                                                                                   creo i due menù
uno = """ 

    1. abitazzione in uso

    2. alloggi a disposizzione

    3. box privati
"""

due = """ 

    1. Inserimento dati

    2. Stampa informazioni TARI

    3. Uscita
"""


#                                                                                   + main
def main():

#                                                                                   faccio un ciclo in modo che l'applicazzione possa essere ripetuta
#                                                                                   cancello la vecchia interfaccia grafica e la vecchia lista in modo da non dover
#                                                                                   chiudere l'app per inserire più dati  
    while True:
        os.system("cls")
        del inp[:]
#                                                                                   richiamo la funzione C_inp
        C_inp(f"selezziona la funzione che vuoi utilizzare{due}: ")
#                                                                                   richiamo la funzione f_menu
        f_menu()


#                                                                                   controllo input
def C_inp(st):
    try:
        inp.append(float(input(st)))
    except:
        print("hai sbagliato input reinserisci il dato")

#                                                                                   funzione menu
def f_menu():
    match inp[0]:
        case 1:
            print("selezziona la proprieta di cui vuoi calcolare la tari ")
            C_inp(uno)
            categoria()
        case 2:
            print(f"hai {i} tari\n ")
            info()
            
        case _:
            print("uscita")  ù
            pass
            
            

def categoria():
        match inp[1]:
            case 1:
                print('hai selezzionato "abitazzione in uso"')
                print("inserisci il numero di resitenti nell'immobile: ")     
                C_inp("")
                print("inserisci i metri quadrati dell'immobile")
                C_inp("")
                #abitazzione in uso 1 residente 20 mq 
                """
                24.7528€ di tassa variabile    
                74.67768€ di totale
                70.9438€ il totale scontato 
                """
                comp_fam(utilizzata,utilizzata,inp[3]) 
            case 2:
                print('hai selezzionato "alloggi a disposizzione"')

                print("inserisci i resitenti nell'immobile: ")     
                C_inp("")
                print("inserisci i metri quadrati dell'immobile")
                C_inp("")
                comp_fam(affitto,affitto,inp[3]) 
            case _:
                print('hai selezzionato "box privati"')
                inp.append(1)
                print("inserisci i metri quadrati dell'immobile")
                C_inp("")
                comp_fam(affitto,affitto,inp[3]) 


                

#                                                                                   componenti famiglia
def comp_fam(n1,n2,mq):
    match inp[2]:
        case 1:
            calc_T(n1[1][0],n2[1][1],mq)
        case 2:
            calc_T(n1[2][0],n2[2][1],mq)
        case _:
            calc_T(n1[3][0],n2[3][1],mq)




def calc_T(n1,n2,n3):
    global i,tot_s_r
    tari.update([(f'tot_{i}' , [n3*n1])])
    tari[f'tot_{i}']+=[tari[f'tot_{i}'][0] + n2]
    tari[f'tot_{i}']+=[tari[f'tot_{i}'][1]-((tari[f'tot_{i}'][1]*5)/100)]
    tot_r = round(tari[f'tot_{i}'][1],5)
    tot_s_r = round(tari[f'tot_{i}'][2],5)
    tari['tot'] += [tot_s_r]
    print(f'\nil totale e: {tot_r}€ \nil totale scontato e: {tot_s_r}€ ')
    input("premere invio per continuare...")    
    i =+ 1
    

def esc():
    pass


def info():
    tari1 = tari['tot']
    c=0
    try:
        for value in tari1:
            print(f'il costo gia scontato della tari n: {c+1}\ne di: {value}€')
            c =+ 1

        input("premere invio per continuare...")
    except:
        print("attenzione inserire prima i dati")
        C_inp(uno)
        categoria()
main()


