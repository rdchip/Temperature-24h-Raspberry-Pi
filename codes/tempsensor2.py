# python 
import Adafruit_DHT
import time
import psutil
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import style
from datetime import datetime
import sys
import os.path
import csv

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 25
window = 24 # number of hours
t_start = time.time()/3600
x,y = [],[]
tiks = [0,0,0,0,0,0]

#------------style ------
plt.style.use("seaborn-dark")
for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
	plt.rcParams[param] = '#212946' # bluish dark grey
for param in ['text.color','axes.labelcolor','xtick.color','ytick.color']:    
	plt.rcParams[param] = '0.9' # very light grey
#-------------------------
fig = plt.figure()
ax = fig.add_subplot(111)
plt.grid(color='#2A3459')
ax.set_ylim(10,30)
ax.tick_params(axis='y',labelsize=15)
ax.set_xticklabels(['1d','-20h','-16h','-12h','-8h','-4h','Now'],fontsize=15)

def read_old_data():
	if os.path.isfile("text.csv"):
		graph_data = open('text.csv','r').read()
		lines = graph_data.split('\n')
		for line in lines:
			if len([num for num, index in enumerate(line) if index == '.']) == 2:  #--- update -
				xs,ys = line.split(',')
				if ys.strip():
					x.append(float(xs))
					y.append(float(ys))
					pre_ys = ys
					pre_xs = xs #--- update -
				else:
					x.append(float(xs))
					y.append(float(pre_ys))
			else:							#--- update -
				x.append(float(pre_xs))
				y.append(float(pre_ys))

def animate(i):
	humidity, temp = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
	mytime = time.asctime(time.localtime(time.time()))
	t = time.time()/3600
	if temp is None or humidity is None:
		temp_str = "--"
		humi_str = "--"
		temp = y[len(y)-1]
		temp = round(temp,1)#--- update -
	else:
		temp = round(temp,1)
		humidity = round(humidity,1)
		temp_str = str(temp)
		humi_str = str(humidity)
	#print("t={0}, t_start={1}, xlen={2}, FuncAnimation={3}".format(t,t_start + 24,len(x),sys.getsizeof(FuncAnimation)))
	if len(x) < 1440: 
		x.append(t)
		y.append(temp)
	else:
		x.append(t)
		y.append(temp)
		x.pop(0)
		y.pop(0)
	with open("text.csv","w") as f:
		writer=csv.writer(f,delimiter=',')
		writer.writerows(zip(x,y))
	ax.set_title("{0:s} Temp {1:s}$^\circ$C".format(mytime,temp_str),fontsize=15)
	ax.set_xlim(t-window, right=t)	
	ax.set_xticks(np.arange(t-window,t+1,4))
	ax.scatter(x,y, color='#FE53BB', s=2)
	fig.canvas.draw()

read_old_data()
ani = FuncAnimation(fig, animate, interval=60000)
plt.show()



