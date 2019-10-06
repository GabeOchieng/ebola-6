import pandas as pd
import numpy as np
import dfebola as dfe
import fixdata as fx
import plotdata as pld


df = dfe.dfebola()


def is_country(str):

	'''Checks if str is a country in the study.'''

	country_list = list(df.Country.drop_duplicates())

	if str in country_list:
		return True
	else:
		return False


def help():

	'''Describes the commands of the program.'''

	h1 = "\n\tLegend:\n\n"
	h2 = "\t (c) = 'Cumulative number of confirmed Ebola cases'\n\t (d) = 'Cumulative number of confirmed Ebola deaths'\n\n"
	h3 = "\tList of commands:\n\n"
	h4 = "\t 'help': Shows this description.\n"
	h5 = "\t 'exit': Exits the program.\n"
	h6 = "\t 'list': Shows the list of countries.\n"
	h7 = "\t 'all': Dislays a bar chart showing the total number of cases and deaths per country.\n"
	h8 = "\t 'Country': Shows a graph displaying (c) and (d) for that country.\n"
	h9 = "\t   'Country c': Shows a graph displaying (c) for that country.\n"
	h10 = "\t   'Country d': Shows a graph displaying (d) for that country.\n"
	'''h11 = "\t   'CountryA, CountryB': Shows a graph displaying (c) and (d) for each country.\n"
	h12 = "\t   'CountryA, CountryB c': Shows a graph comapring CountryA (c) and CountryB (c).\n"
	h13 = "\t   'CountryA, CountryB d': Shows a graph comapring CountryA (d) and CountryB (d).\n"
	'''
	
	help_str = h1 + h2 + h3 + h4 + h5 + h6 + h7 + h8 + h9 + h10 #+ h11 + h12 + h13
	
	return help_str



def country_list():

	'''Returns a list containing the countries involved in the study.'''

	country_list = list(df.Country.drop_duplicates())
	country_list.pop(-1)
	country_list.pop(-1)
	country_list.sort()
	
	return country_list


def ctrys_bars():
  
 	'''Returns a chart bar of the total number of cases and deaths by countries.'''

 	return pld.ctrys_bars_plot()

	

def ctry_selected(str):

	'''Selects the right country command according to the input str.'''

	err_msg = "***Error: You entered an invalid command: "

	str_list = str.lower().split(' ')
	strCap = [i.capitalize() for i in str_list]
	ctry = ' '.join(strCap).replace("Of", "of")

	if ctry[-2:] == " C":
		ctry = ctry[:-2]

		if is_country(ctry):
			pld.plot_ebola_rates(fx.e_cases(ctry), ctry)	
		else:
			print(err_msg + ctry)
			return 0

	elif ctry[-2:] == " D":
		ctry = ctry[:-2]

		if is_country(ctry):
			pld.plot_ebola_rates(fx.e_deaths(ctry), ctry)	
		else:
			print(err_msg + ctry)
			return 0
	
	else:
		if is_country(ctry):
			pld.plot_ebola_c_and_d(fx.e_cases_and_deaths(ctry), ctry)
		else:
			print(err_msg + '"' + ctry + '"')
			return 0


