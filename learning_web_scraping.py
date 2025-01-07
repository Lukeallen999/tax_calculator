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



# Need to come up with a way to split taxable income values 
# Need to rewrite this:


# Need to remove £ before creating upper and lower bands 
df['lower_limit'] = (df['Taxable income'].str.split(' ')).str[0]
df['upper_limit'] = (df['Taxable income'].str.split(' ')).str[-1]

# Removing £ and , from data
for i in ['£',',']:
    df['lower_limit'] = (df['lower_limit'].str.replace(i,''))
    df['upper_limit'] = (df['upper_limit'].str.replace(i,''))

df['lower_limit'] = (df['lower_limit'].str.replace('Up','0'))
df['lower_limit'] = (df['lower_limit'].str.replace('over','9999999999'))

df['lower_limit'] = df['lower_limit'].astype(int)
df['upper_limit'] = df['upper_limit'].astype(int)
print(df)
print('')
for i in range(0,len(df)):

    lower_limit = df.iloc[i,4]
    upper_limit = df.iloc[i,5]

    if lower_limit > upper_limit:
        df.iloc[i,4] = upper_limit
        df.iloc[i,5] = lower_limit


print(df)
