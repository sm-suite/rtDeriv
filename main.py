import sys
from tkinter import *
import tkinter as tk
import numpy as np
import os

#range of values for the visual
viz_rng = np.arange(40,51,1)

class MyWindow:
    def __init__(self, win):
        #create labels 'lbl' and entry fields 't' for inputs 1-6
        self.lbl1=Label(win, text='Risk') #lbl1
        self.lbl2=Label(win, text='Odds')
        self.lbl3=Label(win, text='Score')
        self.lbl4=Label(win, text='Risk')
        self.lbl5=Label(win, text='Odds')
        self.lbl6=Label(win, text='Score')
        self.t1=Entry(bd=1)#t1
        self.t2=Entry(bd=1)
        self.t3=Entry(bd=1)
        self.t4=Entry(bd=1)
        self.t5=Entry(bd=1)
        self.t6=Entry(bd=1)

        #simplify spacing adjustments with spacing variables.
        t1x, label1x, label1y, label4y = 200, 160, 50, 200
        
        #spacing for 6 lbl and 6 t.
        self.lbl1.place(x=label1x, y=label1y)
        self.lbl2.place(x=label1x, y=label1y+25)
        self.lbl3.place(x=label1x, y=label1y+50)
        self.t1.place(x=t1x, y=label1y)
        self.t2.place(x=t1x, y=label1y+25)
        self.t3.place(x=t1x, y=label1y+50)
        self.lbl4.place(x=label1x, y=label4y)
        self.lbl5.place(x=label1x, y=label4y+25)
        self.lbl6.place(x=label1x, y=label4y+50)
        self.t4.place(x=t1x, y=label4y)
        self.t5.place(x=t1x, y=label4y+25)
        self.t6.place(x=t1x, y=label4y+50)

        #buttons for updating databases (b1/s1) and quitting program
        self.btn1=Button(win, text='Update') #create button, add text
        self.b1=Button(win, text='Update', width='6', height='2', fg='green', bg='green', command=self.b1rez) #connect w/ command / format
        self.b1.place(x=275, y=12) #spacing for buttons

        self.btn2=Button(win, text='Update')
        self.b2=Button(win, text='Update', width='6', height='2', fg='green', bg='green', command=self.s1rez)
        self.b2.place(x=275, y=158)

        self.btn3=Button(win, text='Quit')      
        self.b3=Button(win, text='Quit', width='6', height='2', fg='red', bg='red', command=window.quit)
        self.b3.place(x=50, y=230)

        #buttons for displaying different visuals. 2x1(step), 2x2(step/bar), 2x3(step/bar/fill).
        self.btn4=Button(win, text='view 2')
        self.b4=Button(win, text='view 2', width='6', height='2', fg='blue', bg='blue', command=self.view2)
        self.b4.place(x=50, y=20)

        self.btn5=Button(win, text='view 4')
        self.b5=Button(win, text='view 4', width='6', height='2', fg='blue', bg='blue', command=self.view4)
        self.b5.place(x=50, y=90)

        self.btn6=Button(win, text='view 6')
        self.b6=Button(win, text='view 6', width='6', height='2', fg='blue', bg='blue', command=self.view6)
        self.b6.place(x=50, y=160)

    def view2(self):
        from view2 import view2
        view2()

    def view4(self):
        from view4 import view4
        view4()

    def view6(self):
        from view6 import view6
        view6()

        #command for updating the 'over' position. save viz_rng and b1_rez to b1results.txt
    def b1rez(self):
        b1r, b1o, b1stk=float(self.t1.get()), float(self.t2.get()), float(self.t3.get())
        b1w=float(b1r*(b1o-1))
        b1_rez = [b1w if n > abs(b1stk) else -b1r for n in viz_rng]
        with open('b1results.txt', 'w') as f:
            for n in range(0,len(viz_rng)): print(viz_rng[n], ',', b1_rez[n], file=f)
        
        #command for updating the 'under' position. save viz_rng and s1_rez to s1results.txt
    def s1rez(self):
        s1r, s1o, s1stk=float(self.t4.get()), float(self.t5.get()), float(self.t6.get())
        s1w=float(s1r*(s1o-1))
        s1_rez = [s1w if n < abs(s1stk) else -s1r for n in viz_rng]
        with open('s1results.txt', 'w') as f:
            for n in range(0,len(viz_rng)): print(viz_rng[n], ',', s1_rez[n], file=f)

#GUI

window=Tk() #initialize tcl/tk interpreter
window.title('Real-Time Derivative Model')
window.geometry("800x300+10+10")
logo=tk.PhotoImage(file="atb.png") #import .png file for GUI logo
w1=tk.Label(window, image=logo).pack(side="right") #format window for the logo in the GUI
w2=tk.Label(window, justify=tk.LEFT, padx=10).pack(side="left") #format window for the rest of the GUI
#label over / under input section of GUI
b1label=tk.Label(window, text="Over", justify="right", bd=5, height=2, font="Times 20").pack()
s1label=tk.Label(window, text="Under", justify="right", bd=5, height=60, font="Times 20").pack()

#link MyWindow class and interpretter
mywin=MyWindow(window)

#execute infinite loop (so the GUI remains operational)
window.mainloop()


