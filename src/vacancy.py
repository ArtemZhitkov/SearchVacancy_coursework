import json


class Vacancy:
    """Класс для работы с вакансиями"""
    __slots__ = (
        "name",
        "url",
        "area",
        "salary",
        "description"
    )

    def __init__(self, name, url, area, salary, description):
        self.name = name
        self.url = url
        self.area = area
        self.salary = salary
        self.description = description
        self.__validate()

    def __validate(self):
        """Метод валидации входных данных"""
        if not self.salary:
            self.salary = "Не указана"

        if not self.description:
            self.description = "Описание отсутствует"

        if not self.area:
            self.area = "Регион не указан"

    @classmethod
    def cast_to_object_list(cls, vacancies):
        """ Метод преобразовывает набор данных из JSON в список объектов """
        data = json.loads(vacancies)
        vacancies_list = []
        for item in data["items"]:
            name = item.get("name")
            url = item.get("alternate_url")
            area = item.get("area").get("name")
            salary = item.get("salary", "Не указана").get("from")
            description = item.get("snippet", "Отсутствует").get("requirement", "Отсутствует")
            vacancies_list.append(cls(name, url, area, salary, description))
        return vacancies_list

    def __lt__(self, other):
        """Метод сравнивает между собой по зарплате и возвращает вакансию с большей зарплатой"""
        if self.salary == "Не указана" or other.salary == "Не указана":
            print("Не удалось выполнить сравнение т.к. зарплата не указана")

        else:
            if self.salary < other.salary:
                return other.salary
            else:
                return self.salary

    # def __eq__(self, other):
    #     if self.salary == "Не указана" or other.salary == "Не указана":
    #         print("Не удалось выполнить сравнение т.к. зарплата не указана")
    #     else:
    #         if self.salary == other.salary:
    #             print(f"Зарплата {self.name} равна зарплате {other.name}")
