from datetime import datetime
import requests


FILE_PATH = 'decoratorlogs.txt'


def parametrized_decor(parameter):
    def decor(foo):
        def new_foo(*args, **kwargs):
            date_time = datetime.now()
            func_name = foo.__name__
            result = foo(*args, **kwargs)
            with open(parameter, 'w', encoding='utf-8') as file:
                file.write(f'Дата/время: {date_time}\n'
                           f'Имя функции: {func_name}\n'
                           f'Аргументы: {args, kwargs}\n'
                           f'Результат: {result}\n')
            return result
        return new_foo
    return decor


@parametrized_decor(FILE_PATH)
def foo(*args, **kwargs):
    url = ','.join(args)
    response = requests.get(url=url)
    return response.status_code


if __name__ == '__main__':
    foo('https://github.com/')
