import re


class BankRussiaError(Exception):
    def __init__(self, message):
        super().__init__(message)


class ConverterError(BankRussiaError):
    pass


def convert(amount, cur_from, cur_to, date, requests):
    try:
        response = requests.get(f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}')

        # Si hay algún problema, se lanzará una excepción!
        response.raise_for_status()
    except requests.exceptions.RequestException:
        raise BankRussiaError('Невозможно установить связь с Банком России')

    cur_from = cur_from.upper()
    cur_to = cur_to.upper()

    response = response.text
    currencies = re.findall('[A-Z]{3}', response)
    values = re.findall('[0-9]+,[0-9]+', response)
    nominals = re.findall('<Nominal>[10]+', response)

    if not any([currencies, values, nominals]):
        raise ConverterError('Конвертация валюты невозможна!')

    currencies_info = {
        currency: float(values[index].replace(',', '.')) / int(nominals[index].split('<Nominal>')[1])
        for index, currency in enumerate(currencies)
        if currency == cur_from or currency == cur_to
    }

    if cur_from == "RUB":
        return round(amount / currencies_info.get(cur_to), 4)

    if cur_to == 'RUB':
        return round(amount * currencies_info.get(cur_from), 4)

    factor = currencies_info.get(cur_from) / currencies_info.get(cur_to)

    return round(amount * factor, 4)
