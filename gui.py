import sys
from tkinter import *
import tkinter as tk
import numpy as np
import os

set_rng = np.arange(35,55,1)
typ3 = 'tp'
#typ3 = 'option'

window=Tk()
logo=tk.PhotoImage(file="atb.png")

w1=tk.Label(window, image=logo).pack(side="right")
w2=tk.Label(window, justify=tk.LEFT, padx=10).pack(side="left")
b1label=tk.Label(window, text="Over", justify="right", anchor="e", padx=50, bd=5, height=2, font="Times 24").pack()
s1label=tk.Label(window, text="Under", justify="right", anchor="e", padx=50, bd=5, height=102, font="Times 24").pack()

class MyWindow:
	def __init__(self, win):
		self.lbl1=Label(win, text='Risk')
		self.lbl2=Label(win, text='Odds')
		self.lbl3=Label(win, text='Score')
		self.lbl4=Label(win, text='Risk')
		self.lbl5=Label(win, text='Odds')
		self.lbl6=Label(win, text='Score')

		self.t1=Entry(bd=1)
		self.t2=Entry(bd=1)
		self.t3=Entry(bd=1)
		self.t4=Entry(bd=1)
		self.t5=Entry(bd=1)
		self.t6=Entry(bd=1)


		#need to make a for loop variable system for placement variables
		t1x, label1x, label1y, label4y = 200, 160, 50, 200
		
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

		self.btn1=Button(win, text='Update')
		self.btn2=Button(win, text='Update')
		self.btn3=Button(win, text='Quit')		
		self.b1=Button(win, text='Update', bg='black', command=self.b1rez)
		self.b2=Button(win, text='Update', bg='black', command=self.s1rez)
		self.b3=Button(win, text='Quit', fg='red', bg='red', command=window.quit)

		self.b1.place(x=100, y=100)
		self.b2.place(x=100, y=250)
		self.b3.place(x=100, y=275)


	def b1rez(self):
		b1r, b1o, b1stk=float(self.t1.get()), float(self.t2.get()), float(self.t3.get())
		b1w=float(b1r*(b1o-1))
		b1_rez = [b1w if n > abs(b1stk) else -b1r for n in set_rng]
		with open('b1results.txt', 'w') as f:
			for n in range(0,len(set_rng)): print(set_rng[n], ',', b1_rez[n], file=f)


	def s1rez(self):
		s1r, s1o, s1stk=float(self.t4.get()), float(self.t5.get()), float(self.t6.get())
		s1w=float(s1r*(s1o-1))
		s1_rez = [s1w if n < abs(s1stk) else -s1r for n in set_rng]
		with open('s1results.txt', 'w') as f:
			for n in range(0,len(set_rng)): print(set_rng[n], ',', s1_rez[n], file=f)

	def netrez(self):
		net_rez = [self.b1_rez + self.s1_rez]

mywin=MyWindow(window)

window.title('Real-Time Derivative Model')
window.geometry("800x300+10+10")
window.mainloop()


