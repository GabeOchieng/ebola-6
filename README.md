# ebola
Visualization of the 2014-2016 Ebola outbreak cases.

INTRODUCTION:

This program visualizes the Ebola cases and deaths by countries of the 2014-2016 Ebola outbreak. It allows the user to select
the country and the kind of data (cases, deaths or both) to be shown.


OBJECTIVE:

The goal of this project is to offer a much clearer understanding of the progression of the disease in the affected countries. 
For this purpose, the data used in this project has been selected and adapted to accommodate the requirements of the libraries 
used to this end.


DATA SOURCE:

The data has been taken from https://www.kaggle.com/kingburrito666/ebola-cases. 


DATASET: 

The original dataset contains a series of indicators (see APPENDIX for full list) from which the following two has been used: 
*Cumulative number of confirmed Ebola cases;
*Cumulative number of confirmed Ebola deaths;

These two indicators have been selected because they are the confirmed cases, they offer the biggest ammount data for all affected
countries, and they allow to see the progression overtime.

The visualization of the data reveals some flaws in it (e.g. dropping in the cumulative number of certain cases or more deaths
than cases in certain countries). However, finding the explanation for these errors is beyond the purpose of this program.


FILE STRUCTURE:

There are six files in this program:

ebola.csv: contains the data.

ebola.py: contains the main function.

dfebola.py: creates a dataframe from ebola.csv.

command.py: contains the definition of the functions that are called when the user enters a command.

fixdata.py: contains the functions that prepare the data to be plotted.

plotdata.py: contains the functions to plot the data.


APPENDIX:

List of indicators in ebola.csv:

Case fatality rate (CFR) of confirmed Ebola cases

Case fatality rate (CFR) of confirmed, probable and suspected Ebola cases

Case fatality rate (CFR) of probable Ebola cases

Case fatality rate (CFR) of suspected Ebola cases

*Cumulative number of confirmed Ebola cases

*Cumulative number of confirmed Ebola deaths

Cumulative number of confirmed, probable and suspected Ebola cases

Cumulative number of confirmed, probable and suspected Ebola deaths

Cumulative number of probable Ebola cases

Cumulative number of probable Ebola deaths

Cumulative number of suspected Ebola cases

Cumulative number of suspected Ebola deaths

Number of confirmed Ebola cases in the last 21 days

Number of confirmed Ebola cases in the last 7 days

Number of confirmed Ebola deaths in the last 21 days

Number of confirmed, probable and suspected Ebola cases in the last 21 days

Number of probable Ebola cases in the last 21 days

Number of probable Ebola cases in the last 7 days

Number of probable Ebola deaths in the last 21 days

Number of suspected Ebola cases in the last 21 days

Number of suspected Ebola cases in the last 7 days

Number of suspected Ebola deaths in the last 21 days

Proportion of confirmed Ebola cases that are from the last 21 days

Proportion of confirmed Ebola cases that are from the last 7 days

Proportion of confirmed Ebola deaths that are from the last 21 days

Proportion of confirmed, probable and suspected Ebola cases that are from the last 21 days

Proportion of confirmed, probable and suspected Ebola cases that are from the last 7 days

Proportion of confirmed, probable and suspected Ebola deaths that are from the last 21 days

Proportion of probable Ebola cases that are from the last 21 days

Proportion of probable Ebola cases that are from the last 7 days

Proportion of probable Ebola deaths that are from the last 21 days

Proportion of suspected Ebola cases that are from the last 21 days

Proportion of suspected Ebola cases that are from the last 7 days

Proportion of suspected Ebola deaths that are from the last 21 days

