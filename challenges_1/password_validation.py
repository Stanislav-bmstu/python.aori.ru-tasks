# coding=utf-8
# 5. Валидация пароля
# Написать функцию, которая принимает на вход пароль и возвращает True или False
# в зависимости от того, удовлетворяет ли он необходимым требованиям.
# Требования такие: в нём должны быть хотя бы одна строчная буква, хотя бы одна заглавная,
# хотя бы одна цифра и хотя бы один символ; минимальная длина - 8 символов.


def validate(password):
    is_uppercase = False
    is_lowercase = False
    if len(password) < 8:
        return False
    for token in password:
        if token.islower():
            is_lowercase = True
        elif token.isupper():
            is_uppercase = True
        if is_lowercase & is_uppercase:
            return True
    return False


if __name__ == "__main__":
    print validate('itSImpossible')
    print validate('12')
    print validate('itossible')
    print validate('1213231a')
    print validate('1213231B')
    print validate('aSaSa')
    print validate('2DSjdj23')
