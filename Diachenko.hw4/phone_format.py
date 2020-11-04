phone_number = input('Введите номер телефона: ')
dash_split = ''.join(phone_number.split('-')) #удаляем знак -
space_split = ''.join(dash_split.split(' ')) #удаляем пробел
brackets_split = ''.join(space_split.split('(')) #удаляем скобку (
brackets_split2 = ''.join(brackets_split.split(')')) #удаляем скобку )
plus_split = ''.join(brackets_split2.split('+')) #удаляем знак +
good_number = plus_split

while True :
    if len(good_number) > 10:
        print(str(38)+good_number[-10:])
        break
    else:
        print("Повторите попытку(нехватает символов")
        phone_number = input('Введите номер телефона еще раз: ')
        

        