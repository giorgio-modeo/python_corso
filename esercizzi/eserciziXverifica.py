import os   
def main():
    a = True
    while a:
        os.system("cls")
        menu()
        a = switch()

def menu():
    m = """
        +--------------------+
        |        MENÙ        |
        +--------------------+
        | 1.                 |
        | 2.                 |
        | 3.                 |
        | 4.                 |
        |                    |
        |                    |
        | altro ==>  uscita  |
        |                    |
        +--------------------+
        """
    print(m)

def switch():
    a = True
    selezzione = inp_int("inserisci scelta: ")
    match selezzione:
        case 1:
            s1()
            input("premi per continuare...")
        # case 2:
        # case 3:
        # case 4:
        case _:
            a = False
    return a

def s1():
    diz = {}
    diz.update({'nome': input("inserisci il nome: "),"cogniome": input("inserisci il cogniome: ")})
#   diz.update({input("key: ") :  input("value: ")})
    print(diz)

def inp_int(str):
    while True:
        try:
            i = int(input(str))
            print("\n")
            break
        except:
            print("input errato")
    return i
main()
