import sys
from tkinter import *
import numpy as np
import os

set_rng = np.arange(35,55,1)
typ3 = 'tp'
#typ3 = 'option'

class MyWindow:
	def __init__(self, win):
		self.lbl1=Label(win, text='Over - Risk')
		self.lbl2=Label(win, text='Over - Win')
		self.lbl3=Label(win, text='Over - Score')
		self.lbl4=Label(win, text='Under - Risk')
		self.lbl5=Label(win, text='Under - Win')
		self.lbl6=Label(win, text='Under - Score')

		self.t1=Entry(bd=3)
		self.t2=Entry(bd=1)
		self.t3=Entry(bd=1)
		self.t4=Entry(bd=3)
		self.t5=Entry(bd=1)
		self.t6=Entry(bd=1)
		self.btn1=Button(win, text='Update')
		self.btn2=Button(win, text='Update')

		self.lbl1.place(x=100, y=50)
		self.t1.place(x=200, y=50)
		self.lbl2.place(x=100, y=75)
		self.t2.place(x=200, y=75)
		self.lbl3.place(x=100, y=100)
		self.t3.place(x=200, y=100)
		self.lbl4.place(x=100, y=150)
		self.t4.place(x=200, y=150)
		self.lbl5.place(x=100, y=175)
		self.t5.place(x=200, y=175)
		self.lbl6.place(x=100, y=200)
		self.t6.place(x=200, y=200)
		self.b1=Button(win, text='Update', command=self.test_b1rez)
		self.b2=Button(win, text='Update', command=self.test_s1rez)
		self.b1.place(x=50, y=100)
		self.b2.place(x=50, y=200)

	def test_b1rez(self):
		b1r=float(self.t1.get())
		b1w=float(self.t2.get())
		b1stk=float(self.t3.get())
		b1_rez = [b1w if n > abs(b1stk) else -b1r for n in set_rng]
		with open('b1results.txt', 'w') as f:
			for n in range(0,len(set_rng)): print(set_rng[n], ',', b1_rez[n], file=f)


	def test_s1rez(self):
		s1r=float(self.t4.get())
		s1w=float(self.t5.get())
		s1stk=float(self.t6.get())
		s1_rez = [s1w if n < abs(s1stk) else -s1r for n in set_rng]
		with open('s1results.txt', 'w') as f:
			for n in range(0,len(set_rng)): print(set_rng[n], ',', s1_rez[n], file=f)


window=Tk()
mywin=MyWindow(window)
window.title('Real-Time Derivative Model')
window.geometry("400x300+10+10")
window.mainloop()
