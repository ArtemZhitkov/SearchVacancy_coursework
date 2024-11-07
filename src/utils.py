def get_top_n_by_salary(vacancies: list, n: int) -> list:
    """Функция возвращает топ N вакансий по зарплате (N запрашивается у пользователя)"""
    sorted_vacancies = sorted(vacancies, key=lambda x: x.salary)
    return sorted_vacancies[:n]


def filter_vacancies_by_keywords(vacancies: list, keywords: list) -> list:
    """Функция фильтрует вакансии по ключевым словам"""
    if keywords:
        result = []
        for vacancy in vacancies:
            description = vacancy.description
            for word in keywords:
                if word in description:
                    result.append(vacancy)
        return result
    else:
        return vacancies


def print_vacancies(vacancies: list) -> None:
    """Функция выводит в консоль список вакансий"""
    for vacancy in vacancies:
        print(vacancy)
