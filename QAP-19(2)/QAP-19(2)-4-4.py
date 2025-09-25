def filter_api_tests(cases):
    return list(filter(lambda x: x['type'] == 'API', cases))

test_cases = [
   {"id": 1, "description": "Тест №1", "type": "UI"},
   {"id": 2, "description": "Тест №2", "type": "API"},
   {"id": 3, "description": "Тест №3", "type": "API"},
   {"id": 4, "description": "Тест №4", "type": "Performance"},
]

filtered_test_cases = filter_api_tests(test_cases)
print(filtered_test_cases)
# [{'id': 2, 'description': 'Тест №2', 'type': 'API'}, {'id': 3, 'description': 'Тест №3', 'type': 'API'}