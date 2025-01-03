from bs4 import BeautifulSoup
import requests

page_to_be_scraped = 'https://www.gov.uk/income-tax-rates'

data = requests.get(page_to_be_scraped)

soup = BeautifulSoup(data.content, 'html.parser')

s = soup.find('div', class_='gem-c-govspeak govuk-govspeak gem-c-govspeak--direction-ltr js-disable-youtube govuk-!-margin-bottom-0')
content = soup.find_all('table')
table = soup.find_all('table')[0]
rows = table.find_all('tr')
print(content)
print('')
print(table)
print('')
print(rows)