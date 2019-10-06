import dfebola as dfe
import numpy as np 
import command as cm

df = dfe.dfebola()

def shorten_lists(valLst, dateLst):

	'''Shortens both lists up to the index where 'valLst' stops getting bigger plus the four next values.'''

	n = 0

	for i in range(len(valLst) -1, -1, -1):
		if valLst[i - 1] < valLst[i]:
			n = i
			break

	listA = valLst[: n + 4]
	listB = dateLst[: n + 4]

	return(listA, listB)



def fix_dicts(lst):

	'''Prepares data to be plotted: makes the cases and deaths dics of the same length'''

	dic_c = lst[0]
	dic_d = lst[1]

	#Final dictionary
	dic_f = {}

	c_keys = list(dic_c.keys())
	d_keys = list(dic_d.keys())

	## Making both list equal length
	# Add to d_keys the items (dates) that are missing from c_keys
	for i in range(len(c_keys)):
		if c_keys[i] not in d_keys:
			d_keys.append(c_keys[i])

	d_keys.sort()

	#Set first key:value for dic_f 
	if dic_d.get(d_keys[0]) == None:
		dic_f[d_keys[0]] = 0
	else:
		dic_f[d_keys[0]] = dic_d[d_keys[0]]

	# The key:value pairs are passed to dic_f. If a given key has no value,
	# the value of the previous key (item in d_keys) is passed.
	for i in range(1, len(d_keys)):
		if dic_d.get(d_keys[i]):
			dic_f[d_keys[i]] = dic_d[d_keys[i]]
		else:	
			dic_f[d_keys[i]] = dic_f[d_keys[i-1]]


	### Passes the missing key:value to dic_c from dic_f. 
	if (len(dic_c) < len(dic_f)):

		dic_c_keys = list(dic_c.keys())
		dic_f_keys = list(dic_f.keys())

		for i in range(len(dic_f)):
			if (dic_f_keys[i] not in dic_c_keys):
				dic_c[dic_f_keys[i]] = dic_c[dic_c_keys[-1]] 

	return([dic_c, dic_f])



def e_cases(str):

	'''Returns a dictionary holding dates as keys and number of cases as values'''

	dic = {str : 'cases'}

	country = df[df.Country == str]

	cases = country[country.Indicator == 'Cumulative number of confirmed Ebola cases']
	cases2 = cases.sort_values(by=['Date'], ascending= True)

	dates = np.array(cases2.Date)
	values = np.array(cases2.value)

	short_list_values, short_list_dates = shorten_lists(values, dates)

	for d, v in zip(short_list_dates, short_list_values):
		dic[d] = v

	return dic


def e_deaths(str):

	'''Returns a dictionary holding dates as keys and number of cases as values'''

	dic = {str : 'deaths'}

	country = df[df.Country == str]

	deaths = country[country.Indicator == 'Cumulative number of confirmed Ebola deaths']
	deaths2 = deaths.sort_values(by=['Date'], ascending= True)

	dates = np.array(deaths2.Date)
	values = np.array(deaths2.value)

	short_list_values, short_list_dates = shorten_lists(values, dates)

	for d, v in zip(short_list_dates, short_list_values):
		dic[d] = v

	return dic


def e_cases_and_deaths(str):

	'''Returns a list holding two dictionaries: 1st cases, 2nd deaths.'''
	
	lst = [e_cases(str), e_deaths(str)]
	fixed_list = fix_dicts(lst)

	return fixed_list


def max_values():

	'''Returns two dictionary: one, the max number of cases per country, the second, the max number of deaths per country '''

	ctrys = cm.country_list()

	dic_c = {}
	dic_d = {}

	for i in ctrys:
		tc = e_cases(i)
		td = e_deaths(i)

		del tc[i]
		del td[i]
		dic_c[i] = max(tc.values())
		dic_d[i] = max(td.values())
	
	return dic_c, dic_d

