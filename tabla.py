import tkinter as tk
from tkinter import END, messagebox


def getDatosError(inputNumber,entry:tk.Entry): 
    datoError = entry.get()
    cambios = 0
    for i in range(len(inputNumber)):
        if inputNumber[i] != datoError[i]:
            cambios += 1
    if cambios > 1: 
        messagebox.showwarning(title="Error de ingreso", message="Solo puede realizarse cambios en un bit")
        datoError = inputNumber
    print(datoError)
    #Insertar aqui funcion para arreglar paridad

def table(input_number):
    
    p1_indices = [0,2,4,6,8,10,12,14]
    p2_indices = [1,2,5,6,9,10,13,14]
    p4_indices = [3,4,5,6,11,12,13,14]
    p8_indices = [7,8,9,10,11,12,13,14]

    # Crear la ventana principal
    global t1
    t1 = ventana = tk.Tk()
    
    ventana.title("Tabla de Paridad")
    # Crear la tabla
    tabla = tk.Frame(ventana)
    tabla.pack()

    # Crear los encabezados de columna
    encabezados = ["", "p1", "p2", "d1", "p3", "d2", "d3", "d4", "p4", "d5", "d6", "d7", "d8", "d9", "d10", "d11", "d12"]
    datos = ["","Sin paridad", "p1", "p2", "p3", "p4", "Con Paridad"]

    
    for i in range (7):
            
        tk.Label(tabla, text=datos[i], font="Helvetica 14 bold", borderwidth=1, relief="solid", width=10, height=1).grid(row=i, column=0)

        for j in range(1, 17):
            tk.Label(tabla, text="", borderwidth=1, relief="solid", width=5, height=1).grid(row=i, column=j)

            if i == 0:
                tk.Label(tabla, text=encabezados[j], font="Helvetica 13 bold", borderwidth=0, relief="solid", width=5, height=1).grid(row=i, column=j)

            
            elif i == 1:
                if j in [1,2,4,8]:
                    continue
                else:
                    tk.Label(tabla, text=f"{input_number[j-1]}", borderwidth=0, relief="solid").grid(row=i, column=j)
                
  
            elif i == 2:
                par_index = -1
                if j-1 in p1_indices:
                    par_index = p1_indices.index(j-1)
                
                if par_index >= 0:
                    tk.Label(tabla, text=f"{input_number[j-1]}", borderwidth=0, relief="solid").grid(row=i, column=j)
                else:
                    continue
            elif i == 3:
                par_index = -1
                if j-1 in p2_indices:
                    par_index = p2_indices.index(j-1)

                if par_index >= 0:
                    tk.Label(tabla, text=f"{input_number[j-1]}", borderwidth=0, relief="solid").grid(row=i, column=j)
                else:
                    continue
            elif i == 4:
                par_index = -1
                if j-1 in p4_indices:
                    par_index = p4_indices.index(j-1)

                if par_index >= 0:
                    tk.Label(tabla, text=f"{input_number[j-1]}", borderwidth=0, relief="solid").grid(row=i, column=j)
                else:
                    continue

            elif i == 5:
                par_index = -1
                if j-1 in p8_indices:
                    par_index = p8_indices.index(j-1)
                
                if par_index >= 0:
                    tk.Label(tabla, text=f"{input_number[j-1]}", borderwidth=0, relief="solid").grid(row=i, column=j)
                else:
                    continue
            else:
                tk.Label(tabla, text=f"{input_number[j-1]}", borderwidth=0, relief="solid").grid(row=i, column=j)
    
    Ecambio = tk.Entry(ventana,width=100)
    Bcambio = tk.Button(ventana, text="Cambiar un bit",command=lambda: getDatosError(input_number,Ecambio))
    Ecambio.insert(0,input_number)
    Ecambio.pack()
    Bcambio.pack()
    t1.mainloop()
def reiniciar_ventana_t1():
    t1.destroy()
                








