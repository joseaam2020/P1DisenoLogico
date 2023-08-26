import tkinter as tk 
from tkinter import messagebox
from basesnum import *

def printParidad():
    print(paridad.get())

def iniciarTabla(dimensiones,tabla):
    """
    Dimensiones es una dupla (x,y) con el tamaño de la tabla
    """
    matriz = []
    for x in range(dimensiones[0]):
        list = []
        for y in range(dimensiones[1]):
            #print(x,y,)
            newEntry = tk.Entry(tabla,width=60//dimensiones[0],state="disabled",justify="center")
            newEntry.grid(column=x,row=y)
            list.append(newEntry)
        matriz.append(list)
    return matriz

def entradaDatoTabla(posicion,dato,matriz):
    """
    Posicion es una dupla (x,y) donde agregar el dato
    """
    entry = matriz[posicion[0]][posicion[1]]
    print(entry)
    entry.configure(state="normal")
    entry.insert(0,dato)
    entry.configure(state="disabled")
def setValor():
    hex = numeroBinarioHexadecimal.get()
    print(hex)

    warning = False
    if len(hex) != 3:
        warning = True
    try: 
        dec = hex2dec(hex,2)
        bin = dec2bin(dec,'')
        octl = dec2oct(dec,'')
        print(dec, bin, octl)
        entradaDatoTabla((1,1),hex,matrizT1)
        entradaDatoTabla((1,2),dec,matrizT1)
        entradaDatoTabla((1,3),bin,matrizT1)
        entradaDatoTabla((1,4),octl,matrizT1)

    except: 
        warning = True

    if warning: 
        messagebox.showwarning(title="Error de ingreso", message="Por favor ingresar numero hexadecimal de la forma 000 a FFF")
    numeroBinarioHexadecimal.delete(0,'end')

#Creacion ventana
root = tk.Tk()
root.title("Proyecto 1 Diseño Logico")
root.resizable(False,False)

#Creacion ingreso de numero
Lingreso = tk.Label(root,text ="Ingrese numero binario: ")
numeroBinarioHexadecimal = tk.Entry(root)
Bingreso = tk.Button(root,text="Ingresar",command=setValor)
Lingreso.grid(column=0,row=0)
numeroBinarioHexadecimal.grid(column=1,row=0)
Bingreso.grid(column=2,row=0)

#Creacion tabla 1
T1 = tk.LabelFrame(root,text ="Tabla 1. Conversión de numero a Binario, Octal y decimal",labelanchor="n")
dimensionesT1 = (2,5)
matrizT1 = iniciarTabla(dimensionesT1,T1)
entradaDatoTabla ((0,0),"Base Numerica",matrizT1)
entradaDatoTabla ((1,0),"Valor",matrizT1)
entradaDatoTabla ((0,1),"Hexadecimal",matrizT1)
entradaDatoTabla ((0,2),"Decimal",matrizT1)
entradaDatoTabla ((0,3),"Binario",matrizT1)
entradaDatoTabla ((0,4),"Octal",matrizT1)
T1.grid(column=0,row=1,columnspan=3)


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