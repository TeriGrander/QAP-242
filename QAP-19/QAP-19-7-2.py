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
    


sales_data = [["яблоки", 10, 20], ["груши", 5, 30], ["яблоки", 7, 20]]
print(sales_stats(sales_data, revenue=True))
# (490, None)
print(sales_stats(sales_data, quantity=True))
# (None, {'яблоки': 17, 'груши': 5})
print(sales_stats(sales_data, quantity=True, revenue=True))

print(sales_stats(sales_data, customers=True))
# (None, None)
print(sales_stats([('Apple', 10, 0.5), ('Orange', 5, 0.6)], revenue = True, quantity = True))
# (8.0, {'Apple': 10, 'Orange': 5})
print(sales_stats([('Apple', 10, 0.5), ('Orange', 5, 0.6)], revenue = True))
# (8.0, None)
print(sales_stats([], revenue = True, quantity = True))
# (0, {})