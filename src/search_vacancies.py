import requests
from src.base_class import Api


class SearchVacancies(Api):
    """ Класс для поиска вакансий с помощью API """

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'per_page': 100}

    def load_vacancies(self, keyword):
        self.__params['text'] = keyword
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        if response.status_code == 200:
            vacancies = response.json()
            return vacancies
        else:
            raise Exception(f"{response.text}")
