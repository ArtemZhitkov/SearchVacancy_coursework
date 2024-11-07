from abc import ABC, abstractmethod


class Api(ABC):
    """ Абстрактный класс для работы с API по поиску вакансий """
    @abstractmethod
    def load_vacancies(self, keyword: str):
        """ Получение вакансий по поисковому запросу"""
        pass


class FileWorker(ABC):
    """Абстрактный класс для сохранения в файл"""

    @abstractmethod
    def add_vacancy(self, vacancy):
        """Метод добавляет вакансию в существующий файл"""
        pass

    @abstractmethod
    def get_vacancies(self):
        """Метод получает вакансию из файла"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        """Метод удаляет выбранную вакансию"""
        pass

    def save_to_file(self, vacancies_list):
        pass
