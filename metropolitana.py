g ="""
    s. settimanale
    m. mensile
    a. annuale
"""
h="""
    1. urbana 1
    2. extra urbana 2
    3. regionale 3
"""
zona = ["s","m","a"]
tipo = [1,2,3]
priorita = True
print(g)
a = input("inserisci la zona: ")
print(h)
b = int(input("inserisci il tipo: "))
c = input('inserire "bassa" per ricevere lo sconto\ninserisci la priorita: ')
if (a == zona[0]):
    match b:
        case 1:
            costo = 10
        case 2:
            costo = 5
        case 3:
            costo = 15
elif (a == zona[1]):
    match b:
        case 1:
            costo = 30
        case 2:
            costo = 20
        case 3:
            costo = 40
elif (a == zona[2]):
    match b:
        case 1:
            costo = 250
        case 2:
            costo = 150
        case 3:
            costo = 300
if c == "bassa":
    costoS = costo -((costo*20)/100)
    print(costoS)
else:
    print(costo)

