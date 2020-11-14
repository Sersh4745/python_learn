"""
    Необходимо реализовать форму регистрации пользователей.
    Поля формы: номер телефона, email, пароль и подтверждение пароля.

    !!! Для решения необходимо использовать функции и рекурсию, а не циклы. !!!

    пункты с ** - дополнительно, но не обязательно (не влияет на оценку)

    1. Пользователь вводит номер телефона.
        Программа проверяет валидность телефона:
        - приводит номер к формату 380501234567
        - если номер не получается привести к нужному формату
            то запрашивает ввод номера еще раз
            и так до тех пор, пока не будет введен валидный номер

    2. Пользователь вводит email.
        Программа проверяет валидность email:
        - должен иметь длину 6 символов и больше
            (функция len())
        - содержать один символ '@'
            (строчный метод count())
        - ** содержать логин и полный домен (логин@полный.домен)
        Пользователь может вводить email до тех пор, пока он не будет валидным.

    3. Пользователь ввод пароль.
        Программа проверяет надежность пароля:
        - минимум 8 символов
            (функция len())
        - пароль не должен содержать пробельные символы
            (строчный метод isspace())
        - наличие минимум 1 буквы в верхнем регистре, 1 в нижнем и 1 цифры
            (строчные методы isupper(), islower(), isdigit())
        - ** наличие минимум 1 спец символа

    4. После успешного ввода пароля пользователь вводит подтверждение пароля.
        Если подтверждение пароля не сходится с введенным паролем,
        то возвращаемся к пункту 3.

        Программа выводит сообщение:

        Поздравляем с успешной регистрацией!
        Ваш номер телефона: +380501234567
        Ваш email: example@mail.com
        Ваш пароль: **********

"""
from random import choice, randint
from string import digits,ascii_lowercase,ascii_uppercase,punctuation
import re

def main():
    phone = input_phone()
    email = input_email()
    password = input_password()
   
    
    print('Поздравляем с успешной регистрацией!')
    print('Ваш номер телефона:',phone) 
    print('Ваш Email:',email)
    print('Ваш пароль::',password)

        
###########

def input_phone():
    phone_number = input('Введите номер телефона: ')
    phone_number1 = re.sub(r'\D','', phone_number) # если пользователь введет, что то кроме цифр сработает повторите попытку. Не делал проверку на число! умесно делать ее?
    good_number = phone_number1

    if len(good_number) > 10:
        good_number = str(380)+good_number[-9:]
        return good_number
    else:
        print("Повторите попытку (нехватает цифр)")
        return input_phone()

#
        
def input_email():
    email_input = input('Введите символы для будущего Email: ')
    parol = email_input.replace(' ','')# удаляем все пробелы или можно проверку на isspace и просить ввести еще раз
    

    if len(parol) < 6:
        print('Email не верный.\nВведите больше 6 символов')
        return input_email()
    if parol.find('@') > 0 and parol.find('.') > (parol.find('@')+1) and parol.find('.') < parol.rfind(parol[-1]): # находим индекс @ и точки. Если точка стоит дальше чем знак @ + 1 то домен полный(как вариант)
        return parol
    else:
        print('Введите Email правильно. ')
        return input_email()


def input_password():
    words_for_password = input('Введите символы для будущего пароля: ')
    words = words_for_password.replace(' ','')# удаляем все пробелы или можно проверку на isspace и просить ввести еще раз
    

    try:
        if len(words) < 8:
            print('Пароль не надежный.\nВведите больше 8 символов')
            return input_password()
        else:
            for w in words:
                if w.islower() :
                    continue
                if w.isupper() :
                    continue
                if w.isdigit() :
                    continue
                if w in punctuation:  #***
                    return words
            print('Пароль не надежный.')
            return input_password()
    finally:
        pas_exposure = input('Подтверждение пароля: ')
        if pas_exposure == words:
            return words
        print('Пароли не совпадают.')
        return input_password()

main()


