import pytest
from src.average import *

@pytest.mark.parametrize('list, extend_result',[
                            ([1, 2, 3], 2)])
def test_input_type_positive(list, extend_result):
    assert average(list) == extend_result


@pytest.mark.parametrize('list, extend_result',[
                            (None, pytest.raises(ValueError)),
                            (123, pytest.raises(TypeError)),
                            (123.123, pytest.raises(TypeError)),
                            ('строка', pytest.raises(TypeError)),
                            (True, pytest.raises(TypeError))
                            ])
def test_input_type_negative(list, extend_result):
    with extend_result:
        assert average(list) == extend_result


@pytest.mark.parametrize('list, extend_result',[
                            ([1, 2, 3], 2),
                            ([2, 3, 4], 3),
                            ([1.5, 2.5], 3.5)
                            ])
def test_data_list_positive(list, extend_result):
    average(list) == extend_result


@pytest.mark.parametrize('list, extend_result',[
                            (['qwe', 2, 3], pytest.raises(TypeError)),
                            ([None, 2, 3], pytest.raises(TypeError)),
                            ([[1, 2, 3], 2, 3], pytest.raises(TypeError)),
                            ([], pytest.raises(ValueError))
                            ])
def test_data_list_negative(list, extend_result):
    with extend_result:
        assert average(list) == extend_result


@pytest.mark.parametrize('list, extend_result',[
                            ([5, 6, 7], 6),
                            ([5.5, 6.5, 7.5], 6.5),
                            ([0], 0),
                            ([123], 123),
                            ([-1, -2, -3, -4, -5], -3),
                            ([1, 1, 1, 1, 1], 1)
])
def test_result_positive(list, extend_result):
    average(list) == extend_result







#
# @pytest.mark.parametrize('string, extend_result',[
#                             ("", 'Строка пустая')])
# def test_input_palindrome_boundary(string, extend_result ):
#     assert is_palindrome(string) == extend_result
#
#
# @pytest.mark.parametrize('string, extend_result',[
#                             (None, pytest.raises(TypeError)),
#                             (123, pytest.raises(TypeError)),
#                             (123.53, pytest.raises(TypeError))
#                             ])
# def test_input_palindrome_negative(string, extend_result):
#     with extend_result:
#         assert is_palindrome(string) == extend_result
#
#
# @pytest.mark.parametrize('string, extend_result',[
#                             ('qwert', False),
#                             ('ротор', True)
#                             ])
# def test_correct_result_palindrome(string, extend_result):
#     assert is_palindrome(string) == extend_result
