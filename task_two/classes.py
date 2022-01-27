class Person:
    """
    A helpful class of Person to easily get
    name, surname, fullname and first letters of them
    """
    def __init__(self, first_name: str, second_name: str) -> None:
        self._first_name = first_name
        self._second_name = second_name

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"

    @property
    def name(self) -> str:
        return self._first_name

    @property
    def surname(self) -> str:
        return self._second_name

    @property
    def full_name(self) -> str:
        return f"{self._first_name} {self._second_name}"

    @property
    def surname_first_letter(self) -> str:
        return self._second_name[0].upper()

    @property
    def name_first_letter(self) -> str:
        return self._first_name[0].upper()

