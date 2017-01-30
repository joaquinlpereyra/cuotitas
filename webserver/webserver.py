from flask import Flask, render_template, request, json
import requests
app = Flask(__name__)

url='http://127.0.0.1:5000/api/v1.0/calc/'

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/calc/", methods=['GET'])
def calc():
	parameters = {
		'payment_price': request.args.get('payment_price'),
		'payment_months': request.args.get('payment_months'),
		'interest_rate': request.args.get('interest_rate'),
		'expected_inflation': request.args.get('expected_inflation')
		}
	r = requests.get(url, params=parameters)
	return render_template('cuotitas.html', prices=r.json()['prices'], total_price=r.json()['total_price'])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
