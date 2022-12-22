from collections import UserDict
import re

"""
Класи бота помічника.
Record
AddressBook(UserDict)
Field
Name(Field)
Phone(Field)
Birthday(Field)
AddressContact(Field)
EmailContact(Field)
Notes(Field)
"""


class Record:
    """
    Клас Record, який відповідає за логіку додавання/видалення/редагування необов'язкових полів та зберігання
    обов'язкового поля Name.
    При ініціалізації класу створюється ім'я класу Name, та список номерів телефоні, в який будуть записані номери
    телефонів класу Phone. Поле Birthday створюється пустим, поле Email створюється порожній список в якому будуть
    екземпляри класу EmailContact, поле
    """

    def __init__(self, name):
        self.name = Name(name)
        self.phone = []
        self.notes = []
        self.birthday = None
        self.address = None
        self.email = None


class AddressBook(UserDict):
    """
    Клас книги контактів.
    Батьківський клас UserDict.
    """
    pass


class Field:
    """
    Батьківський клас для Name, Phone, Birthday, AddressContact, EmailContact.
    """

    def __init__(self, value):
        self.value = value


class Name(Field):
    """
    Ім'я контакта.
    """

    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    """
    Номер телефону контакта.
    Додається до списку phones, який створюється при ініціалізації класу Record.
    """

    def __init__(self, phone):
        self.__value = None
        super().__init__(phone)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, phone):
        check_match = re.search(
            r"\([0-9]{2}\)\-[0-9]{3}\-[0-9]{1}\-[0-9]{3}|\([0-9]{2}\)\-[0-9]{3}\-[0-9]{2}\-[0-9]{2}", phone)
        if check_match:
            self.__value = phone
        else:
            self.__value = None


class Birthday(Field):
    """
    День народження контакта.
    Додається до списку birthday, який створюється при ініціалізації класу Record.
    """

    def __init__(self, birthday):
        self.__value = None
        super().__init__(birthday)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, birth_day):
        check_match = re.search(r"[0-9]{4}\-[0-9]{2}\-[0-9]{2}", birth_day)
        if check_match:
            self.__value = birth_day
        else:
            self.__value = None


class AddressContact(Field):
    """
    Адрес контакта.
    Додається до списку address, який створюється при ініціалізації класу Record.
    """

    def __init__(self, address):
        super().__init__(address)


class EmailContact(Field):
    """
    Email контакта.
    Додається до списку email_contact, який створюється при ініціалізації класу Record.
    """

    def __init__(self, email):
        self.__value = None
        super().__init__(email)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, email):
        check_match = re.search(
            r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", email)
        if check_match:
            self.__value = email
        else:
            self.__value = None


class Notes(Field):
    """
    Нотатки до контакта.
    Додаються до списку notes_contact, який створюється при ініціалізації класу Record.
    """

    def __init__(self, note, tag):
        super().__init__(note)
        self.tag = tag
