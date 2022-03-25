import requests

from currency import convert

amount = 1
cur_from = 'USD'
cur_to = 'RUB'
date = '20/03/2022'

if __name__ == '__main__':
    result = convert(amount, cur_from, cur_to, date, requests)
    print(f'{amount} {cur_from} to {cur_to} => {result} {cur_to}')
