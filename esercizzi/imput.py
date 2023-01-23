def inp(st,n1,n2):
    while True:
        try:
            numero=int(input(st))
            if numero >= n1 and numero <= n2:
                break
            else:
                print("il numero non e nel intervallo")
        except:
            print("type error")
    return(numero)

a = inp("inserisci altezza",50,220)
b=inp("inserisci largezza",10,50)

