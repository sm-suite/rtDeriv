#A1 import packages
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
plt.style.use(['ggplot'])
plt.style.use(['seaborn-deep'])
import matplotlib.animation as animation
import time


ro = lambda x : round(x, ndigits=2)



def view2():

	#B initialize figure, add subplots
	fig = plt.figure(figsize=(10, 3))
	ax1, ax2 = fig.add_subplot(121), fig.add_subplot(122)
	mycmap = plt.get_cmap('RdYlGn')


	def Animate2tp(i):
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
		trisk = abs(min(b1)) + abs(min(s1))
		roi = [(val/trisk)*100 for val in net]

		#format subplots in figure
		for ax in [ax1, ax2]: ax.clear()
		ax2.set_title('Net', fontsize=12)
		ax1.set_xticks([])
		for ax in [ax1, ax2]: ax.set_ylabel('Result($)', fontsize=12)
		
		#generate 6 visualizations for figure

		ax1.plot(viz_rng,b1, 'C4--', color='g')
		ax1.plot(viz_rng,s1, 'C6--', color='r')
		ax1.stem(viz_rng,roi, linefmt='None', markerfmt='yv--', use_line_collection=True)

		
		ax2.stem(viz_rng,b1, linefmt='None', markerfmt='gP', use_line_collection=True)
		ax2.stem(viz_rng,s1, linefmt='None', markerfmt='r_', use_line_collection=True)
		ax2.bar(viz_rng,roi, color='yellow')
		
		ax1.set_title('Over/Under', fontsize=12)
		for ax in [ax2]: ax.set_xlabel('Total Points' , fontsize=14)

	fig.suptitle("Over/Under/Net", fontsize=14)

	#assign variable 'ani'; matplotlib's animation module, with 'dAnimate' function as an operator.
	ani = animation.FuncAnimation(fig, Animate2tp, interval=1000)

	plt.show()

#view2()

