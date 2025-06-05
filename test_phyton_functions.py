from datetime import time
import pytest

def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    is_dark_theme = None

    current_time = time(hour=23)
    #  переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)
    if 0<=current_time.hour<6:
        is_dark_theme = True
    elif 22<=current_time.hour<=23:
        is_dark_theme = True
    else:
        is_dark_theme = False
    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    is_dark_theme = None
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True
    # переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную
    if dark_theme_enabled_by_user == None:
        if 0 <= current_time.hour < 6 or 22 <= current_time.hour <= 23:
            is_dark_theme = True
        else:
            is_dark_theme = False
    elif dark_theme_enabled_by_user == True:
        is_dark_theme = True
    elif dark_theme_enabled_by_user == False:
        is_dark_theme = False

    print(f'Включена ли темная тема - {is_dark_theme}')
    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    #  найдите пользователя с именем "Olga"
    suitable_users = []
    for i in range((len(users))):
         if users[i]["name"] == "Olga":
             suitable_users = users[i]
    assert suitable_users == {"name": "Olga", "age": 45}

    #  найдите всех пользователей младше 20 лет
    suitable_users = []
    for i in range((len(users))):
        if users[i]["age"] <20:
            suitable_users.append(users[i])
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]

# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"
def print_function_name_and_args(func, *args):  # функция принимает имя функции и значения аргументов
        func_name = func.__name__.replace('_',' ').title()  # получаем имя функции и преобразуем его в читаемый вид (заменяем символ подчеркивания на пробел, делаем первую букву заглавной)
        args_name = ", ".join([*args])  # преобразуем значения аргументов в строку
        print(f"{func_name} [{args_name}]")  # печатаем имя функции и значения аргументов
        return f"{func_name} [{args_name}]"  # возвращаем строку с именем функции и значениями аргументов


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = print_function_name_and_args(open_browser,"Chrome")
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = print_function_name_and_args(go_to_companyname_homepage,"https://companyname.com")
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = print_function_name_and_args(find_registration_button_on_login_page,"https://companyname.com/login", "Register")
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
