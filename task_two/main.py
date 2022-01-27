from classes import Person
import typing


def process_names(items: typing.Iterable) -> typing.Dict:
    """
    The func gets iterable of full names,
    process them and return a dict form of
    {
      <First_surname_letter>:
        {
          <First_name_letter>: [<List of full names>]
        }
    }
    :param items: and iterable of full names
    :return: dict

    Example:
    process_names(("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))

    Output:
{
    "С":{
        "И":["Иван Сергеев", "Инна Серова"],
        "А":["Анна Савельева"]
    },

    "А":{
        "П":["Петр Алексеев"]
    },

    "И":{
        "И":["Илья Иванов"]
    }
}
    """
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
