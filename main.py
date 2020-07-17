import sys
from tkinter import *
import tkinter as tk
import numpy as np
import os

#range of values for the visual
#viz_rng = np.arange(1.5,1.7,.02) #option range
viz_rng = np.arange(109,110,.05) #tp range

class MyWindow:
	def __init__(self, win):
		#create labels 'lbl' and entry fields 't' for inputs 1-6

		self.lbl1=Label(win, text='Size') #lbl1
		self.lbl2=Label(win, text='Price')
		self.lbl3=Label(win, text='Strike')
		self.lbl4=Label(win, text='Size')
		self.lbl5=Label(win, text='Price')
		self.lbl6=Label(win, text='Strike')

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

		#buttons
		self.btn1=Button(win, text='Update') #create button, add text
		self.b1=Button(win, text='Update', width='12', height='2', fg='green', bg='green', command=self.b1rez) #connect w/ command / format
		self.b1.place(x=275, y=12) #spacing for buttons

		self.btn2=Button(win, text='Update')
		self.b2=Button(win, text='Update', width='12', height='2', fg='green', bg='green', command=self.s1rez)
		self.b2.place(x=275, y=158)


		self.btn3=Button(win, text='ROI')
		self.b3=Button(win, text='ROI', width='6', height='2', fg='blue', bg='blue', command=self.roi)
		self.b3.place(x=50, y=90)

		self.btn4=Button(win, text='BuySell')
		self.b4=Button(win, text='BuySell', width='6', height='2', fg='blue', bg='blue', command=self.buysell)
		self.b4.place(x=50, y=20)


		self.btn5=Button(win, text='Overview')
		self.b5=Button(win, text='Overview', width='6', height='2', fg='blue', bg='blue', command=self.overview)
		self.b5.place(x=50, y=160)


		self.btn6=Button(win, text='Quit')
		self.b6=Button(win, text='Quit', width='6', height='2', fg='red', bg='red', command=quit)
		self.b6.place(x=50, y=230)

	def buysell(self):
		from charts import buysell
		buysell()
	def roi(self):
		from charts import roi
		roi()
	def overview(self):
		from charts import overview
		overview()

	def quit(self):
		quit()

	def b1rez(self):
		b1sz, b1p, b1stk=float(self.t1.get()), float(self.t2.get()), float(self.t3.get())
		b1r=float(b1p * b1sz)
		b1w=float(100*b1sz + (-b1r))
		b1_rez = [b1w if n > abs(b1stk) else -b1r for n in viz_rng]
		with open('b1results.txt', 'w') as f:
			for n in range(0,len(viz_rng)): print(viz_rng[n], ',', b1_rez[n], file=f)
	
	def s1rez(self):
		s1sz, s1p, s1stk=float(self.t4.get()), float(self.t5.get()), float(self.t6.get())
		s1r= float((100-s1p)*s1sz)
		s1w= float(s1p*(s1sz))
		s1_rez = [s1w if n < abs(s1stk) else -s1r for n in viz_rng]
		with open('s1results.txt', 'w') as f:
			for n in range(0,len(viz_rng)): print(viz_rng[n], ',', s1_rez[n], file=f)

#GUI
window=Tk() #initialize tcl/tk interpreter
window.title('Real-Time Derivative Model v1.6.2')
window.geometry("800x300-1000-1000")
try:	
	logo=tk.PhotoImage(file="sms_gui.png") 
	w1=tk.Label(window, image=logo).pack(side="right")
except: pass #open GUI w/out A logo.png
w2=tk.Label(window, padx=10).pack(side="left") #format window for GUI

b1lb=tk.Label(window, text="Buy", justify="right", bd=2, height=2, font="Times 22").pack() #labels above update buttons
s1lb=tk.Label(window, text="Sell", justify="right", bd=5, height=60, font="Times 22").pack()

mywin=MyWindow(window) #link MyWindow class and tk interpretter

window.mainloop() #execute infinite loop


