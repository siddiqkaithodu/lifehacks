Need to read CSV and EXCEL files then try this automation script that uses the Pandas module famous for its data science functions. Below you can find methods and functions that you will mostly need.

This script is very handy when you need to read Excel or CSV files for a project or need to parse some specific data programmatically.

# Read Excel and CSV
# pip install pandas
import pandas as pd
# <==Read CSV Files==>
csv = pd.read_csv('test.csv')
# read csv file with specific columns
csv = pd.read_csv('test.csv', usecols=['col1', 'col2'])
# Fetch only first 5 rows
csv = pd.read_csv('test.csv', nrows=5)
# Convert CSV to List
csv = pd.read_csv('test.csv').values.tolist()
# Read specific Col and row
csv = pd.read_csv('test.csv', usecols=['col1', 'col2'], nrows=5)
# <==Read Excel Files==>
excel = pd.read_excel('test.xlsx')
# read excel file with specific columns
excel = pd.read_excel('test.xlsx', usecols=['col1', 'col2'])
# Fetch only first 10 rows
excel = pd.read_excel('test.xlsx', nrows=10)
# Drop first row
excel = pd.read_excel('test.xlsx', skiprows=1)
# Convert Excel to List
excel = pd.read_excel('test.xlsx').values.tolist()
