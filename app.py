from flask import Flask, render_template, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes
from forex_python.bitcoin import BtcConverter
from currency_data import check_curr_code, get_curr_symbol

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

rates = CurrencyRates()
codes = CurrencyCodes()
btc = BtcConverter()

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/convert")
def convert_route():
    from_curr = request.args["from"]
    to_curr = request.args["to"]
    raw_amount = request.args["amount"]

    if check_curr_code(from_curr) == False:
        flash(f"Invalid Currency Code!! - {from_curr}")
        return redirect("/")

    if check_curr_code(to_curr) == False:
        flash(f"Invalid Currency Code!! - {to_curr}")
        return redirect("/")

    try:
        amount = float(raw_amount)
    except:
        flash(f"Invalid Currency Amount!! - {raw_amount}")
        return redirect("/")
    
    symbol = get_curr_symbol(to_curr)

    raw_result = rates.convert(from_curr, to_curr, amount)
    result = round(raw_result, 2)

    return render_template("/convert.html", result=result, symbol=symbol)