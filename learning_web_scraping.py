from bs4 import BeautifulSoup
import requests
import pandas as pd
from io import StringIO

url = 'https://www.gov.uk/income-tax-rates'
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
table = soup.find_all("table")[0]

df = pd.read_html(StringIO(str(table)))[0]

print('a')
print(df)

df['tax_rate2'] = ((df['Tax rate'].str.replace('%','')).astype(float)) * 0.01
print('')
print(df)



'''df['tax_rate2'] = df['Tax rate']
for i in ['%','0']:
    df['tax_rate2'] = (df['tax_rate2'].str.replace(i,''))
    #print(df)
df['tax_rate2'].astype(float) * 0.01'''

# Need to come up with a way to split taxable income values 

df['A'] = df['Taxable income'].str.split(' to ')

df['B'] = df['Taxable income'].str.split(' ')
# Need to remove £ before creating upper and lower bands 
df['C'] =  df['B'].str[0]
df['D'] =  df['B'].str[-1]
print(df)
# Need to come up with a way to split taxable income values 

