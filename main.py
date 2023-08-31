import tkinter as tk 
from tkinter import END, messagebox
from basesnum import *
from paridad import *
from tabla import *
from signalNRZI import *

final_string = ""

def iniciarTabla(dimensiones,tabla):
    """
    Añade tkinter.entries al objeto indicado

    Dimensiones es una dupla (x,y) con el tamaño de la tabla.
    Tabla es un objeto de Tkinter que sea padre de los tkinter.Entry formados
    (debe ser objeto tkinter.Frame). 

    Devuelve una matriz con todas las entries creadas en la tabla.
    """
    matriz = []
    for x in range(dimensiones[0]):
        list = []
        for y in range(dimensiones[1]):
            newEntry = tk.Entry(tabla,width=60//dimensiones[0],state="disabled",justify="center")
            newEntry.grid(column=x,row=y)
            list.append(newEntry)
        matriz.append(list)
    return matriz

def entradaDatoTabla(posicion,dato,matriz):
    """
    Posicion es una dupla (x,y) donde agregar el dato
    El dato es un string o int para agregar al entry
    Matriz es una matriz de entries creada por iniciarTabla
    
    No devuelve nada
    """
    entry = matriz[posicion[0]][posicion[1]]
    entry.configure(state="normal")
    entry.delete(0,END)
    entry.insert(0,dato)
    entry.configure(state="disabled")

def serValorT1():
    """
    Coloca los valores de las conversiones en la tabla 1 y entrega la señal a crearSeñal
    """
    hex = numeroBinarioHexadecimal.get()
    numeroBinarioHexadecimal.delete(0,'end')
    warning = False
    print(len(hex))
    if len(hex) != 3:
        warning = True
    try: 
        if warning:
            raise Exception
        dec = hex2dec(hex,2)
        bin = dec2bin(dec,'')
        octl = dec2oct(dec,'')
        entradaDatoTabla((1,1),hex,matrizT1)
        entradaDatoTabla((1,2),dec,matrizT1)
        entradaDatoTabla((1,3),bin,matrizT1)
        entradaDatoTabla((1,4),octl,matrizT1)
        crearSeñal(Csignal,bin)
        
        global final_string
        newBin = bin
        while (len(newBin) < 12):
            newBin = "0" + newBin
        print(newBin)
        
        final_string = calculate_parity_bits(bin, paridad.get())
        table(final_string)
        
        
    except Exception as e: 
        print(e)
        warning = True
    
    if warning: 
        messagebox.showwarning(title="Error de ingreso", message="Por favor ingresar numero hexadecimal de la forma 000 a FFF")
    
    
#Creacion ventana
root = tk.Tk()
root.title("Proyecto 1 Diseño Logico")
root.resizable(False,False)

#Creacion ingreso de numero
Lingreso = tk.Label(root,text ="Ingrese numero hexadecimal: ")
numeroBinarioHexadecimal = tk.Entry(root)
Bingreso = tk.Button(root,text="Ingresar",command=serValorT1)
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
Csignal = tk.Canvas(root,bg="white",width=400,height=200)
LNZRI.grid(column=0,row=4,columnspan=3)
Csignal.grid(column=0,row=5,columnspan=3)



#Opciones paridad
Lparidad = tk.Label(root,text ="Paridad: ")
Lparidad.grid(column=0,row=6,rowspan=2)
paridad = tk.IntVar()
paridad.set(2)
Rparpar = tk.Radiobutton(root, text="Paridad par", variable=paridad, value=2)
Rparimpar = tk.Radiobutton(root, text="Paridad impar", variable=paridad, value=1)
Rparpar.grid(column=1,row=6,columnspan=2)
Rparimpar.grid(column=1,row=7,columnspan=2)

Ecambio = tk.Entry(root,width=100)
Bcambio = tk.Button(root, text="Cambiar un bit",command=lambda:table(final_string, "error", calculate_parity_bits(Ecambio.get(), paridad.get())))
#Ecambio.insert(0,bin)
Ecambio.grid(column=0, row=8)
Bcambio.grid(column=2,row=8)



root.mainloop()
