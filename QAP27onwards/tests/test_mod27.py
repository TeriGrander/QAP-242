from module27.code import Module27
import pytest

tt = Module27()


class TestModule27:
    '''Tests for module 27'''

    def ids_a(val):
        return 'a=({0})'.format(str(val))

    def ids_b(val):
        return 'b=({0})'.format(str(val))

    def ids_c(val):
        return f'c={val}'

    @pytest.mark.parametrize('a', [-1, 0, 1, 3], ids=ids_a)
    @pytest.mark.parametrize('b', [-1, 0, 1, 4], ids=ids_b)
    @pytest.mark.parametrize('c', [-1, 0, 1, 5], ids=ids_c)
    def test_is_triangle(self, a, b, c):
        res = tt.is_triangle(a, b, c)
        print(f'[a = {a}, b = {b}, c = {c}] is a triangle - {res}')
        assert True
