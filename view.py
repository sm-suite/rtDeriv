#A1 import packages
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

#A2 define 'ro' and 'typ3'
ro = lambda x : round(x, ndigits=2)
typ3 = 'tp'
#typ3 = 'option'

#B initialize figure, add 6 subplots
fig = plt.figure(figsize=(8, 6))
ax1, ax2 = fig.add_subplot(321), fig.add_subplot(322)
ax3, ax4 = fig.add_subplot(323), fig.add_subplot(324)
ax5, ax6 = fig.add_subplot(325), fig.add_subplot(326)

fig.suptitle("Real-Time Derivative Model", fontsize=16)

#view function
def dAnimate(i):
	pullData = open("b1results.txt","r").read()#c -1
	pullData1 = open("s1results.txt", "r").read()# c -2
	dataArray = pullData.split('\n')
	dataArray1 = pullData1.split('\n')

	global net
	pts, net, b1, s1 = [], [], [], []
	for eachLine in dataArray:
		if len(eachLine)>1:
			x,y = eachLine.split(',')
			pts.append(float(x))
			b1.append(float(y))
	for eachLine in dataArray1:
		if len(eachLine)>1:
			j,b = eachLine.split(',')
			s1.append(float(b))
	

	zipped_rez = zip(b1, s1)
	net = [x+y for (x,y) in zipped_rez]
	bcs, wcs = ro(max(net)), ro(min(net))




	for ax in [ax1, ax2, ax3, ax4, ax5, ax6]: ax.clear()
	for ax in [ax1, ax3, ax5]: ax.set_ylabel('Result($)', fontsize=12)
	for ax in [ax1, ax2, ax3, ax4]: ax.set_xticks([])
	ax2.set_title("Net \n " + "BCS: $" + str(bcs), fontsize=12)
	ax4.set_title("WCS: $" + str(wcs), fontsize=12)
	ax1.step(pts,b1)
	ax1.step(pts,s1)
	ax2.step(pts,net)
	ax3.bar(pts,b1)
	ax3.bar(pts,s1)
	ax4.bar(pts,net)
	ax5.fill(pts,b1)
	ax5.fill(pts,s1)
	ax6.fill(pts,net)



	if typ3 == 'option':	
		for ax in [ax5, ax6]: ax.set_xlabel('Strike Price', fontsize=14)
		ax1.set_title('Long/Short', fontsize=12)

	elif typ3 == 'tp':
		ax1.set_title('Over/Under', fontsize=12)
		for ax in [ax5, ax6]: ax.set_xlabel('Total Points', fontsize=14)


#assign variable 'ani'; matplotlib's animation module, with 'dAnimate' function as an operator.
ani = animation.FuncAnimation(fig, dAnimate, interval=1000)

plt.show()


