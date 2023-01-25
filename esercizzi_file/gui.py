from tkinter import filedialog 
import os
nome_file=filedialog.askopenfilename(filetypes=(("File di testo","*.txt"),("Tutti i file ","*.*")))
print(nome_file)

stream = open(nome_file, mode="r")
print(stream.read())
stream.close ()

stream=open("esercizzi_file/prova.txt","w.",encoding="utf-8")
st="e una frase di prova\n"
st1="questa frase e scritta al rigo successivo\n"
stream.write(st+st1)
stream.close()