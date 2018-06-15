from tkinter import *
import math

currFunctions = []
currColours = []
scale = 10
frame = Frame()
frame.pack()
canvas = Canvas(frame,bg="#000000",height=500,width=500)
canvas.pack()
entry = Entry(frame)
colourSwitch = Entry(frame)
entry.pack()
colourSwitch.pack()
entry.insert(0,"y=x*x")
colourSwitch.insert(0,"cyan")

def drawLineNums():
    for i in range(int(-250/scale),int(250/scale)):
        canvas.create_text(250,250-i*scale,fill="white",font="Arial 7",text=str(i))
        canvas.create_text(i*scale+250,250,fill="white",font="Arial 7",text=str(i))

def clear():
    canvas.delete("all")
    canvas.create_line(0, 250, 500, 250, fill="grey", width=0)
    canvas.create_line(250, 0, 250, 500, fill="grey", width=0)
    global currFunctions
    global currColours
    currFunctions = []
    currColours = []
    drawLineNums()
    
def graph():
    function = entry.get()
    currColour = colourSwitch.get().lower()
    currColours.append(currColour)
    if function != "":
        function = function[2:]
        currFunctions.append(function)
        for i in range(int(-250/scale),int(250/scale)):
            tempFunc = function.replace("x",str(i))
            y=0
            try:
                y = eval(tempFunc)
            except:
                print("Undefined")
            y *= -1
            canvas.create_oval(i*scale+250, y*scale+250, i*scale+250, y*scale+250, width = 0, fill = currColour)

def zoom_in():
    canvas.delete("all")
    canvas.create_line(0, 250, 500, 250, fill="grey", width=0)
    canvas.create_line(250, 0, 250, 500, fill="grey", width=0)
    drawLineNums()
    global scale
    scale += 1
    for a in range(len(currFunctions)):
        function = currFunctions[a]
        currColour = currColours[a]
        if function != "":
            for i in range(int(-250/scale),int(250/scale)):
                tempFunc = function.replace("x",str(i))
                y=0
                try:
                    y = eval(tempFunc)
                except:
                    print("Undefined")
                y *= -1
                canvas.create_oval(i*scale+250, y*scale+250, i*scale+250, y*scale+250, width = 0, fill = currColours[a])

def zoom_out():
    canvas.delete("all")
    canvas.create_line(0, 250, 500, 250, fill="grey", width=0)
    canvas.create_line(250, 0, 250, 500, fill="grey", width=0)
    drawLineNums()
    global scale
    if scale - 1 > 0:
        scale -= 1
    for a in range(len(currFunctions)):
        function = currFunctions[a]
        currColour = currColours[a]
        if function != "":
            for i in range(int(-250/scale),int(250/scale)):
                tempFunc = function.replace("x",str(i))
                y=0
                try:
                    y = eval(tempFunc)
                except:
                    print("Undefined")
                y *= -1
                canvas.create_oval(i*scale+250, y*scale+250, i*scale+250, y*scale+250, width = 0, fill = currColours[a])

drawLineNums()
canvas.create_line(0, 250, 500, 250, fill="grey", width=0)
canvas.create_line(250, 0, 250, 500, fill="grey", width=0)
zoomOut = Button(frame, text="Zoom Out",command=zoom_out).pack(side=BOTTOM)
zoomIn = Button(frame, text="Zoom In",command=zoom_in).pack(side=BOTTOM)
clearB = Button(frame, text="Clear", command=clear).pack(side=BOTTOM)
graphB = Button(frame, text="Graph", command=graph).pack(side=BOTTOM)
frame.mainloop()

"""
I used these sites to learn some of the syntax:

String replace: https://www.tutorialspoint.com/python/string_replace.htm
Point on canvas: https://stackoverflow.com/questions/39888580/how-can-i-draw-a-point-with-canvas-in-tkinter
Line on canvas: https://stackoverflow.com/questions/25701347/how-to-draw-a-line-on-a-canvas
Text box: http://effbot.org/tkinterbook/entry.htm
eval function: https://stackoverflow.com/questions/9383740/what-does-pythons-eval-do
TKinter canvas: https://www.tutorialspoint.com/python/tk_canvas.htm
Clearing the TKinter canvas: https://stackoverflow.com/questions/15839491/how-to-clear-tkinter-canvas
"""
