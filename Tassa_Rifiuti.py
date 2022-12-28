#Giorgio Bruno Modeo


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
a = True

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
#                                                                                      faccio un ciclo in modo che l'applicazzione possa essere ripetuta
#                                                                                      cancello la vecchia interfaccia grafica e la vecchia lista in modo da non dover
#                                                                                      chiudere l'app per inserire più dati  
    while a:
        os.system("cls")
        del inp[:]
#                                                                                      richiamo la funzione C_inp
        C_inp(f"selezziona la funzione che vuoi utilizzare{due}: ")
#                                                                                      richiamo la funzione f_menu
        f_menu()

#                                                                                   + controllo input
def C_inp(st):
    try:
        inp.append(float(input(st)))
    except:
        print("hai sbagliato input reinserisci il dato")

#                                                                                   + funzione menu
def f_menu():
    match inp[0]:
#                                                                                      prima scelta la che tipo di proprieta su vuole utilizzare
        case 1:
#                                                                                         inserisco i dati
            C_inp(f"selezziona la proprieta di cui vuoi calcolare la tari {uno}: ")
#                                                                                         richiamo categoria
            categoria()
#                                                                                      seconda scelta stampa informazzioni 
        case 2:
            info()
#                                                                                      uscita            
        case _:
            print("uscita...")  
            global a
            a = False

#                                                                                   + categoria
def categoria():
        match inp[1]:
#                                                                                      prima scelta utilizzare i dati di abitazzione in uso 
#                                                                                      (key di riferimento nel dizzionario :'abit_uso')
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
#                                                                                      seconda scelta utilizzare i dati di alloggi a disposizzione 
#                                                                                      (key di riferimento nel dizzionario :'all_disp')
            case 2:
                print('hai selezzionato "alloggi a disposizzione"')
                print("inserisci i resitenti nell'immobile: ")     
                C_inp("")
                print("inserisci i metri quadrati dell'immobile")
                C_inp("")
                comp_fam(affitto,affitto,inp[3]) 
#                                                                                      defoult scelta utilizzare i dati di box privati 
#                                                                                      (key di riferimento nel dizzionario :'box')
            case _:
                print('hai selezzionato "box privati"')
#               inserisco automaticamente 1 in modo da poter riutilizzare comp_fam
                inp.append(1)
                print("inserisci i metri quadrati dell'immobile")
                C_inp("")
                comp_fam(affitto,affitto,inp[3]) 

#                                                                                   + componenti famiglia
def comp_fam(n1,n2,mq):
    match inp[2]:
#                                                                                      prima scelta utilizzare i dati con solo una persona in famiglia
        case 1:
            calc_T(n1[1][0],n2[1][1],mq)
#                                                                                      seconda scelta utilizzare i dati con due persone in famiglia
        case 2:
            calc_T(n1[2][0],n2[2][1],mq)
#                                                                                      terza scelta utilizzare i dati con tre o più persone in famiglia
        case _:
            calc_T(n1[3][0],n2[3][1],mq)

#                                                                                   + calcolo tari
#                                                                                   ho utilizzato questa formula >>>mq * tariffa variabile = tot + tarriffa fissa<<<
def calc_T(n1,n2,n3):
#                                                                                      calcolo la tari utilizzando i dati precedentemente inseriti
#   definisco questa variabile {i} globale in modo che una volta modificata in questa funzione venga mantenuta in tutto il codice
    global i
#                                                                                      calcolo la tariffa variabile 
    tari.update([(f'tot_{i}' , [n3*n1])])
#                                                                                      aggiungo alla tariffa variabile la tariffa fissa
    tari[f'tot_{i}']+=[tari[f'tot_{i}'][0] + n2]
#                                                                                      applico al totale il 5% di sconto
    tari[f'tot_{i}']+=[tari[f'tot_{i}'][1]-((tari[f'tot_{i}'][1]*5)/100)]
#                                                                                      arrotondo i risultati
    tot_r = round(tari[f'tot_{i}'][1],5)
    tot_s_r = round(tari[f'tot_{i}'][2],5)
#                                                                                      aggungo ad un database temporane i totali gia scontati
    tari['tot'] += [tot_s_r]
    print(f'\nil totale e: {tot_r}€ \nil totale scontato e: {tot_s_r}€ ')
    input("premere invio per continuare...")    
    i =+ 1

#                                                                                   + stampa informazzioni
def info():
#                                                                                      provo a stampare le informazzioni altrimenti ne forzo l'inserimento
    c=0
    try:
        for value in tari['tot']:
            print(f'il costo gia scontato della tari n: {c+1}\ne di: {value}€')
            c =+ 1
        print(f"hai {i} tari\n ")
        input("premere invio per continuare...")
    except:
        print("attenzione inserire prima i dati")
        C_inp(uno)
        categoria()

main()


