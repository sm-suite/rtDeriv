#A1 import packages
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
def view2():
	#A2 define 'ro' and 'dType'
	ro = lambda x : round(x, ndigits=2)
	dType, cType = 'tp', 'step' #alt dType = 'option'

	#B initialize figure, add subplots
	fig = plt.figure(figsize=(8, 6))
	ax1, ax2 = fig.add_subplot(211), fig.add_subplot(212)


	#view function
	def Animate2(i):
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

		#format subplots in figure
		for ax in [ax1, ax2]: ax.clear()
		ax2.set_title('Net')
		for ax in [ax1, ax2]: ax.set_ylabel('Result($)', fontsize=12)
		
		#generate 6 visualizations for figure
		if cType == 'step':
			ax1.step(viz_rng,b1)
			ax1.step(viz_rng,s1)
			ax2.step(viz_rng,net)
		elif cType == 'bar':
			ax1.bar(viz_rng,b1)
			ax1.bar(viz_rng,s1)
			ax2.bar(viz_rng,net)

		#dType decision
		if dType == 'option':	
			ax1.set_title('Long/Short', fontsize=12)
			for ax in [ax2]: ax.set_xlabel('Strike Price', fontsize=14)
		elif dType == 'tp':
			ax1.set_title('Over/Under', fontsize=12)
			for ax in [ax2]: ax.set_xlabel('Total Points' , fontsize=14)

	fig.suptitle("Real-Time Derivative Model", fontsize=16)

	#assign variable 'ani'; matplotlib's animation module, with 'dAnimate' function as an operator.
	ani = animation.FuncAnimation(fig, Animate2, interval=1000)

	plt.show()

#view2()
