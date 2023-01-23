import math as m
riso=0
while 0==0:
    caselle = int(input("inserisci numero di caselle: "))
    for i in range(caselle):
        riso1 = int(m.pow(2,i))
        riso = riso +riso1
        print("nella casella",i+1,"ci sono",riso1,"chicchi di riso")
    print("il totale e:",riso)