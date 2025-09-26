import os, json
main_path = os.getcwd()
relative_path = r'QAP-242\QAP-20\orders_july_2023.json'
full_path = os.path.join(main_path, relative_path)
with open(full_path, 'r') as orders_file:
    orders_data = json.load(orders_file)

by_price = sorted(orders_data, key = lambda x: orders_data[x]['price'], reverse=True)
max_price = orders_data[by_price[0]]['price']
priciest_orders = list(filter(lambda x: orders_data[x]['price'] == max_price, orders_data))
by_items = sorted(orders_data, key = lambda x: orders_data[x]['quantity'], reverse=True)
highest_quantity = orders_data[by_items[0]]['quantity']
most_items = list(filter(lambda x: orders_data[x]['quantity'] == highest_quantity, orders_data))

print(f'Самые дорогие заказы в июле: {priciest_orders}, цена заказа {max_price}')
print(f'Заказы с самым большим количеством товаров: {most_items}, количество товаров {highest_quantity}')

numbers_by_dates = {}
for v in orders_data.values():
    if v['date'] in numbers_by_dates.keys():
        numbers_by_dates[v['date']] += 1
    else:
        numbers_by_dates[v['date']] = 1

numbers_by_dates_ordered = sorted(numbers_by_dates, key = lambda x: numbers_by_dates[x], reverse=True)
most_orders_in_day = numbers_by_dates[numbers_by_dates_ordered[0]]
best_days = list(filter(lambda x: numbers_by_dates[x] == most_orders_in_day, numbers_by_dates))
print(f'Дни с максимальным количеством заказов: {best_days}, заказов: {most_orders_in_day}')


numbers_by_users = {}
for v in orders_data.values():
    if v['user_id'] in numbers_by_users.keys():
        numbers_by_users[v['user_id']] += 1
    else:
        numbers_by_users[v['user_id']] = 1
numbers_by_users_ordered = sorted(numbers_by_users, key = lambda x: numbers_by_users[x], reverse=True)
most_orders_by_user = numbers_by_users[numbers_by_users_ordered[0]]
best_users = list(filter(lambda x: numbers_by_users[x] == most_orders_by_user, numbers_by_users))
print(f'Пользователи с максимальным количеством заказов: {best_users}, заказов: {most_orders_by_user}')

sums_by_user = {}
for v in orders_data.values():
    if v['user_id'] in sums_by_user.keys():
        sums_by_user[v['user_id']] += v['price']
    else:
        sums_by_user[v['user_id']] = v['price']
sums_by_user_ordered = sorted(sums_by_user, key = lambda x: sums_by_user[x], reverse=True)
highest_sum_by_user = sums_by_user[sums_by_user_ordered[0]]
wealthiest_users = list(filter(lambda x: sums_by_user[x] == highest_sum_by_user, sums_by_user))
print(f'Пользователи с максимальной стоимостью всех заказов: {wealthiest_users}, стоимость заказов: {highest_sum_by_user}')

sum_prices = 0
for v in orders_data.values():
    sum_prices += v['price']
average_price = sum_prices / len(orders_data)

print(f'Средняя стоимость заказа в июле была {average_price}')

sum_items = 0
for v in orders_data.values():
    sum_items += v['quantity']
average_item_price = sum_prices / sum_items

print(f'Средняя стоимость товаров в июле была {average_item_price}')