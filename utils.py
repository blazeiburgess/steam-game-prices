from random import randint, random
from time import sleep
from re import search


def random_sleep(min_: int, max_: int):
    sleep_time = randint(min_,max_) + random()
    sleep(sleep_time)

def _convert_commas_to_periods_in_money(money_text):
    broken = money_text.replace(',','.').split('.')
    return "".join(broken[:-1]) + "." + broken[-1]

def parse_float(text: str) -> float:
    if text.lower().strip() in ('free to play', 'free', 'play for free!'):
        return 0
    elif text.count(',') > 1:
        return float(search(r'\d{1,}[\d,.]*',text).group(0).replace(',',''))
    elif text.count(',') == 1:
        return float(search(r'\d{1,}[\d,.]*',_convert_commas_to_periods_in_money(text)).group(0))
    else:
        try:
            return float(search(r'\d{1,}[\d.]*',text).group(0))
        except AttributeError as ae:
            raise AttributeError(f'{ae}: {text}')
