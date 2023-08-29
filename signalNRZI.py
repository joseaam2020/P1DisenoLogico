import tkinter as tk

def crearSeñal(canvas:tk.Canvas,signal):
    canvas.delete("all")
    lenght = len(signal)
    spaceLen = canvas.winfo_width() / lenght
    last = 50
    for x in range(lenght):
        canvas.create_text(((spaceLen/2)*(2*x+1)),20,text=signal[x],fill="black")
        dashLineCoodinate = spaceLen*(x+1),0,spaceLen*(x+1),canvas.winfo_height()
        canvas.create_line(dashLineCoodinate, dash=(10,5))
        if (signal[x] == '1'):
            if(last == 50): 
                last = 150
            else: 
                last = 50
            translineCoordinate = spaceLen*x,50,spaceLen*x,150
            canvas.create_line(translineCoordinate, fill="red")
        lineCoordiante = spaceLen*x,last,spaceLen*(x+1),last
        canvas.create_line(lineCoordiante, fill="red")
        

