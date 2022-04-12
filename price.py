from itertools import product


def discounted(price, discount, max_discount = 40):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 60:
        raise ValueError('Максимальная скидка не может быь более 60%')
    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    return price_with_discount
discounted(100, 40, 90)