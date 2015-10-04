# coding: utf-8
import hashlib

credentials = {
    'bruce': 'd63dc919e201d7bc4c825630d2cf25fdc93d4b2f0d46706d29038d01',  # password
    'rachel': '39dda14e76849cd4ab63c95c0a096a38cb020e596c98d976bb77814d',  # secretpwd
    'alfred': '5154aaa49392fb275ce7e12a7d3e00901cf9cf3ab10491673f97322f',  # qwerty
    'james': '78d8045d684abd2eece923758f3cd781489df3a48e1278982466017f',  # 123
    'john': 'b82cd17c844ed0f9e97a84d7d7bff754625085649c5008f67cee0f8c',  # qweasd
}


#	5. User authentication
#
#	Открыть файл user_auth.py (python.aori.ru/bp/user_auth.py).
#	Реализовать функцию is_auth_successful, которая возвращает True или False в зависимости от того, 
#	верно ли введён пользователь и пароль.
def is_auth_successful(login, password):
    return credentials[login] == hashlib.sha224(password).hexdigest()


if __name__ == "__main__":
    print is_auth_successful('bruce', 'secretpwd')
    print is_auth_successful('alfred', 'some_wrong_password')
    print is_auth_successful('rachel', 'secretpwd')
