# first import the request package
import requests
#import Json to handle file from api
import json

#https://openexchangerates.org/api/latest.json?app_id=YOUR_APP_ID

# get data from api using the request package and open exchange URL

response = requests.get("https://openexchangerates.org/api/latest.json?app_id=09f89dfa41154f3099316b1bb3002a2f")

# converting exchange rate data from api to json file a dictionary

exchange_rates =  response.json()

#get currency code list

with open(r"C:\Users\Emmanuel Soetan\Documents\Python projects\Currency converter\currencies_code.txt","r") as f:
    currency_code_list = [line.strip() for line in f.readlines()] 
    
#fix base currency
base_currency = input("Please Enter your base currency ISO code ")

#amount to be converted
currency_amt = int(input("Please Enter amount to be converted "))

#convert base currency to dollar since open exchange base currency is dollars
if base_currency in currency_code_list:
    currency_amt_in_dollar = currency_amt // exchange_rates["rates"][base_currency]
    print(f'Your base currency in USD is {currency_amt_in_dollar} USD')
else:
    pass

#fixed currency to be converted to 
to_currency = input("Please Enter currency ISO CODE you are converting to ")

#check if the currency code exits
if to_currency in currency_code_list:
    
    #execute if the currency code exist
    conversion = currency_amt_in_dollar * exchange_rates["rates"][to_currency]
    print(f'{currency_amt} {base_currency} is {conversion} {to_currency}')
    
else:
    conversion = currency_amt * exchange_rates["rates"][to_currency]
    print(f'{currency_amt} USD is {conversion} {to_currency}')






