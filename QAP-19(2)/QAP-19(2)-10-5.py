from typing import Dict, List, Any

def category_dict(categories: Dict[Any, Any], parent_path='') -> List[str]:
   res = []
   if parent_path != '': res.append(parent_path)
   if len(categories) == 0: return res
   else:
      for k in categories.keys():
         if parent_path == '': new_parent_path = k
         else: new_parent_path = f"{parent_path} > {k}"
         res.extend(category_dict(categories[k], new_parent_path))
   return res

      
# 1 уровень, 2 категории => две строки
# 2 уровня, по 2 категории => 4 строки


categories = {
   "Электроника": {
       "Телефоны": {
           "Смартфоны": {},
           "Проводные": {}
       },
       "Компьютеры": {
           "Ноутбуки": {},
           "Стационарные": {
               "Игровые": {},
               "Для работы": {}
           }
       }
   },
   "Одежда": {
       "Мужская": {
           "Джинсы": {},
           "Куртки": {}
       }
   }
}

paths = category_dict(categories, parent_path='root')
for path in paths:
   print(path)

# root > Электроника
# root > Электроника > Телефоны
# root > Электроника > Телефоны > Смартфоны
# root > Электроника > Телефоны > Проводные
# root > Электроника > Компьютеры
# root > Электроника > Компьютеры > Ноутбуки
# root > Электроника > Компьютеры > Стационарные
# root > Электроника > Компьютеры > Стационарные > Игровые
# root > Электроника > Компьютеры > Стационарные > Для работы
# root > Одежда
# root > Одежда > Мужская
# root > Одежда > Мужская > Джинсы
# root > Одежда > Мужская > Куртки


paths = category_dict(categories)
for path in paths:
   print(path)

# Электроника
# Электроника > Телефоны
# Электроника > Телефоны > Смартфоны
# ...
# Одежда > Мужская
# Одежда > Мужская > Джинсы
# Одежда > Мужская > Куртки