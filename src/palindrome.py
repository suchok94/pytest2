def is_palindrome(s):
    if not isinstance(s, str):
        raise TypeError

    if not s:
        return 'Строка пустая'

    return s == s[::-1]

