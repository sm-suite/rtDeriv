#A1 import packages
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

def view4():
	#A2 define 'ro' and 'dType'
	ro = lambda x : round(x, ndigits=2)
	dType = 'option' #alt dType = 'option'

	#B initialize figure, add 6 subplots
	fig = plt.figure(figsize=(8, 6))
	ax1, ax2 = fig.add_subplot(221), fig.add_subplot(222)
	ax3, ax4 = fig.add_subplot(223), fig.add_subplot(224)

	#view function
	def Animate4(i):
		#import result data from .txt files
		pullData = open("b1results.txt","r").read()#pull data from .txt databases create dataArray objects
		pullData1 = open("s1results.txt", "r").read()
		dataArray = pullData.split('\n') #separate data by line for both dataArrays
		dataArray1 = pullData1.split('\n')
		viz_rng, net, b1, s1 = [], [], [], []
		for eachLine in dataArray: #loop through each line in 'dataArray' object
			if len(eachLine)>1: #for each line, save the first element to 'viz_rng', second to 'b1'.
				x,y = eachLine.split(',')
				viz_rng.append(float(x))
				b1.append(float(y))
		for eachLine in dataArray1: #similar to b1, just save s1_rez tho
			if len(eachLine)>1:
				j,b = eachLine.split(',')
				s1.append(float(b))

		#create 'net' set from b1 and s1
		zipped_rez = zip(b1, s1)
		net = [x+y for (x,y) in zipped_rez]
		bcs, wcs = ro(max(net)), ro(min(net))
		if max(b1) >= max(s1): bcsa = ro(max(b1))
		else: bcsa = ro(max(s1))
		if min(b1) <= min(s1): wcsa = ro(min(b1))
		else: wcsa = ro(min(s1))

		#bcs and wcs variables for resp. stats in visual

		#format subplots in figure
		for ax in [ax1, ax2, ax3, ax4]: ax.clear()
		for ax in [ax1, ax3]: ax.set_ylabel('Result($)', fontsize=12)
		for ax in [ax1, ax2]: ax.set_xticks([])
		ax2.set_title("Net \n " + "BCS: $" + str(bcs), fontsize=12)
		ax4.set_title("WCS: $" + str(wcs), fontsize=12)
		ax3.set_title("WCS: $" + str(wcsa), fontsize=12)
		
		#generate 4 visualizations for figure
		ax1.step(viz_rng,b1)
		ax1.step(viz_rng,s1)
		ax2.step(viz_rng,net)
		ax3.fill(viz_rng,b1)
		ax3.fill(viz_rng,s1)
		ax4.fill(viz_rng,net)


		#dType decision
		if dType == 'option':	
			ax1.set_title('Long/Short', fontsize=12)
			for ax in [ax3, ax4]: ax.set_xlabel('Strike Price', fontsize=14)
		elif dType == 'tp':
			ax1.set_title("Over/Under \n " + "BCS: $" + str(bcsa), fontsize=12)

			for ax in [ax3, ax4]: ax.set_xlabel('Total Points', fontsize=14)

	fig.suptitle("Real-Time Derivative Model" + "\n", fontsize=16)

	#assign variable 'ani'; matplotlib's animation module, with 'dAnimate' function as an operator.
	ani = animation.FuncAnimation(fig, Animate4, interval=1000)

	plt.show()

#view4()