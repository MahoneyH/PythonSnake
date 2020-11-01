from tkinter import *
master = Tk()

w= Canvas(master, width=200, height = 200)
w.pack()

#w.create_line(0,0,200,100)
#w.create_line(0,100,200,0,fill="red", dash=(4,4))

#w.create_rectangle(50,25,150,75, fill="blue")

r1 = w.create_rectangle(10,10,10,10, fill="red")

def keypress(event):
    x=0
    y=0
    if event.char=="a": x = -10
    elif event.char == "s": y = 10
    elif event.char == "d": x = 10
    elif event.char == "w": y = -10
    w.move(r1, x, y)

master.bind("<Key>", keypress)

master.mainloop()
#adding a comment to see what happens.