# income
'''
- User defined input 
- float to 2 dp
'''

# income tax
'''
Website: https://www.gov.uk/income-tax-rates
- Percentage depends on income (after pension)
- float to 2 dp 
- do not get personal allowance if earning more than £125,140.
'''

# national insurance
'''
Website: https://www.gov.uk/national-insurance-rates-letters
- Percentage depends on income (after pension)
- float to 2 dp 
'''

# pension
'''
- User defined input 
- percentage
- calculated before tax 
'''

# Student loan
'''
Website: https://www.gov.uk/repaying-your-student-loan/what-you-pay
- Percentage depends on income (after pension)
- float to 2 dp 
- depends on loan plan
'''
# Bonus
'''
- No Tax relief
- Doesn't add to pension 
'''



'''
1) Calculates amount paid in tax
2) Amount after tax
3) amount added to pension
4) pension amount when getting to retirement stage
5) student loan vs amount paid off per year graph
    a) interest on the loan
    b) how many years till you pay it back
    C) ask if they make any voluntary contribution 

- Add option to pick between average monthly,yearly,weekly salary
Possible breaks:
- If the Urls change
- If the names of the columns change
- if over is change

Why I made this:
I mainly made this to practice Webscraping 
#######################################################################

from bs4 import BeautifulSoup
import requests
import pandas as pd
from io import StringIO

try:
   url = 'https://www.gov.uk/income-tax-rates'
   response = requests.get(url)
   response.raise_for_status()

except requests.exceptions.RequestException as e:
   print(f"Error fetching the webpage: {e}")

try:
   soup = BeautifulSoup(response.content, "html.parser")

   table = soup.find_all("table")[0]

   df = pd.read_html(StringIO(str(table)))[0]

except Exception as e:
   print(f"Error parsing the HTML or reading the table: {e}")

print(df)
'''

