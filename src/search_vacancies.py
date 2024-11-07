from typing import Any

import requests

from src.base_class import Api


class SearchVacancies(Api):
    """Класс для поиска вакансий с помощью API"""

    def __init__(self) -> None:
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies: list[Any] = []

    def load_vacancies(self, keyword) -> Any:
        self.params["text"] = keyword
        while self.params.get("page") != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            if response.status_code == 200:
                vacancies = response.json()["items"]
                self.vacancies.extend(vacancies)
                self.params["page"] += 1
        return self.vacancies
