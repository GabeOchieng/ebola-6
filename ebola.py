#!/usr/bin/env python

'''

Author:         Jorge Martin Joven
Date:           Oct 6, 2019
Description:    Using the data from https://www.kaggle.com/kingburrito666/ebola-cases, this program displays graphs showing the
                cumulative Ebola cases and deaths on the affected countries of the 2014-2016 Ebola outbreak.
                 
'''
import command as cm

def main():

	print("\n\tThis program visualizes data on the 2014-2016 Ebola outbreak.\n")
	print("\t(Data source: https://www.kaggle.com/kingburrito666/ebola-cases)\n")
	print(cm.help())

	while True:
		answer = input('\nEnter command: ')
		
		if answer.lower() == 'help':
			print(cm.help())

		elif answer.lower() == 'list':
			for i in cm.country_list():
				print( '\t' + i)
	
		elif answer.lower() == 'all':
			
			cm.ctrys_bars()

		elif answer.lower() == 'exit':
			break
			
		else:
			print(cm.ctry_selected(answer))
			


if __name__ == '__main__':
	main()