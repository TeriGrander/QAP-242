from api import PetFriends
import pytest
from pfhelpers import Helpers
import tests.helpers

pf = PetFriends()
# prepare lists of parameters for parametrize fixture
name_pos = [tests.helpers.generate_string(20),
            tests.helpers.russian_chars(),
            tests.helpers.russian_chars().upper(),
            tests.helpers.chinese_chars()
            ]
name_neg = ['',
            tests.helpers.generate_string(255),
            tests.helpers.generate_string(1001),
            tests.helpers.special_chars(),
            123
            ]
animal_type_pos = [tests.helpers.generate_string(20),
                   tests.helpers.russian_chars(),
                   tests.helpers.russian_chars().upper(),
                   tests.helpers.chinese_chars(),]
animal_type_neg = ['',
                   tests.helpers.generate_string(255),
                   tests.helpers.generate_string(1001),
                   tests.helpers.special_chars(),
                   123
                   ]
age_pos = [1, 1.5, 8]
age_neg = [0, -1, 500, 2147483647, 2147483648, '123']
image_pos = ['tests/images/cat1.jpg']
image_neg = ['tests/images/large_file.png',
             'tests/images/text_file.txt',
             'tests/images/broken.jpg',
             ''
             ]
headers_accept = [{'Accept': 'application/json'},
                  {'Accept': 'application/xml'}
                  ]
headers_content = [{'Content-Type': 'application/json'},
                   {'Content-Type': 'application/xml'},
                   ]


class TestUpdatePet():
    @pytest.mark.update
    @pytest.mark.parametrize('age', age_pos,
                             ids=tests.helpers.ids_gen('age'))
    @pytest.mark.parametrize('animal_type', animal_type_pos,
                             ids=tests.helpers.ids_gen('animal_type'))
    @pytest.mark.parametrize('name', name_pos,
                             ids=tests.helpers.ids_gen('name'))
    def test_update_pet_with_valid_data(self, get_key, name,
                                        animal_type, age):
        """Проверяем, что при передаче корректных данных информация о
        питомце успешно обновляется.
        """

        code, first_pet = Helpers.get_first_of_my_pets_helper(get_key)

        if code == 1:
            test_pet_id = first_pet['id']
            status, result = pf.put_update_pet({'key': get_key}, test_pet_id,
                                               name, animal_type, age)
            assert status == 200
            assert result['name'] == name
            assert result['animal_type'] == animal_type
            assert result['age'] == str(age)
        else:
            raise Exception("There is no my pets")

    @pytest.mark.update
    def test_update_pet_with_blank_id(self, get_key, name='Lissa',
                                      animal_type='cat', age=2):
        """Проверяем, что при передаче пустой строки в pet_id возвращается
        код 404.
        """

        status, result = pf.put_update_pet({'key': get_key}, '', name,
                                           animal_type, age)

        assert status == 404
        assert 'name' not in result

    @pytest.mark.update
    @pytest.mark.parametrize('header_content_type', headers_content,
                             ids=tests.helpers.ids_gen('Content_type_Header'))
    @pytest.mark.parametrize('header_accept', headers_accept,
                             ids=tests.helpers.ids_gen('Accept_Header'))
    @pytest.mark.parametrize('age', age_neg,
                             ids=tests.helpers.ids_gen('age'))
    @pytest.mark.parametrize('animal_type', animal_type_neg,
                             ids=tests.helpers.ids_gen('animal_type'))
    @pytest.mark.parametrize('name', name_neg,
                             ids=tests.helpers.ids_gen('name'))
    def test_update_pet_with_incorrect_data(self, get_key, name,
                                            animal_type, age,
                                            header_accept,
                                            header_content_type):
        """Проверяем, что некорректные данные адекватно обрабатываются."""

        headers = {**header_accept, **header_content_type}
        code, first_pet = Helpers.get_first_of_my_pets_helper(get_key)

        if code == 1:
            test_pet_id = first_pet['id']
            status, _ = pf.put_update_pet({'key': get_key}, test_pet_id,
                                          name, animal_type, age, headers)
            assert status == 400
        else:
            raise Exception("There is no my pets")


class TestAddPetPhoto():
    @pytest.mark.update
    @pytest.mark.parametrize('image', image_pos,
                             ids=tests.helpers.ids_gen('image'))
    def test_add_pet_photo_for_existing_pet(self, get_key, image):
        """Проверяем, что фото добавляется к существующему питомцу без фото."""

        _, my_pets = pf.get_pets_list({'key': get_key}, 'my_pets')
        test_pet = list(filter(lambda x: x['pet_photo'] == '',
                               my_pets['pets']))[0]

        status, result = pf.post_add_pet_photo({'key': get_key},
                                               test_pet['id'], image)

        assert status == 200
        assert result['pet_photo'] != ''

    @pytest.mark.update
    @pytest.mark.xfail(reason='Баг NN4 в API, будет исправлен после XX')
    def test_add_pet_photo_for_non_existing_pet(self, get_key,
                                                image='tests/images/cat2.jpg'):
        """Проверяем, что к несуществующему питомцу фото не добавляется.
        На данный момент в API есть баг, и такой запрос возвращает 500.
        """

        status, result = pf.post_add_pet_photo({'key': get_key}, '1111', image)

        assert status == 404
        assert 'pet_photo' not in result

    @pytest.mark.update
    @pytest.mark.parametrize('header_content_type', headers_content,
                             ids=tests.helpers.ids_gen('Content_type_Header'))
    @pytest.mark.parametrize('header_accept', headers_accept,
                             ids=tests.helpers.ids_gen('Accept_Header'))
    @pytest.mark.parametrize('image', image_neg,
                             ids=tests.helpers.ids_gen('image'))
    def test_add_pet_photo_with_incorrect_data(self, get_key, image,
                                               header_accept,
                                               header_content_type):
        """Проверяем, что некорректные данные фото адекватно
        обрабатываются.
        """

        headers = {**header_accept, **header_content_type}
        _, my_pets = pf.get_pets_list({'key': get_key}, 'my_pets')
        test_pet = list(filter(lambda x: x['pet_photo'] == '',
                               my_pets['pets']))[0]

        status, _ = pf.post_add_pet_photo({'key': get_key}, test_pet['id'],
                                          image, headers)

        assert status == 400
