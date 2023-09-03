import pandas as pd
import requests
from bs4 import BeautifulSoup
from pandas import ExcelWriter
import csv
import openpyxl
import numpy

# url = "https://abiastate.gov.ng/legislature/"

# Declaring Input variables that will be used for processing
# Website to target
InputUrl = input("Enter Url :")

# Name of the file to be created where the scrapped data will be stored
doc = input("Enter Document Name :")
fileName = doc + '.xlsx'

print('Processing Data ')


# Action to send a get request to the website
response = requests.get(InputUrl)
# print(response.status_code)
soup = BeautifulSoup(response.text, 'html.parser')

# Specifying beautifulsoup to find all tables in the website
tables = soup.findAll('table')

data = pd.read_html(str(tables))

# print(data)
print('Writing Data to Excel')
with ExcelWriter(fileName) as writer:
    for i, df in enumerate(data):
        df.to_excel(writer,'sheet%s' % i)
    writer.save()

print('Data Processing Successful')
print("Data saved to", fileName)