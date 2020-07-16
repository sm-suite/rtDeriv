#A1 import packages
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
plt.style.use(['ggplot'])
import matplotlib.animation as animation
import time

ro = lambda x : round(x, ndigits=2)



def roi():
	fig = plt.figure(figsize=(10, 4))
	ax1, ax2 = fig.add_subplot(121), fig.add_subplot(122)


	def Animate2tp(i):
		pullData = open("b1results.txt","r").read()
		pullData1 = open("s1results.txt", "r").read()
		dataArray = pullData.split('\n') 
		dataArray1 = pullData1.split('\n')
		viz_rng, net, b1, s1 = [], [], [], []
		for eachLine in dataArray:
			if len(eachLine)>1: 
				x,y = eachLine.split(',')
				viz_rng.append(float(x))
				b1.append(float(y))
		for eachLine in dataArray1:
			if len(eachLine)>1:
				j,b = eachLine.split(',')
				s1.append(float(b))

		zipped_rez = zip(b1, s1)
		net = [x+y for (x,y) in zipped_rez]
		trisk = abs(min(b1)) + abs(min(s1))
		roi = [(val/trisk)*100 for val in net]
		broi = [(val/trisk)*100 for val in b1]
		sroi = [(val/trisk)*100 for val in s1]


		#format subplots in figure
		for ax in [ax1, ax2]: ax.clear()
		#for ax in [ax1, ax2]: ax.set_title("Buy/Sell/Net", fontsize=12)
		for ax in [ax1, ax2]: ax.set_ylabel("ROI(%)", fontsize=12)
		ax1.set_title("Buy/Sell", fontsize=12)
		ax2.set_title("Net", fontsize=12)


		ax1.stem(viz_rng,sroi, linefmt='None', markerfmt='r_--', use_line_collection=True)		
		ax1.stem(viz_rng,broi, linefmt='None', markerfmt='g+--', use_line_collection=True)
		ax1.plot(viz_rng,broi, 'C7o', alpha=0.5)
		ax1.plot(viz_rng,sroi, 'C6o', alpha=0.5)

		ax2.stem(viz_rng,roi, linefmt='yellow', markerfmt='bv--', use_line_collection=True)


		for ax in [ax1, ax2]: ax.set_xlabel('Strike Price', fontsize=12)

	fig.suptitle("ROI Model", fontsize=14)
	
	#assign variable 'ani'; matplotlib's animation module, with 'dAnimate' function as an operator.
	ani = animation.FuncAnimation(fig, Animate2tp, interval=1000)

	plt.show()

