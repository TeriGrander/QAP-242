def filter_high_severity(bugs):
    return list(filter(lambda x: x['severity'] == 'high', bugs))

bugs = [
   {"id": 1, "description": "Баг №1", "severity": "low"},
   {"id": 2, "description": "Баг №2", "severity": "medium"},
   {"id": 3, "description": "Баг №3", "severity": "high"},
   {"id": 4, "description": "Баг №4", "severity": "high"},
]

filtered_bugs = filter_high_severity(bugs)
print(filtered_bugs)
# [{'id': 3, 'description': 'Баг №3', 'severity': 'high'}, {'id': 4, 'description': 'Баг №4', 'severity': 'high'}]