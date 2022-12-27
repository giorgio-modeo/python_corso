# quota fissa = mq * n_persone
# quota fissa + quota variabile 
#  m    € a persona     tot     tar fissa 
# 100 * 1,23764     = 123,764 + 49,92488

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
    'box':[0.34758,0.35771]
}

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

inp=[]
utilizzata = tari['abit_uso']
affitto = tari['all_disp']


    
def main():
    ins_d()
    
def ins_d():  
    C_inp(f"selezziona la funzione che vuoi utilizzare{due}: ")
    f_menu()




    
def C_inp(st):
    while True:
        try:
            inp.append(float(input(st)))
            break
        except:
            print("hai sbagliato input reinserisci il dato")

def f_menu():
    match inp[0]:
        case 1:
            print("selezziona la proprieta di cui vuoi calcolare la tari ")
            C_inp(uno)
            categoria()
        case 2:
            info()
            
        case _:
            print("uscita")  
            

def categoria():
        match inp[1]:
            case 1:
                print('hai selezzionato "abitazzione in uso"')
                print("inserisci i resitenti nell'immobile: ")     
                C_inp("")
                print("inserisci i metri quadrati della casa")
                C_inp("")
                print(inp)
                comp_fam(inp[3]) 
            case 2:
                print('hai selezzionato "alloggi a disposizzione"')
                print('hai selezzionato "abitazzione in uso"')
                print("inserisci i resitenti nell'immobile: ")     
                C_inp("")
                print("inserisci i metri quadrati della casa")
                C_inp("")
                print(inp)
                comp_fam(inp[3]) 
            case _:
                print('hai selezzionato "box privati"')
                
                
#                                                                                   componenti famiglia
def comp_fam(mq):
    match inp[2]:
        case 1:
            calc_T(utilizzata[1][0],utilizzata[1][1],mq)
        case 2:
            calc_T(utilizzata[2][0],utilizzata[2][1],mq)
        case _:
            calc_T(utilizzata[3][0],utilizzata[3][1],mq)



def calc_T(n1,n2,n3):
    tar_fissa = (n3*n1)
    tari.update([('tot_1' , tar_fissa + n2)])
    print(tari)
    return tar_fissa

x = calc_T 
def info(x):
    print(x)
main()


