import tkinter as tk

def crearSeñal(canvas:tk.Canvas,signal):
    canvas.delete("all")
    lenght = len(signal)
    spaceLen = canvas.winfo_width() / lenght
    last = 1
    for x in range(lenght):
        canvas.create_text(((spaceLen/2)*(2*x+1)),20,text=signal[x],fill="black")
        dashLineCoodinate = spaceLen*(x+1),0,spaceLen*(x+1),canvas.winfo_height()
        canvas.create_line(dashLineCoodinate, dash=(10,5))
        print(last,signal[x])
        if (signal[x] != last):
            last = signal[x]
            translineCoordinate = spaceLen*x,50,spaceLen*x,150
            canvas.create_line(translineCoordinate, fill="red")
        print(last, type(last))
        if (last == '1'): 
            print("en 50")
            lineCoordiante = spaceLen*x,50,spaceLen*(x+1),50
        else: 
            print("en 150")
            lineCoordiante = spaceLen*x,150,spaceLen*(x+1),150
        canvas.create_line(lineCoordiante, fill="red")
        

