#modeo giorgio

selezzione = str(input('\nselezzionare la via percorsa dal camion: \n\nper il primo esercizzio \n-digitare "p"\n\nper il secondo esercizzio \n-caso a "a",\n-caso b "b", \n-caso c "c" \n\ndigita la tua scelta: '))

                                                                                            # menù di selezzione
match selezzione:
    case 'p':
        ponte = 7
        #        0 1 2 3
        ponti = [2,4,3,6]        
    case 'a':
        ponte = 2
        ponti = [6,2,4,5]
    case 'b':
        ponte = 8
        ponti = [6,2,9,5]
    case 'c':
        ponte = 8
        ponti = [9,9,4,7]


                                                                                            # calcolo delle tonnellate massime
if ponte > max(ponti):
    print("\nIl massimo tonnellaggio trasportabile è: ",max(ponti),"tonnellate\n")
else:
    print("\nIl massimo tonnellaggio trasportabile è: ",ponte,"tonnellate\n")               # crediti delle frasi matricola: ©ICTS22-24.386 


                                                                                            # scelta dell itinerario migliore
if ponte < ponti[0]:
    print("puoi utilizzare l'itinerario 1 con: ",ponti[0],"tonnellate")
elif (ponti[1] >= ponte) and (ponti[2] >= ponte) :
    print("puoi utilizzare l'itinerario 2 ")
elif ponte < ponti[3]:
    print("puoi utilizzare l'itinerario 3 con: ",ponti[3],"tonnellate")
elif max(ponti) == ponti[0]:
    print("puoi utilizzare l'itinerario 1 con: ",ponti[0],"tonnellate")
elif max(ponti) == ponti[3]:
    print("puoi utilizzare l'itinerario 3 con: ",ponti[3],"tonnellate")
else:
    print("puoi utilizzare l'itinerario 1 con: ",ponti[0],"tonnellate")
print("")
