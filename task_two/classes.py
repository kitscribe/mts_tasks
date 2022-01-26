class Person:
    """
    A helpful class of Person to easily get
    name, surname, fullname and first letters of them
    """
    def __init__(self, first_name, second_name):
        self._first_name = first_name
        self._second_name = second_name

    def __str__(self):
        return f"{self.name} {self.surname}"

    @property
    def name(self):
        return self._first_name

    @property
    def surname(self):
        return self._second_name

    @property
    def full_name(self):
        return f"{self._first_name} {self._second_name}"

    @property
    def surname_first_letter(self):
        return self._second_name[0].upper()

    @property
    def name_first_letter(self):
        return self._first_name[0].upper()

