import tkinter as tk 
from basesnum import *

def printParidad():
    print(paridad.get())

#Creacion ventana
root = tk.Tk()
root.title("Proyecto 1 Diseño Logico")

#Creacion ingreso de numero
Lingreso = tk.Label(root,text ="Ingrese numero binario: ")
numeroBinarioHexadecimal = tk.Entry(root)
Bingreso = tk.Button(root,text="Ingresar")
Lingreso.grid(column=0,row=0)
numeroBinarioHexadecimal.grid(column=1,row=0)
Bingreso.grid(column=2,row=0)

#Creacion tabla 1
T1titulo = tk.Label(root,text ="Tabla 1. Conversión de numero a Binario, Octal y decimal",anchor="center")
T1titulo.grid(column=0,row=1,columnspan=3)


#Creacion señal
LNZRI = tk.Label(root,text ="Señal NRZI: ", anchor="center")
lsignal = tk.Label(root, text="[insertar imagen de señal]",anchor="center")
LNZRI.grid(column=0,row=4,columnspan=3)
lsignal.grid(column=0,row=5,columnspan=3)



#Opciones paridad
Lparidad = tk.Label(root,text ="Paridad: ")
Lparidad.grid(column=0,row=6,rowspan=2)
paridad = tk.IntVar()
paridad.set(2)
Rparpar = tk.Radiobutton(root, text="Paridad par", variable=paridad, value=2,command=printParidad)
Rparimpar = tk.Radiobutton(root, text="Paridad impar", variable=paridad, value=1,command=printParidad)
Rparpar.grid(column=1,row=6,columnspan=2)
Rparimpar.grid(column=1,row=7,columnspan=2)


root.mainloop()