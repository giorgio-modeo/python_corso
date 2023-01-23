h = int(input("inserisci h: "))
k = int(input("inserisci k: "))
n = int(input("quanti numeri vuoi inserire: "))
for i in range(1, n+1):
    a = int(input("inserisci il numero: "))
    if ((a > h) and (a < k)) or ((a < h) and (a > k)):
        print("il numero e nel range")
    else:
        print("il numero non e nel range")