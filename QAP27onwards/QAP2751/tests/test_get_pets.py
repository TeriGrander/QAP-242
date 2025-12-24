from api import PetFriends
import pytest
import tests.helpers

pf = PetFriends()
# prepare lists of parameters for parametrize fixture
filter_pos = ['', 'my_pets']
filter_neg = [tests.helpers.generate_string(255),
              tests.helpers.generate_string(1001),
              tests.helpers.russian_chars(),
              tests.helpers.russian_chars().upper(),
              tests.helpers.chinese_chars(),
              tests.helpers.special_chars(),
              123]
headers_accept = [{'Accept': '*/*'},
                  {'Accept': 'application/json'},
                  {'Accept': 'application/xml'}]


class TestPetsList():
    @pytest.mark.list
    @pytest.mark.parametrize('filter', filter_pos,
                             ids=tests.helpers.ids_gen('filter'))
    def test_get_pets_list_with_valid_key(self, get_key, filter):
        """Проверяем, что при передаче корректного ключа аутентификации
        успешно возвращается список питомцев.
        """

        # _, auth_key = pf.get_api_key(valid_email, valid_password)
        status, result = pf.get_pets_list({'key': get_key}, filter)

        assert status == 200
        assert len(result['pets']) != 0

    @pytest.mark.list
    def test_get_pets_list_with_invalid_key(self):
        """Проверяем, что при передаче некорректного ключа аутентификации
        возвращается код 403, а не список питомцев.
        """

        status, result = pf.get_pets_list({'key': '111'})
        assert status == 403
        assert 'Forbidden' in result

    @pytest.mark.list
    @pytest.mark.parametrize('header_accept', headers_accept,
                             ids=tests.helpers.ids_gen('Accept_Header'))
    @pytest.mark.parametrize('filter', filter_neg,
                             ids=tests.helpers.ids_gen('filter'))
    def test_get_pets_list_with_negative_filter(self, get_key, filter,
                                                header_accept):
        """Проверяем обработку некорректных данных, переданных в фильтр."""
        headers = {**header_accept}
        status, _ = pf.get_pets_list({'key': get_key}, filter, headers)
        assert status == 400
