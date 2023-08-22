import tkinter as tk 

def printParidad():
    print(paridad.get())

#Creacion ventana
root = tk.Tk()
root.geometry("500x500")
root.title("Proyecto 1 Diseño Logico")

#Creacion Labels
Lingreso = tk.Label(root,text ="Ingrese numero binario: ")
Lbinario = tk.Label(root,text ="Binario: ")
Loctal = tk.Label(root,text ="Octal: ")
Ldecimal = tk.Label(root,text ="Decimal: ")
LNZRI = tk.Label(root,text ="Señal NRZI: ")
lsignal = tk.Label(root, text="[insertar imagen de señal]")
Lparidad = tk.Label(root,text ="Paridad: ")
Lingreso.grid(column=0,row=0)
Lbinario.grid(column=0,row=1)
Loctal.grid(column=0,row=2)
Ldecimal.grid(column=0,row=3)
LNZRI.grid(column=0,row=4,columnspan=2)
lsignal.grid(column=0,row=5,columnspan=2)
Lparidad.grid(column=0,row=6,rowspan=2)

#Creacion entries
numeroBinarioHexadecimal = tk.Entry(root)
numeroBinarioHexadecimal.grid(column=1,row=0)

#Opciones paridad
paridad = tk.IntVar()
paridad.set(2)
Rparpar = tk.Radiobutton(root, text="Paridad par", variable=paridad, value=2,command=printParidad)
Rparimpar = tk.Radiobutton(root, text="Paridad impar", variable=paridad, value=1,command=printParidad)
Rparpar.grid(column=1,row=6)
Rparimpar.grid(column=1,row=7)


root.mainloop()