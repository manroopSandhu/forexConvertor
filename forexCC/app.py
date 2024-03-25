from flask import Flask, request, render_template, jsonify, session, flash, redirect
import requests
from currency_symbols import CurrencySymbols


app = Flask(__name__)
app.config["SECRET_KEY"] = "abc123"
url = 'http://api.exchangerate.host/live?access_key=a9da0467564422cbdd55277852964965'


currencies = ['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 
 'BBD','BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTC', 'BTN', 'BWP', 
'BYN', 'BYR', 'BZD', 'CAD', 'CDF', 'CHF', 'CLF', 'CLP', 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 
'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 
'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 
'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 
'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 
'LVL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MUR', 'MVR', 'MWK', 
'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 
'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 
'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SRD', 'STD', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 
'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VEF', 'VND', 
'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMK', 'ZMW', 
'ZWL']



@app.route("/", methods=["GET", "POST"])
def homepage():
        if request.method == "POST":
            convert_from = request.form.get('converting-from')
            convert_to = request.form.get('converting-to')
            amount = request.form.get('amount')

            if convert_from not in currencies:
                flash(f"Sorry! {convert_from} is not a valid currency!")
                return redirect('/')
            elif convert_to not in currencies:
                flash(f"Sorry! {convert_to} is not a valid currency!")
                return redirect('/')
            elif amount.isnumeric() == False:
                 flash(f"Sorry! {amount} is not a valid number!")
                 return redirect('/')
                  

                  

            response = requests.get(url)
            data = response.json()

            first_amount = data[convert_from]
            second_amount = data[convert_to]

            result_not_rounded = (second_amount/first_amount)*float(amount)
            result = round(result_not_rounded, 2)

            symbol = CurrencySymbols.get_symbol(convert_to)

            currency_results = {"result": result}

            
            return render_template("index.html", res=currency_results, symbol=symbol)
        
        return render_template('index.html')
