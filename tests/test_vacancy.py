from src.vacancy import Vacancy


def test_vacancy_init(vacancy_test):
    assert vacancy_test.name == "Фронтенд разработчик"
    assert vacancy_test.url == "https://hh.ru/vacancy/109570768"
    assert vacancy_test.area == "Ташкент"
    assert vacancy_test.salary == 2000000
    assert vacancy_test.description == "Знания HTML, CSS, JS, Jquery."


def test_vacancy_validate(vacancy_test_2):
    assert vacancy_test_2.name == "Фронтенд разработчик"
    assert vacancy_test_2.url == "https://hh.ru/vacancy/109570768"
    assert vacancy_test_2.area == "Регион не указан"
    assert vacancy_test_2.salary == 0
    assert vacancy_test_2.description == "Описание отсутствует"


def test_cast_to_object_list(json_data):
    result = Vacancy.cast_to_object_list(json_data)
    assert len(result) == 2
    assert result[0].name == "React Front-End Developer (Frontend разработчик)"
    assert result[0].url == "https://hh.ru/vacancy/109792373"
    assert result[0].area == "Санкт-Петербург"
    assert result[0].salary == 0
    assert result[0].description == ("Базовые знания HTML / CSS / JavaScript. React / React Native. "
                                     "English (на уровне понимания технических текстов). Русский язык (для общения). ")


def test_vacancy_str(vacancy_test, vacancy_test_2):
    assert str(vacancy_test) == ('Фронтенд разработчик: Знания HTML, CSS, JS, Jquery., Регион:Ташкент, '
                                 'Зарплата: 2000000, Ссылка: https://hh.ru/vacancy/109570768')
    assert str(vacancy_test_2) == ('Фронтенд разработчик: Описание отсутствует, Регион:Регион не указан, '
                                   'Зарплата: Не указана, Ссылка: https://hh.ru/vacancy/109570768')


def test_vacancy_comparison(vacancy_test, vacancy_test_2):
    result = vacancy_test < vacancy_test_2
    assert result is False
    result2 = vacancy_test_2 < vacancy_test
    assert result2 is True
