from functools import reduce

def calculate_total_price(cart):
    return reduce(lambda acc, item: acc + item['price'], cart, 0)


cart = [
    {'product_name': 'Мышка', 'price': 15.99},
    {'product_name': 'Клавиатура', 'price': 25.50},
    {'product_name': 'Наушники', 'price': 10.75}
]

total_price = calculate_total_price(cart)
print(f"Общая стоимость товаров в корзине: ${total_price:.2f}")
# Общая стоимость товаров в корзине: $52.24