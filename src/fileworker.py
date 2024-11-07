import json
import os
from typing import Any

from config import DATA_PATH
from src.base_class import FileWorker
from src.vacancy import Vacancy


class JSONSWorker(FileWorker):
    """Класс сохраняет данные в JSON-файл"""

    def __init__(self, filename="vacancies.json") -> None:
        self.__filename = filename
        self.file_path = os.path.join(DATA_PATH, self.__filename)

    def save_to_file(self, vacancies) -> None:
        """Метод сохраняющий список вакансий в JSON-файл"""
        result = []
        for vacancy in vacancies:
            vacancy_dict = {
                "name": vacancy.name,
                "url": vacancy.url,
                "area": vacancy.area,
                "salary": vacancy.salary,
                "description": vacancy.description,
            }
            result.append(vacancy_dict)
        with open(self.file_path, "a+", encoding="utf-8") as file:
            json.dump(result, file, ensure_ascii=False, indent=4)

    def get_vacancies(self) -> Any:
        """Метод получает список вакансий из файла"""
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            vacancies = []
            for item in data:
                vacancies.append(Vacancy(**item))
            return vacancies

    def add_vacancy(self, vacancies) -> None:
        """Метод добавляет вакансии в существующий файл"""

        with open(self.file_path, "r+") as file:
            data = json.load(file)
            for vacancy in vacancies:
                data.append(
                    {
                        "name": vacancy.name,
                        "url": vacancy.url,
                        "area": vacancy.area,
                        "salary": vacancy.salary,
                        "description": vacancy.description,
                    }
                )
            file.seek(0)
            json.dump(data, file, ensure_ascii=False, indent=4)

    def delete_vacancy(self, vacancy) -> None:
        """Метод удаляет выбранную вакансию"""
        with open(self.file_path, "r+") as file:
            data = json.load(file)
            data = list(filter(lambda x: x.get("name") != vacancy.name, data))
            file.seek(0)
            json.dump(data, file, ensure_ascii=False, indent=4)
