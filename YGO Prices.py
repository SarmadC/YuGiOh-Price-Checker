import requests
import pandas as pd
import time
import openpyxl 

df = pd.read_excel("Your Excel file with print tags.xlsx", usecols=['print_tag'])  

# pd.read_excel

def get_tag(print_tag):
    request = requests.get(
        'http://yugiohprices.com/api/price_for_print_tag/' + print_tag)
    time.sleep(1)  # sleep for a second to prevent sending too many API calls per minute
    return request.json()

df['result'] = df['print_tag'].apply(get_tag)

df2 = pd.json_normalize(df['result'])
df2.to_excel('Output name of file.xlsx')
