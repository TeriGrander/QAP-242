from api import PetFriends
import pytest
import tests.helpers

pf = PetFriends()


class TestDeletePet():
    pet_ids_neg = ['',
                   tests.helpers.generate_string(20),
                   tests.helpers.generate_string(255),
                   tests.helpers.generate_string(1001),
                   tests.helpers.special_chars(),
                   '123']
# Unclear how to parametrize: id of not-my pet, non-existent id.
# Adding separate tests for those.
    headers_accept = [{'Accept': 'application/json'},
                      {'Accept': 'application/xml'}
                      ]
    headers_content = [{'Content-Type': 'application/json'},
                       {'Content-Type': 'application/xml'},
                       ]

    @pytest.mark.delete
    def test_delete_existing_pet(self, get_key):
        """Проверяем, что при передаче существующего pet_id питомец успешно
        удаляется.
        """

        # _, auth_key = pf.get_api_key(valid_email, valid_password)
        _, test_pet = pf.post_add_pet_simple({'key': get_key},
                                             '111', '111', 11)

        status, _ = pf.delete_pet({'key': get_key}, test_pet['id'])
        _, check = pf.get_pets_list({'key': get_key}, filter='my_pets')
        ids_list = list(map(lambda x: x['id'], check['pets']))

        assert status == 200
        assert test_pet['id'] not in ids_list

    @pytest.mark.delete
    # @pytest.mark.xfail(reason='Баг NN3 в API, будет исправлен после XX')
    def test_delete_non_existing_pet(self, get_key):
        """Проверяем, что при попытке удалить питомца по несуществующему id
        возвращается ошибка.
        На данный момент в API есть баг, и такой запрос возврщает 200.
        """

        # _, auth_key = pf.get_api_key(valid_email, valid_password)
        status, _ = pf.delete_pet({'key': get_key}, '111111')

        assert status == 403

    @pytest.mark.delete
    # @pytest.mark.xfail(reason='Баг NN3 в API, будет исправлен после XX')
    def test_delete_not_my_pet(self, get_key, get_2nd_key):
        """Проверяем, что при попытке удалить чужого питомца возвращается
        ошибка.
        На данный момент в API есть баг, и такой запрос срабатывает.
        """
        _, result = pf.post_add_pet_simple({'key': get_2nd_key}, "name",
                                           "type", "age")
        pet_id = result['id']
        status, _ = pf.delete_pet({'key': get_key}, pet_id)

        assert status == 403

    @pytest.mark.delete
    # @pytest.mark.xfail(reason='Баг NN3 в API, будет исправлен после XX')
    @pytest.mark.parametrize('header_content_type', headers_content,
                             ids=tests.helpers.ids_gen('Content_type_Header'))
    @pytest.mark.parametrize('header_accept', headers_accept,
                             ids=tests.helpers.ids_gen('Accept_Header'))
    @pytest.mark.parametrize('pet_id', pet_ids_neg,
                             ids=tests.helpers.ids_gen('pet_id'))
    def test_delete_negative_ids(self, get_key, pet_id, header_accept,
                                 header_content_type):
        """Проверяем, что передача некорректного id обрабатывается.
        На данный момент в API есть баг, и такой запрос возврщает 200.
        """
        headers = {**header_accept, **header_content_type}
        status, _ = pf.delete_pet({'key': get_key}, pet_id, headers)

        assert status == 400
