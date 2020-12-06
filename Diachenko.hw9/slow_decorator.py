"""
    Напишите декоратор, который будет замедлять выполнение функции на 5 секунд.

    Если функция выполняется более 10 секунд (с учетом замедления), то
    дополнительно выводить сообщение f'{func.__name__} - very slow function'
"""
import time


# создаем функцию-декоратор
def timed(func):

    def wrapper(*args, **kwargs):
        print('Выполняется функция', func.__name__)
        start = time.time()
        result = func(*args, **kwargs)  # выполняется задекорированная функция
        end = time.time() - start
        if round(end, 2) > 10:
            print(f'{func.__name__} - very slow function')
        else:
            print(round(end, 2), 'seconds')
        return result

    return wrapper


@timed
def summ(a, b):
    time.sleep(5)
    return a + b


result = summ(10, 5)
print('10 + 5 =', result)
