from api import PetFriends

pf = PetFriends()


class Helpers():
    def get_first_of_my_pets_helper(get_key) -> tuple:
        """Вспомогательная функция, возвращает код 1 и данные о первом
        питомце в списке, полученном по фильтру my_pets, или код 0 и
        сообщение что по этому фильтру нет питомцев.
        """

        _, my_pets = pf.get_pets_list({'key': get_key}, filter='my_pets')
        if len(my_pets['pets']) > 0:
            return 1, my_pets['pets'][0]
        else:
            return 0, 'There is no my pets'
