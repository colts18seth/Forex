from forex_python.converter import CurrencyRates, CurrencyCodes
from forex_python.bitcoin import BtcConverter

cr = CurrencyRates()
cc = CurrencyCodes()
b = BtcConverter()

dict_file = open("codes.txt")
codes = [w.strip() for w in dict_file]
dict_file.close()

def check_curr_code(curr_code):
    if curr_code in codes:
        return True
    return False

def get_curr_symbol(curr_code):
    symbol = cc.get_symbol(curr_code)
    return symbol