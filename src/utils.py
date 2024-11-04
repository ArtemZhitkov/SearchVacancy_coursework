import json
import os

from config import DATA_PATH


def save_to_file(filename: str, vacancies: list) -> None:
    """Функция сохраняющая список вакансий в JSON-файл"""
    path = os.path.join(DATA_PATH, filename)
    result = []
    for vacancy in vacancies:
        vacancy_dict = {
            "name": vacancy.name,
            "url": vacancy.url,
            "area": vacancy.area,
            "salary": vacancy.salary,
            "description": vacancy.description
        }
        result.append(vacancy_dict)
    with open(path, "a", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=4)


def get_vacancies_by_salary_range(vacancies: list, salary_range: str):
    """Функция фильтрует вакансии входящие в диапазон зарплат"""
    salary_from = int(salary_range.split("-")[0])
    salary_to = int(salary_range.split("-")[1])
    return list(filter(lambda x: salary_from <= x.salary <= salary_to, vacancies))


def get_top_n_by_salary(vacancies: list, n: int = 5) -> list:
    """Функция возвращает топ N вакансий по зарплате (N запрашивается у пользователя), по умолчанию N = 5"""
    sorted_vacancies = sorted(vacancies, key=lambda x: x.salary)
    return sorted_vacancies[:n]


def filter_vacancies_by_keywords(vacancies: list, keywords: list) -> list:
    """Функция фильтрует вакансии по ключевым словам"""
    return list(filter(lambda x: x.description in keywords, vacancies))

