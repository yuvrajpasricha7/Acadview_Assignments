#Q1

import requests
response=requests.get('https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en')
d1=response.json()
print(d1['quoteText'])