def test_range(number, range_start, range_end):
    if not (range_start <= number <= range_end): print(f'Число {number} не попадает в диапазон между {range_start} и {range_end}')