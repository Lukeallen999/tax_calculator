from bs4 import BeautifulSoup
import requests
import pandas as pd
from io import StringIO

def get_tax_table() -> pd.DataFrame:
    '''
    1) Trys to get the html from the tax page on the UK government website
    2) Reads the HTML and outputs the table that outlines the tax rates
    3) Puts the data into a pandas DataFrame 
    '''

    try:
        url = 'https://www.gov.uk/income-tax-rates'
        response = requests.get(url)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print(f'ERROR fetching the webpage: {e}')
        raise e

    try:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find_all("table")[0]
        tax_table_df = pd.read_html(StringIO(str(table)))[0]

    except Exception as e:
        print(f'ERROR parsing the HTML or reading the table: {e}')
        raise e

    return(tax_table_df)

def clean_tax_table(tax_table_df : pd.DataFrame) -> pd.DataFrame:
    '''
    1) Converts the "Tax rate" column from percentage to decimal
    2) Splits the "Taxable income" column and creates upper and lower limit columns 
    3) Removes unneeded characters
    4) converts the datatype to int
    5) checks that the lower limit is lower than the upper limit 
    '''
    try:
        tax_table_df['tax_rate_decimal'] = ((tax_table_df['Tax rate'].str.replace('%','')).astype(float)) * 0.01
    
    except Exception as e:
        print(f'ERROR converting "Tax Rate" column to decimal: {e}')

    try:
        tax_table_df['lower_limit'] = (tax_table_df['Taxable income'].str.split(' ')).str[0]
        tax_table_df['upper_limit'] = (tax_table_df['Taxable income'].str.split(' ')).str[-1]

        for i in ['£',',']:
            tax_table_df['lower_limit'] = (tax_table_df['lower_limit'].str.replace(i,''))
            tax_table_df['upper_limit'] = (tax_table_df['upper_limit'].str.replace(i,''))

        tax_table_df['lower_limit'] = (tax_table_df['lower_limit'].str.replace('Up','0'))
        tax_table_df['lower_limit'] = (tax_table_df['lower_limit'].str.replace('over','9999999999'))

        tax_table_df['lower_limit'] = tax_table_df['lower_limit'].astype(int)
        tax_table_df['upper_limit'] = tax_table_df['upper_limit'].astype(int)

        for i in range(0,len(tax_table_df)):

            lower_limit = tax_table_df.iloc[i,4]
            upper_limit = tax_table_df.iloc[i,5]

            if lower_limit > upper_limit:
                tax_table_df.iloc[i,4] = upper_limit
                tax_table_df.iloc[i,5] = lower_limit
    except Exception as e:
        print(f'ERROR creating Lower/Upper limits: {e}')    
        raise e
    
    return tax_table_df