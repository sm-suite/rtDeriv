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
	def AniRoi(i):
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
		for ax in [ax1, ax2]: ax.clear()
		ax1.stem(viz_rng,sroi, linefmt='None', markerfmt='r_--', use_line_collection=True)		
		ax1.stem(viz_rng,broi, linefmt='None', markerfmt='g+--', use_line_collection=True)
		ax1.plot(viz_rng,broi, 'C7o', alpha=0.5)
		ax1.plot(viz_rng,sroi, 'C6o', alpha=0.5)
		ax2.stem(viz_rng,roi, linefmt='yellow', markerfmt='bv--', use_line_collection=True)
		for ax in [ax1, ax2]: ax.set_ylabel("ROI(%)", fontsize=12)
		ax1.set_title("Buy/Sell", fontsize=12)
		ax2.set_title("Net", fontsize=12)
		for ax in [ax1, ax2]: ax.set_xlabel('Strike Price', fontsize=12)
	fig.suptitle("ROI Model", fontsize=14)
	ani = animation.FuncAnimation(fig, AniRoi, interval=1000)
	plt.show()




def buysell():
	fig = plt.figure(figsize=(10, 4))
	ax1, ax2 = fig.add_subplot(121), fig.add_subplot(122)
	def Anibs(i):
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
		for ax in [ax1, ax2]: ax.clear()
		ax1.stem(viz_rng,b1, linefmt='green', markerfmt='gv--', use_line_collection=True)
		ax2.stem(viz_rng,s1, linefmt='red', markerfmt='rv--', use_line_collection=True)
		ax1.set_title('Buy', fontsize=12)
		ax2.set_title('Sell', fontsize=12)
		for ax in [ax1, ax2]: ax.set_xlabel('Strike Price' , fontsize=14)
		for ax in [ax1, ax2]: ax.set_ylabel('Return($)', fontsize=12)

	fig.suptitle("Buy & Sell Positions", fontsize=14)
	ani = animation.FuncAnimation(fig, Anibs, interval=1000)
	plt.show()


def overview():
	fig = plt.figure(figsize=(9, 9))
	ax1, ax2, ax3 = fig.add_subplot(321), fig.add_subplot(322), fig.add_subplot(323)
	ax4, ax5, ax6 = fig.add_subplot(324), fig.add_subplot(325), fig.add_subplot(326)
	def AniOverview(i):
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
		b1r, s1r, b1w, s1w = ro(abs(min(b1))), ro(abs(min(s1))), ro(max(b1)), ro(max(s1))
		ww, wl, lw = ro(b1w+s1w), ro(b1w-s1r), ro(s1w-b1r)
		wwr, wlr, lwr = ro((ww/trisk)*100), ro((wl/trisk)*100), ro((lw/trisk)*100)
		for ax in [ax1, ax2, ax3, ax4, ax5, ax6]: ax.clear()
		ax1.barh('Sell risk\n $' + str(s1r), s1r)		
		ax1.barh('Buy risk\n $' + str(b1r), b1r)
		ax2.barh('Sell\n return\n $' + str(s1w), s1w)
		ax2.barh('Buy\n return\n $' + str(b1w), b1w)
		ax3.barh('loss-win\n $' + str(lw), lw)
		ax3.barh('win-loss\n $' + str(wl), wl)
		ax3.barh('win-win\n $' + str(ww), ww)
		ax4.barh('loss-win\n %' + str(lwr), lwr)
		ax4.barh('win-loss\n %' + str(wlr), wlr)
		ax4.barh('win-win\n %' + str(wwr), wwr)
		ax5.stem(viz_rng,sroi, linefmt='None', markerfmt='rv-', use_line_collection=True)
		ax5.stem(viz_rng,broi, markerfmt='gv-', linefmt='None', use_line_collection=True)
		ax6.stem(viz_rng,roi, linefmt='yellow', markerfmt='bv--', use_line_collection=True)
		ax1.set_title("Risk($)", fontsize=12)
		ax2.set_title("Return($)", fontsize=12)
		ax3.set_title("Outcomes Net($)", fontsize=12)
		ax4.set_title("Outcomes ROI(%)", fontsize=12)
		ax5.set_title("Buy/Sell ROI(%)", fontsize=12)
		ax6.set_title("Net ROI(%)", fontsize=12)
		for ax in [ax5]: ax.set_ylabel('ROI(%)', fontsize=10)
		for ax in [ax1, ax2, ax3, ax4]: ax.set_xticks([])
		for ax in [ax5, ax6]: ax.set_xlabel('Strike Price', fontsize=14)

	fig.suptitle("Derivative Position", fontsize=16)
	ani = animation.FuncAnimation(fig, AniOverview, interval=1000)
	plt.show()


#overview()
#buysell()
#roi()