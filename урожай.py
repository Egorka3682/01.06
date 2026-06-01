import tkinter as tk
import math
def draw():
    xx = float(vhod_x.get())
    yy = float(vhod_y.get())
    canvas.delete("all")
    canvas.create_line(0, yy, 400, yy)
    canvas.create_line(xx, 0, xx, 400)
    canvas.create_text(390, yy+10, text='Ось Х')
    canvas.create_text(xx+10, 10, text='Ось У')
    for x in range(-800, 800):
        y = math.sin(x / 30) * 50
        canvas.create_oval(xx+x, yy-y, xx+x, yy-y)

graf = tk.Tk()
graf.title("График")
tk.Label(graf, text="X").pack()
vhod_x = tk.Entry(graf)
vhod_x.pack()

tk.Label(graf, text="Y").pack()
vhod_y = tk.Entry(graf)
vhod_y.pack()

tk.Button(graf, text="Построить", command=draw).pack()
canvas = tk.Canvas(graf, width=400, height=400, bg="white")
canvas.pack()
graf.mainloop()