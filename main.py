from tkinter import *
master = Tk()

w= Canvas(master, width=200, height = 200)
w.pack()

r1 = w.create_rectangle(10,10,10,10, fill="red")

global xMove
global yMove

xMove = 10
yMove = 0

#this class will build the player
#Requires a need for an array and to keep rack of direction and current coordinates on the grid.
#movement will need to move to the location of the element in front of it. Follow the array.
#need to track coordiates, array location, expand on the array, and check if head hits itself.
class player:
    x = 10

def move():
    w.move(r1, xMove, yMove)
    w.after(250, move)

#This is directional movement for the square, prevents it from reversing direction.
#Uses global varibles to keep track of the direction it is moving.
def keypress(event):
    global xMove
    global yMove
    if event.char=="a" and xMove!= 10:
        xMove = -10
        yMove = 0
    elif event.char == "s" and yMove!=-10:
        yMove = 10
        xMove = 0
    elif event.char == "d" and xMove!=-10:
        xMove = 10
        yMove = 0
    elif event.char == "w" and yMove!=10:
        yMove = -10
        xMove = 0;

master.bind("<Key>", keypress)
move()
master.mainloop()
#adding a comment to see what happens.
