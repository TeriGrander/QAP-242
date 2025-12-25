from api import PetFriends
import pytest
import tests.helpers

pf = PetFriends()
# prepare lists of parameters for parametrize fixture
name_pos = [tests.helpers.generate_string(20),
            tests.helpers.russian_chars(),
            tests.helpers.russian_chars().upper(),
            tests.helpers.chinese_chars()
            ]
name_neg = [tests.helpers.generate_string(255),
            tests.helpers.generate_string(1001),
            tests.helpers.special_chars(),
            123,
            ''
            ]
animal_type_pos = [tests.helpers.generate_string(20),
                   tests.helpers.russian_chars(),
                   tests.helpers.russian_chars().upper(),
                   tests.helpers.chinese_chars(),]
animal_type_neg = [tests.helpers.generate_string(255),
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


class TestAddPetFull():
    @pytest.mark.add
    @pytest.mark.parametrize('image', image_pos,
                             ids=tests.helpers.ids_gen('image'))
    @pytest.mark.parametrize('age', age_pos,
                             ids=tests.helpers.ids_gen('age'))
    @pytest.mark.parametrize('animal_type', animal_type_pos,
                             ids=tests.helpers.ids_gen('animal_type'))
    @pytest.mark.parametrize('name', name_pos,
                             ids=tests.helpers.ids_gen('name'))
    def test_add_pet_with_valid_data(self, get_key, name,
                                     animal_type, age, image):
        """Проверяем, что при запросе с корректными данными питомец успешно
        добавляется.
        """

        status, result = pf.post_add_pet({'key': get_key}, name, animal_type,
                                         age, image)

        assert status == 200
        assert result['name'] == name
        assert result['animal_type'] == animal_type
        assert result['age'] == str(age)
        pf.delete_pet({'key': get_key}, result['id'])

    @pytest.mark.add
    # @pytest.mark.skip(reason='Баг NN1 в API, будет исправлен после XX')
    @pytest.mark.parametrize('header_content_type', headers_content,
                             ids=tests.helpers.ids_gen('Content_type_Header'))
    @pytest.mark.parametrize('header_accept', headers_accept,
                             ids=tests.helpers.ids_gen('Accept_Header'))
    @pytest.mark.parametrize('image', image_neg,
                             ids=tests.helpers.ids_gen('image'))
    @pytest.mark.parametrize('age', age_neg,
                             ids=tests.helpers.ids_gen('age'))
    @pytest.mark.parametrize('animal_type', animal_type_neg,
                             ids=tests.helpers.ids_gen('animal_type'))
    @pytest.mark.parametrize('name', name_neg,
                             ids=tests.helpers.ids_gen('name'))
    def test_add_pet_negative_data(self, get_key, name,
                                   animal_type, age, image,
                                   header_accept,
                                   header_content_type):
        """Проверяем обработку некорректных данных в запросе на
        добавление питомца.
        На данный момент в API никакой валидации данных нет, и питомцы
        добавляются даже с самыми некорректно-выглядящими данными.
        """
        headers = {**header_accept, **header_content_type}
        status, result = pf.post_add_pet({'key': get_key}, name,
                                         animal_type, age, image,
                                         headers)

        assert status == 400
        if 'id' in result:
            pf.delete_pet({'key': get_key}, result['id'])


class TestAddPetSimple():
    @pytest.mark.add
    @pytest.mark.parametrize('age', age_pos,
                             ids=tests.helpers.ids_gen('age'))
    @pytest.mark.parametrize('animal_type', animal_type_pos,
                             ids=tests.helpers.ids_gen('animal_type'))
    @pytest.mark.parametrize('name', name_pos,
                             ids=tests.helpers.ids_gen('name'))
    def test_add_pet_simple_valid_data(self, get_key, name,
                                       animal_type, age):
        """Проверяем, что при запросе с корректными данными без фото
        питомец успешно добавляется.
        """

        # _, auth_key = pf.get_api_key(valid_email, valid_password)
        status, result = pf.post_add_pet_simple({'key': get_key}, name,
                                                animal_type, age)

        assert status == 200
        assert result['name'] == name
        assert result['animal_type'] == animal_type
        assert result['age'] == str(age)
        pf.delete_pet({'key': get_key}, result['id'])

    @pytest.mark.add
    def test_add_pet_simple_invalid_key(self, name, animal_type, age):
        """Проверяем, что при запросе с некорректным ключом аутентификации
        питомец не добавляется.
        """

        status, result = pf.post_add_pet_simple({'key': '111'}, name,
                                                animal_type, age)

        assert status == 403
        assert 'name' not in result

    @pytest.mark.add
    # @pytest.mark.skip(reason='Баг NN2 в API, будет исправлен после XX')
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
    def test_add_pet_simple_negative_data(self, get_key, name,
                                          animal_type, age,
                                          header_accept,
                                          header_content_type):
        """Проверяем обработку некорректных данных в запросе на
        добавление питомца без фото.
        На данный момент в API никакой валидации данных нет, и питомцы
        добавляются даже с самыми некорректно-выглядящими данными.
        """
        headers = {**header_accept, **header_content_type}
        status, result = pf.post_add_pet_simple({'key': get_key}, name,
                                                animal_type, age, headers)

        assert status == 422
        assert name not in result
        if 'id' in result:
            pf.delete_pet({'key': get_key}, result['id'])

    def test_add_pet_simple_create_test_data1(self, get_key,
                                              name='',
                                              animal_type='type',
                                              age=1):
        """Проверяем обработку некорректных данных в запросе на
        добавление питомца без фото.
        На данный момент в API никакой валидации данных нет, и питомцы
        добавляются даже с самыми некорректно-выглядящими данными.
        """
        status, result = pf.post_add_pet_simple({'key': get_key}, name,
                                                animal_type, age)

        assert status == 200

    def test_add_pet_simple_create_test_data2(self, get_key,
                                              name='name',
                                              animal_type='',
                                              age=1):
        """Проверяем обработку некорректных данных в запросе на
        добавление питомца без фото.
        На данный момент в API никакой валидации данных нет, и питомцы
        добавляются даже с самыми некорректно-выглядящими данными.
        """
        status, result = pf.post_add_pet_simple({'key': get_key}, name,
                                                animal_type, age)

        assert status == 200
        
    def test_add_pet_simple_create_test_data3(self, get_key,
                                              name='name',
                                              animal_type='type',
                                              age=''):
        """Проверяем обработку некорректных данных в запросе на
        добавление питомца без фото.
        На данный момент в API никакой валидации данных нет, и питомцы
        добавляются даже с самыми некорректно-выглядящими данными.
        """
        status, result = pf.post_add_pet_simple({'key': get_key}, name,
                                                animal_type, age)

        assert status == 200        