"""
1. Riempie un array di 50 elementi di numeri random tra 20 e 100.
2. Calcola il minimo di tutti gli elementi
3. Calcola il massimo di tutti gli elementi
4. Calcola la media di tutti gli elementi
5. Stampa l’array, il minimo, il massimo e la media
6. Copia l’array dei numeri random in un secondo array inizialmente vuoto
7. Copia l’array dei numeri random in ordine inverso in un terzo array inizialmente
vuoto
"""
from random import randrange
import numpy as np

numeri = []
mmm = []
numeri2 = []
for x in range(0,50):
    y = randrange(20,101)
    numeri.append(y)
print(numeri)
mmm.extend([min(numeri),max(numeri),np.mean(numeri)])
print("il minimo e: ",mmm[0],"\nil massimo e: ",mmm[1],"\nla media e: ", mmm[2])
numeri2.extend(numeri)
print(numeri2)
inverso = numeri2[::-1]
print(inverso)
