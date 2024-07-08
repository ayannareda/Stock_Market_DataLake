import pandas as pd
import requests
from datetime import datetime

# Access Key
myAccessKey = "2K1QLHCNPHLGX8SC"

# Top 10 Companies by Market Cap {as of 06 Jul 2024}
topCompanies = {'Reliance' : 'RELIANCE.BSE',
'TCS' : 'TCS.BSE',
'HDFC Bank' : 'HDFCBANK.BSE',
'ICICI Bank' : 'ICICIBANK.BSE',
'Bharti Airtel' : 'BHARTIARTL.BSE',
'SBI' : 'SBIN.BSE',
'Infosys' : 'INFY.BSE',
'LIC India' : 'LICI.BSE',
'HUL' : 'HINDUNILVR.BSE',
'ITC' : 'ITC.BSE'}

# Empty Pandas DF
DF = pd.DataFrame(columns=['Date', 'Company', 'Open', 'Close', 'High', 'Low', 'Volume'])

# Loop over top companies Dict
for company, symbol in topCompanies.items():
    # Create API URL
    apiURL = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={myAccessKey}&outputsize=full'
    
    # Check response
    response = requests.get(apiURL)

    # return if status code is not 200 {failed}
    if response.status_code != 200:
        print(f"Failed to fetch data for {symbol}. HTTP Status code: {response.status_code}")
        continue

    # Load content in json
    content = response.json()

    # Get data from json
    daily_data = content["Time Series (Daily)"]

    # Empty Array to store data for a company
    records = []

    # Loop over all json rows
    for date, values in daily_data.items():
        # Check if date is between Jan 1, 2020 to May 31, 2024
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        if (datetime(2020, 1, 1) <= date_obj <= datetime(2024, 5, 31)):
            records.append({
                'Date': date,
                'Company': company,
                'Open': float(values['1. open']),
                'High': float(values['2. high']),
                'Low': float(values['3. low']),
                'Close': float(values['4. close']),
                'Volume': int(values['5. volume'])
                })
    
    # Load records in a temp DF
    tempDF = pd.DataFrame(records)

    # Append tempDF to original DF
    DF = pd.concat([DF, tempDF], ignore_index=True)

# Write DF
DF.to_csv('historical_data.csv', index=False)