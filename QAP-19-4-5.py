def format_date(date_string, format='dmy'):
    date_list = date_string.split('-')
    if format == 'dmy': return date_list[2] + date_list[1] + date_list[0]
    elif format == 'mdy': return date_list[1] + date_list[2] + date_list[0]
    elif format == 'ymd': return date_list[0] + date_list[1] + date_list[2]
    else: return date_string 


print(format_date("2023-07-01"))
# 01072023
print(format_date("2023-07-01", format="dmy"))
# 01072023
print(format_date("2023-07-01", format="mdy"))
# 07012023
print(format_date("2023-07-01", format="ymd"))
# 20230701
