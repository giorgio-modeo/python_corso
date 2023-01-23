import os

men = """
            *************************************************
            *                   alunni                  *
            *************************************************

            *************************************************
            *             MENÙ UTENTE PRINCIPALE            *
            *************************************************
            *   I inserire i dati                           *
            *   L leggere i dati dal file e stamparli       *
            *   F fine programma                            *
            *************************************************
"""
a = True
#                                                                                   + main
def main():
    ins = False
    while a:
        os.system("cls")
        menu(ins)

def menu(ins):
    print(men)
    seleziona = str(input("inserisci l'opzione"))
    match seleziona:
        case "i"|"I":
            ins = True
            stream=op_a()
            nome,media,esito = inserimento()
            scrivi(stream,nome,media,esito)
        case "l"|"L":
            if ins ==True:
                stream=op_r()
                stampa(stream)
            else:
                print("inserire prima un voto")
            input()
        case"f"|"F":
            a = False
def inserimento():
    nome =str(input("inserisci il nome: "))
    while True:
        media = float(input("inserisci la media: "))
        cont(media)
        break

    if media >=6:
        esito = "Promosso"
    else:
        esito = "Bocciato"
    return nome,media,esito

def cont(a):
    if (a > 10)or (a <1):
        print("imput errato")

def op_a():
    stream=open("esercizzi_file\esercizzio\studenti.txt","a",encoding="utf-8")
    return stream

def op_r():
    try:
        stream=open("esercizzi_file\esercizzio\studenti.txt","r+",encoding="utf-8")
        return stream
    except:
        print("")

def scrivi(stream,nome,media,esito):
    stream.write(f"nome: {nome}\nmedia: {media}\nesito: {esito}")
    stream.close()

def stampa(stream):
    print(stream.read())
    stream.close()

main()
