import pytest
from src.palindrome import *

@pytest.mark.parametrize('string, extend_result',[
                            ('строка', False)])
def test_input_palindrome_positive(string, extend_result ):
    assert is_palindrome(string) == extend_result


@pytest.mark.parametrize('string, extend_result',[
                            ("", 'Строка пустая')])
def test_input_palindrome_boundary(string, extend_result ):
    assert is_palindrome(string) == extend_result


@pytest.mark.parametrize('string, extend_result',[
                            (None, pytest.raises(TypeError)),
                            (123, pytest.raises(TypeError)),
                            (123.53, pytest.raises(TypeError))
                            ])
def test_input_palindrome_negative(string, extend_result):
    with extend_result:
        assert is_palindrome(string) == extend_result


@pytest.mark.parametrize('string, extend_result',[
                            ('qwert', False),
                            ('ротор', True)
                            ])
def test_correct_result_palindrome(string, extend_result):
    assert is_palindrome(string) == extend_result
