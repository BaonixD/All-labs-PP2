def is_palindrome(s):
    s = s.replace(" ", "").lower()  # Убираем пробелы и приводим к нижнему регистру
    return s == s[::-1]

print(is_palindrome("madam"))       # True