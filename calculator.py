from decimal import Decimal, ROUND_DOWN

def _rounding(something):
    cent = Decimal('0.05')
    something = Decimal(something)
    return something.quantize(cent, rounding=ROUND_DOWN)

def calculator(price, months, expected_inflation = 2, interest_rate = 0):
    expected_inflation = _rounding((100 - expected_inflation) / 100)
    interest_rate = _rounding((100 + interest_rate) / 100)
    price = _rounding(price) * interest_rate
    official_price = price / months
    last_price_paid = official_price
    real_prices = []
    for n in range(1, months+1):
        last_price_paid = _rounding(last_price_paid * expected_inflation)
        real_prices.append(last_price_paid)
    return real_prices
