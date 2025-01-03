from bs4 import BeautifulSoup
import requests
import bs4

page_to_be_scraped = 'https://www.gov.uk/income-tax-rates'

data = requests.get(page_to_be_scraped)

soup = BeautifulSoup(data.content, 'html.parser')

s = soup.find('div', class_='gem-c-govspeak govuk-govspeak gem-c-govspeak--direction-ltr js-disable-youtube govuk-!-margin-bottom-0')
content = soup.find_all('table')
table = soup.find_all('table')[0]
rows = soup.find_all('td')
rows2 = soup.find_all('th')
#print(content)
print('')
print('')
print(table)
print('')
print(rows[0])
print('')
print(rows)
print('')
print(rows2)
'''
for i in range(0,len(rows2)-1):
    print(f'{i} = {rows2[i]}')
'''