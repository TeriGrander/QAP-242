from api import PetFriends
from settings import valid_email, valid_password
import pytest
import tests.helpers

pf = PetFriends()
# prepare lists of parameters for parametrize fixture
emails = ['11'+valid_email,
          '',
          tests.helpers.generate_string(50),
          tests.helpers.generate_string(255),
          tests.helpers.generate_string(1001),
          '123'
          ]
passwords = ['11'+valid_password,
             '',
             tests.helpers.generate_string(50),
             tests.helpers.generate_string(255),
             tests.helpers.generate_string(1001),
             '123'
             ]
headers_accept = [{'Accept': '*/*'},
                  {'Accept': 'application/json'},
                  {'Accept': 'application/xml'}]
headers_content = [{'Content-Type': 'application/json'},
                   {'Content-Type': 'application/xml'},
                   {'Content-Type': 'application/x-www-form-urlencoded'},
                   {'Content-Type': 'application/form-data'},
                   {'Content-Type': 'text/plain'},
                   ]


class TestGetKey():
    def test_get_api_key_for_valid_user(self, email=valid_email,
                                        password=valid_password,
                                        headers={}):
        """Проверяем, что при передаче email и пароля существующего
        пользователя успешно возвращается ключ аутентификации.
        (Тест взят из модуля).
        """

        status, result = pf.get_api_key(email, password, headers)

        assert status == 200
        assert 'key' in result

    @pytest.mark.parametrize('header_content_type', headers_content,
                             ids=tests.helpers.ids_gen('Content_type_Header'))
    @pytest.mark.parametrize('header_accept', headers_accept,
                             ids=tests.helpers.ids_gen('Accept_Header'))
    @pytest.mark.parametrize('password', passwords,
                             ids=tests.helpers.ids_gen('password'))
    @pytest.mark.parametrize('email', emails,
                             ids=tests.helpers.ids_gen('email'))
    def test_get_api_key_invalid_credentials(self, email, password,
                                             header_accept,
                                             header_content_type):
        """Проверяем, что при передаче несуществующих email и пароля ключ
        аутентификации не возвращается.
        """
        headers = {**header_accept, **header_content_type}
        status, result = pf.get_api_key(email, password, headers)
        assert status == 403
        assert 'key' not in result
