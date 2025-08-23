import tkinter
from tkinter import *
import random
import time

res = "Letztes Ergebnis: "
sol = 0
addsol = 0
aufg = 0
inp = 0

def handleButton(event):
    global t
    global w
    global sol
    global inp
    global aufg
    global res
    inp = t.get()
    if inp[0] == "+":
        inp = inp.strip("+")
        addsol = int(sol) + int(inp)
        aufg = sol, "+", inp, "=", addsol
        v["text"] = (res,sol)
        sol = addsol
        w["text"] = aufg
        
    elif inp[0] == "-":
        inp = inp.strip("-")
        addsol = int(sol) - int(inp)
        aufg = sol, "-", inp, "=", addsol
        sol = addsol
        v["text"] = (res,sol)
        w["text"] = aufg
        
    elif inp[0] == "*":
        inp = inp.strip("*")
        addsol = int(sol) * int(inp)
        aufg = sol, "*", inp, "=", addsol
        sol = addsol
        v["text"] = (res,sol)
        w["text"] = aufg
        
    elif inp[0] == "/":
        inp = inp.strip("/")
        addsol = int(sol) / int(inp)
        aufg = sol, "/", inp, "=", addsol
        sol = addsol
        v["text"] = (res,sol)
        w["text"] = aufg
        
    else:
        aufg = inp, "=", eval (inp)
        sol = eval (inp)
        v["text"] = (res,sol)
        w["text"] = aufg

top = tkinter.Tk()

s1 = tkinter.Label(top, text = " "*100)
s1.pack()

v = tkinter.Label(top, text = "Calculator V0.2")
v.pack()

s2 = tkinter.Label(top, text = "_"*30)
s2.pack()

w = tkinter.Label(top, text = " ")
w.pack()

t = tkinter.Entry(top)
t.pack()

b = tkinter.Button(top, text = "Berechnen")
b.pack()
s1 = tkinter.Label(top, text = " "*100)
s1.pack()

b.bind ("<Button-1>", handleButton)

top.mainloop()
