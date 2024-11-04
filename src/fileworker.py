import json
import os

from config import DATA_PATH
from src.base_class import FileWorker
from src.vacancy import Vacancy


class JSONSWorker(FileWorker):
    """Класс сохраняет данные в JSON-файл"""

    def __init__(self, filename):
        self.file_path = os.path.join(DATA_PATH, filename)

    def get_vacancies(self):
        """Метод получает список вакансий из файла"""
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return Vacancy.cast_to_object_list(data)

    def add_vacancy(self, vacancy):
        """Метод добавляет вакансию в существующий файл"""

        with open(self.file_path, "a+") as file:
            vacancy_dict = {
                "name": vacancy.name,
                "url": vacancy.url,
                "area": vacancy.area,
                "salary": vacancy.salary,
                "description": vacancy.description
            }
            if vacancy_dict not in json.load(file):
                json.dump(vacancy_dict, file, ensure_ascii=False, indent=4)
            else:
                print("Вакансия уже существует")

    def delete_vacancy(self, vacancy):
        """Метод удаляет выбранную вакансию"""
        with open(self.file_path, "a+") as file:
            data = list(filter(lambda x: x.get("name") != vacancy.name, file))
            json.dump(data, file, ensure_ascii=False, indent=4)
