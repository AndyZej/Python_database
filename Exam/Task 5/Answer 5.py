
from exam_lib import Book


class EBook(Book):
    def __init__(self, title, author, page_count, size, registration_code):
        # call parent constructor
        super().__init__(title, author, page_count)

        self.size = size

        # private attribute (name-mangled)
        if EBook.check_code(registration_code):
            self.__registration_code = registration_code
        else:
            self.__registration_code = None

    @staticmethod
    def check_code(code):
        return (
            isinstance(code, str) and
            code.isdigit() and
            len(code) == 16
        )

    @property
    def registration_code(self):
        return self.__registration_code

    @registration_code.setter
    def registration_code(self, value):
        if EBook.check_code(value):
            self.__registration_code = value