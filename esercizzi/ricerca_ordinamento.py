#                                       Ordinamento Insertion Sort
def insertionSort(lista):
    for i in range(len(lista)-1):
# ciclo interno che trova il valore minimo e lo inserisce in posizione i
        for j in range(i+1,len(lista)):
            if (lista[i]>lista[j]):
                lista[i],lista[j]=lista[j],lista[i]
lista = [54,26,93,17,77,31,44,55,20]
insertionSort(lista)
print(lista)

#                                       Ordinamento Selection Sort
def SelectionSort(lista):
    for i in range(len(lista)-1): # i = indice elemento perno
        #// cerca il più piccolo elemento dalla posizione i alla posizione N-1
        jmin = i #// jmin indice dell'elemento minore
        for j in range(i+1,len(lista)):
            if (lista[j] < lista[jmin] ):
            #se l'elemento minore è in posizione j, assegna j a jmin
                jmin = j
        if (i != jmin):
            # se (i != jmin) è stato trovato un elemento minore in posizione jmin
            # SCAMBIO elemento in posizione i con elemento in posizione jmin
            lista[jmin],lista[i]=lista[i],lista[jmin]
lista = [54,26,93,17,77,31,44,55,20]
SelectionSort(lista)
print(lista)

#Ordinamento Bubble sort
def BubbleSort(lista):
# la variabile Scambio indica se durante una scansione si è verificato almeno uno scambio
    scambio = True
    ultimo = len(lista)-1
    while ultimo > 0 and scambio:
        scambio = False
        for i in range(ultimo):
            if lista[i]>lista[i+1]:
                scambio = True
                lista[i],lista[i+1]=lista[i+1],lista[i]
                #temp = lista[i]
                #lista[i] = lista[i+1]
                #lista[i+1] = temp
            ultimo = ultimo-1
lista=[20,30,40,90,50,60,70,80,100,110]
BubbleSort(lista)
print(lista)


#Ricerca SEQUENZIALE
def RicercaSequenziale(lista, item):
    pos = 0
    found = False
    while pos < len(lista) and not found:
        if lista[pos] == item:
            found = True
        else:
            pos = pos+1
        return found
testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(RicercaSequenziale(testlist, 3))
print(RicercaSequenziale(testlist, 13))

#Ricerca BINARIA
def RicercaBinaria(lista, item):
    primo = 0
    ultimo = len(lista)-1
    trovato = False
    while primo<=ultimo and not trovato:
        medio = (primo + ultimo)//2
        if lista[medio] == item:
            trovato = True
        else:
            if item < lista[medio]:
                ultimo = medio-1
            else:
                primo = medio+1
    return trovato
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(RicercaBinaria(testlist, 3))
print(RicercaBinaria(testlist, 13))
