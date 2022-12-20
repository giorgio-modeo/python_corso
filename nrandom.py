from random import random,randint,randrange
n = random()

print(n)
print("output 1")
for i in range(5):
    print(randint(1,20))

print("output 2")
for i in range(5):
    print(randrange(0,10,20))

print("output 3")
lista=[]
for x in range(0,6):
    y = randint(1,45)
    lista.append(y)
print(lista)