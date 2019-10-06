import matplotlib.pyplot as plt
import math
import numpy as np
from fixdata import max_values


def plot_ebola_rates(dic, country):

	'''Creates a graph using the dictionary keys in x-axis and values in y-axis.'''

	#Create lists of dates and values
	z = dic.pop(country)
	dates = list(dic.keys())
	values = list(dic.values())

	#Creates a subplot for the figure 
	ax = plt.subplot(1, 1, 1)

	#Makes sure the values (y-axis) are shown as integers
	ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True)) 

	#Sets the y-axis (values) when the cases/deaths are constant.
	if(values[-1] - values[0] == 0 ):
		plt.ylim(bottom=0, top=(values[-1] + 1))
	
	#Sets the number of dates shown in the x-axis and plots the graph.
	if (len(dates) < 20):
		ax.xaxis.set_major_locator( plt.MaxNLocator( len(dates) ) )
		plt.plot_date(dates, values, '-o', xdate=True)

	elif (len(dates) >= 20) and (len(dates) < 100):
		ax.xaxis.set_major_locator( plt.MaxNLocator(20) )
		plt.plot(dates, values, '-')

	elif (len(dates) >= 200):
		ax.xaxis.set_major_locator( plt.MaxNLocator( math.floor( len(dates)/20 ) ) )
		plt.plot(dates, values, '-')

	#Layout of the x-axis
	plt.xticks(rotation=60, fontsize = 8)
	plt.subplots_adjust(bottom=0.25)

	#Extra-info for the graph
	plt.title( country + ': Cumulative ebola ' + z)
	plt.xlabel('dates ( yyyy-mm-dd )')
	plt.ylabel('number of ' + z)
	plt.grid(linestyle = ':')
	
	plt.show()


def plot_ebola_c_and_d(lst, country):

	'''Display a graph showing ebola cases and deaths for the input country.'''

	#Creates lists of dates and values from each dictionary
	dic1 = lst[0]
	n = dic1.pop(country)
	dates1 = list(dic1.keys())
	cases = list(dic1.values())

	dic2 = lst[1]
	m = dic2.pop(country)
	dates2 = list(dic2.keys())
	deaths = list(dic2.values())

	#Creates a subplot for the figure 
	ax = plt.subplot(1, 1, 1)

	#Makes sure the values (y-axis) are shown as integers and plots the graph
	ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))

	#Sets the number of dates shown in the x-axis
	if (len(dates1) < 20):
		ax.xaxis.set_major_locator( plt.MaxNLocator( len(dates1) ) )
		plt.plot(dates1, cases, '-o', label='cases')
		plt.plot(dates1, deaths, '-x', label='deaths', color='red')

	elif (len(dates1) >= 20) and (len(dates1) < 100):
		ax.xaxis.set_major_locator( plt.MaxNLocator(20) )
		plt.plot(dates2, cases, '-', label='cases')
		plt.plot(dates2, deaths, '-', label='deaths', color='red')

	elif (len(dates1) >= 200):
		ax.xaxis.set_major_locator( plt.MaxNLocator( math.floor( len(dates1)/20 ) ) )
		plt.plot(dates2, cases, '-', label='cases')
		plt.plot(dates2, deaths, '-', label='deaths', color='red')

	#Layout of the x-axis
	plt.xticks(rotation=60, fontsize=8)
	plt.subplots_adjust(bottom=0.25)

	#Extra-info for the graph
	plt.title( country + ': Cumulative ebola cases & deaths' )
	plt.xlabel('dates ( yyyy-mm-dd )')
	plt.ylabel('ammount')
	plt.legend()
	plt.grid(linestyle = ':')

	plt.show()


def ctrys_bars_plot():

	'''Shows a bar chart on the total number of cases and deaths per country.'''

	d_cases, d_deaths = max_values()
	
	#Getting y-axis data
	v_cases = list(d_cases.values())
	v_deaths = list(d_deaths.values())

	#Getting x-axis data
	ctrys = list(d_cases.keys())

	#Acronyms of some countries to better fit the chart
	for n, i in enumerate(ctrys):
		if (i == "United States of America"):
			ctrys[n] = "USA"
		elif (i == "United Kingdom"):
			ctrys[n] = "UK"

	#Showing values on top of each bar
	for a,b in enumerate(v_cases):
		plt.text(a-0.2, b, str(b), fontsize=8, rotation=60, color='blue')

	for i,v in enumerate(v_deaths):
		plt.text(i+0.1, v, str(v), fontsize=8, rotation=60, color='red')

	#Creates the sequence of scalars for the x-axis.
	x_pos = np.arange(len(ctrys))

	#Create the bat chart
	plt.bar(x_pos-0.15, v_cases, width=0.3, align='center', color='blue', label='Cases')
	plt.bar(x_pos+0.15, v_deaths, width=0.3, align='center', color='red', label='Deaths')

	#Setting x and y axis
	plt.xticks(x_pos, ctrys, rotation=60)
	plt.ylim(top=10000)

	#Setting the bottom margin
	plt.subplots_adjust(bottom=0.25)

	#Additional information
	plt.ylabel('Total')
	plt.title('Ebola cases per country 2014-2016')
	plt.legend()

	plt.show()

	
   

  