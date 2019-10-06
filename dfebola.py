import pandas as pd 

def dfebola():

	'''Creates a pandas dataframe from the ebola.csv file'''

	df = pd.read_csv(r'ebola.csv')

	return df