from flask import Flask, render_template, request, json
from calculator import calculator
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/calc/", methods=['GET'])
def calc():
    payment_price = float(request.args.get('payment_price'))
    payment_months = int(request.args.get('payment_months'))
    interest_rate = float(request.args.get('interest_rate'))
    expected_inflation = float(request.args.get('expected_inflation'))
    prices = calculator(payment_price, payment_months, expected_inflation, interest_rate)
    return render_template('cuotitas.html', prices=prices, total_price=sum(prices))

if __name__ == '__main__':
    app.run()
