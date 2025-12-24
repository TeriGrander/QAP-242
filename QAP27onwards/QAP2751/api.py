import requests
import json
import functools
from typing import Callable, Any
from datetime import datetime
from urllib.parse import urlparse, parse_qs


def log_requests(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        method_name = func.__name__
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        res: requests.Response = func(*args, **kwargs)
        with open('log.txt', 'a', encoding='utf-8') as log_file:
            log_file.write('\n')
            log_file.write(f'Тест от: {timestamp}\n')
            log_file.write(f'Метод API: {method_name}\n')

            log_file.write('____ Request ____\n')

            request = res.request
            log_file.write(f'Метод запроса: {request.method}\n')
            log_file.write(f'URL запроса: {request.url}\n')
            parsed_url = urlparse(request.url)
            log_file.write(f'Путь запроса: {parsed_url.path}\n')
            query_params = parse_qs(parsed_url.query)
            if query_params:
                log_file.write('Query Params:\n')
                log_file.write(f'{json.dumps(query_params, indent=2,
                                             ensure_ascii=False)}\n')
            else:
                log_file.write('Query Params: Отсутствует\n')
            log_file.write('Headers:\n')
            # request преобразуем в dict
            log_file.write(f'{json.dumps(dict(request.headers), indent=2,
                                         ensure_ascii=False)}\n')
            log_file.write('Request Body:\n')
            if request.body:
                try:
                    body_content = request.body
                    if isinstance(body_content, bytes):
                        body_content = body_content.decode('utf-8')
                    body_content = body_content.strip()
                    if body_content.startswith('{') and \
                            body_content.endswith('}'):
                        log_file.write(f'{json.dumps(json.loads(body_content),
                                                     indent=2,
                                                     ensure_ascii=False)}\n')
                    else:
                        log_file.write(f'{body_content}\n')
                except (UnicodeDecodeError, json.JSONDecodeError, TypeError):
                    log_file.write(f'{repr(request.body)}\n')
            else:
                log_file.write('Request Body: Отсутствует\n')

            log_file.write('\n____ Response ____\n')
            log_file.write(f'Status code: {res.status_code}\n')
            log_file.write('Response Body:\n')

            try:
                result_json = res.json()
                log_file.write(f'{json.dumps(result_json, indent=2,
                                             ensure_ascii=False)}\n')
            except json.decoder.JSONDecodeError:
                log_file.write(f'{res.text}\n')

        status = res.status_code
        result = ''
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text

        return status, result
    return wrapper


class PetFriends():
    '''API библиотека к веб приложению Pet Friends'''
    def __init__(self) -> None:
        self.base_url = 'https://petfriends.skillfactory.ru/'

    @log_requests
    def get_api_key(self, email: str, password: str,
                    headers: dict = {}) -> json:
        """Метод делает запрос к API сервера и возвращает статус
        запроса и результат в формате JSON с уникальным ключом
        пользователя, найденного по указанным email и паролю.
        """

        endpoint_url = 'api/key'
        header = {'email': email, 'password': password, **headers}

        res = requests.get(self.base_url + endpoint_url, headers=header)

        return res

    @log_requests
    def get_pets_list(self, auth_key: json, filter: str = '',
                      headers: dict = {}) -> json:
        """Метод делает запрос к API сервера и возвращает статус
        запроса и результат в формате JSON со списком найденных
        питомцев, совпадающих с фильтром. На данный момент фильтр
        может иметь либо пустое значение - получить список всех
        питомцев, либо 'my_pets' - получить список собственных питомцев.
        """

        endpoint_url = 'api/pets'
        header = {'auth_key': auth_key['key'], **headers}
        params = {'filter': filter}

        res = requests.get(self.base_url + endpoint_url,
                           headers=header,
                           params=params)

        return res

    @log_requests
    def post_add_pet(self, auth_key: json, pet_name: str,
                     pet_type: str, pet_age: int, pet_image: str,
                     headers: dict = {}) -> json:
        """Метод отправляет на сервер данные о добавляемом питомце и
        возвращает статус запроса на сервер и результат в формате JSON
        с данными добавленного питомца.
        """

        endpoint_url = 'api/pets'
        header = {'auth_key': auth_key['key'], **headers}
        data = {
                'name': pet_name,
                'animal_type': pet_type,
                'age': pet_age
                }
        if pet_image != '':
            file = {'pet_photo': (pet_image, open(pet_image, 'rb'),
                                  'image/jpeg')}
        else:
            file = {'pet_photo': ''}

        res = requests.post(self.base_url + endpoint_url,
                            headers=header,
                            data=data,
                            files=file)

        return res

    @log_requests
    def delete_pet(self, auth_key: json, pet_id: str,
                   headers: dict = {}) -> json:
        """Метод отправляет на сервер запрос на удаление питомца по
        указанному ID и возвращает статус запроса.
        """

        endpoint_url = 'api/pets' + '/' + pet_id
        header = {'auth_key': auth_key['key'], **headers}

        res = requests.delete(self.base_url + endpoint_url, headers=header)

        return res

    @log_requests
    def put_update_pet(self, auth_key: json, pet_id: str,
                       pet_name: str, pet_type: str, pet_age: int,
                       headers: dict = {}) -> json:
        """Метод отправляет запрос на сервер об обновлении данных
        питомца по указанному ID и возвращает статус запроса и result
        в формате JSON с обновлённыи данными питомца.
        """

        endpoint_url = 'api/pets' + '/' + pet_id
        header = {'auth_key': auth_key['key'], **headers}
        params = {'name': pet_name, 'age': pet_age, 'animal_type': pet_type}

        res = requests.put(self.base_url + endpoint_url,
                           headers=header,
                           data=params)

        return res

    @log_requests
    def post_add_pet_simple(self, auth_key: json, pet_name: str,
                            pet_type: str, pet_age: int,
                            headers: dict = {}) -> json:
        """Метод отправляет на сервер данные о добавляемом питомце без
        фото и возвращает статус запроса на сервер и результат в
        формате JSON с данными добавленного питомца.
        """

        endpoint_url = 'api/create_pet_simple'
        header = {'auth_key': auth_key['key'], **headers}
        data = {
                'name': pet_name,
                'animal_type': pet_type,
                'age': pet_age
                }

        res = requests.post(self.base_url + endpoint_url,
                            headers=header,
                            data=data)

        return res

    @log_requests
    def post_add_pet_photo(self, auth_key: json,
                           pet_id: str, pet_image: str,
                           headers: dict = {}) -> json:
        """Метод отправляет запрос на сервер о добавлении фото питомца
        по указанному id питомца и возвращает статус запроса на сервер
        и результат в формате JSON с данными питомца, для которого
        добавлено фото.
        """

        endpoint_url = 'api/pets/set_photo' + '/' + pet_id
        header = {'auth_key': auth_key['key'], **headers}
        if pet_image != '':
            file = {'pet_photo': (pet_image, open(pet_image, 'rb'),
                                  'image/jpeg')}
        else:
            file = {'pet_photo': ''}

        res = requests.post(self.base_url + endpoint_url,
                            headers=header,
                            files=file)

        return res
