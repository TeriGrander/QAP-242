def sales_stats(data, **kwargs):
    revenue = 0
    quantity = {}
    if 'revenue' in kwargs.keys():
        for sale in data:
            revenue += sale[1] * sale[2]
    else: revenue = None
    if 'quantity' in kwargs.keys():
        for sale in data:
            if sale[0] in quantity.keys():
                quantity[sale[0]] += sale[1]
            else:
                quantity[sale[0]] = sale[1]
    else: quantity = None
    return revenue, quantity

def create_report(sales_data, sales_stats):
    data = sales_stats(sales_data, revenue=True, quantity=True)
    average = data[0] / len(sales_data)
    quantity_str = []
    for name, quant in data[1].items():
        quantity_str.append(f'{name}: {quant}')
    quantities = '\n'.join(quantity_str)
    report = 'Средний доход за данный период составил {a}.\nКоличество проданных единиц каждого товара:\n{q}'.format(a = average, q = quantities)
    return report

sales_data = [["яблоки", 20, 20], ["груши", 5, 30], ["яблоки", 7, 20]]
print(create_report(sales_data, sales_stats))
# Средний доход за данный период составил 230.0.
# Количество проданных единиц каждого товара:
# яблоки: 27
# груши: 5


def dummy_func(data, **kwargs):
    revenue = 100.0
    quantity = {"Apple": 10, "Orange": 5}
    return revenue, quantity
print(create_report([('Apple', 10, 0.5), ('Orange', 5, 0.6)], dummy_func))