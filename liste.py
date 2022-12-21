#giorgio modeo
"""
1. Calcolare quale è la persona più alta di tutto l’elenco e stampare
2. Calcolare la persona più bassa di tutto l’elenco
3. Dato un nome di persona stampare la sua altezza
4. Data una altezza stampare l’elenco delle persone che hanno quella altezza
5. Ordinare l’elenco in ordine crescente di altezza
6. Stampare elenco con nomi e altezze
"""
from random import randrange as ra
import numpy as np


persona={
    "omar" : [143],
    "mario" : [180],
    "alberto" : [202],
    "giovanni" : [123],
    "aldo" :[124],
    "luca" : [157]
}

for name,altezza in persona.items():
    print(name + ": "+str(altezza)+" cm")

alto= max(persona.values())
basso= min(persona.values())


print(alto)

