from flask import Flask, request, jsonify
from calculator import calculator

app = Flask(__name__)

@app.route("/")
def index():
	return 'Bienvenido a cuotitas'

@app.route("/api/v1.0/calc/", methods=['GET'])
def calc():
	payment_price = float(request.args.get('payment_price'))
	payment_months = int(request.args.get('payment_months'))
	interest_rate = float(request.args.get('interest_rate'))
	expected_inflation = float(request.args.get('expected_inflation'))
	prices = calculator(payment_price, payment_months, expected_inflation, interest_rate)
	return jsonify(prices=prices,total_price=sum(prices))
	#return str(request.args)

if __name__ == '__main__':
	app.run()
