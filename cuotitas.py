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
    prices = calculator(payment_price, payment_months)
    return render_template('cuotitas.html', prices=prices, total_price=sum(prices))

if __name__ == '__main__':
    app.run()
