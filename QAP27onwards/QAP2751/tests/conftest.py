import pytest
from settings import valid_email, valid_password, user2_email, user2_password
from api import PetFriends
from datetime import datetime


pf = PetFriends()


@pytest.fixture(scope="class")
def get_key():
    # переменные email и password нужно заменить своими учетными данными
    status, result = pf.get_api_key(valid_email, valid_password)
    assert status == 200, 'Запрос выполнен неуспешно'
    return result['key']


@pytest.fixture(autouse=True)
def time_delta():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    print(f"\nТест шел: {end_time - start_time}")


@pytest.fixture
def get_2nd_key():
    status, result = pf.get_api_key(user2_email, user2_password)
    assert status == 200, 'Запрос выполнен неуспешно'
    return result['key']
