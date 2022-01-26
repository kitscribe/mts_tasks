from classes import Person


def process_names(items: iter) -> dict:
    persons = [Person(*item.split()) for item in items]
    res = dict()

    for person in persons:
        fls = person.surname_first_letter  # first letter of surname
        fln = person.name_first_letter  # first letter of name

        if fls not in res:
            res[fls] = dict()
        if fln not in res[fls]:
            res[fls][fln] = list()
        res[fls][fln] += [person.full_name]

    return res


if __name__ == '__main__':
    test_data = ("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
    result = process_names(test_data)
    print(result)
