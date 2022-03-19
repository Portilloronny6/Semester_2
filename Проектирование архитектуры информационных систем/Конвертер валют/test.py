import requests

from currency import convert

amount = 1000
cur_from = 'RUB'
cur_to = 'USD'
date = '20/03/2022'

result = convert(amount, cur_from, cur_to, date, requests)

print(f'{amount} {cur_from} to {cur_to} => {result} {cur_to}')