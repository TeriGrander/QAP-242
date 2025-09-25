phone_numbers = ['123-456-7890', '123.456.7890', '(123) 456-7890', '+1234567890', '1234567890']

def format_phone_number(number):
   return ''.join(list(filter(lambda x: x.isdigit(), number)))

formatted_numbers = list(map(format_phone_number, phone_numbers))

print(formatted_numbers)

print(format_phone_number(['a','b','b','5','6']))