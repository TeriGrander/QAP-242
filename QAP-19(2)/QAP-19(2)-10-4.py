def log_filter(log: str, level: str):
    messages = log.splitlines()
    return filter(lambda x: x[20:].startswith(level), messages)



logs = """\
2023-08-15 14:15:24 INFO Starting the system.
2023-08-15 14:15:26 WARN System load is above 80%.
2023-08-15 14:15:27 ERROR Failed to connect to database.
2023-08-15 14:15:28 INFO Connection retry in 5 seconds.
2023-08-15 14:15:33 ERROR Failed to connect to database.
2023-08-15 14:15:28 INFO Connection returned 503 error.
"""

for log in log_filter(logs, 'ERROR'):
   print(log)
