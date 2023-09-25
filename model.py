from copy import deepcopy

class Contact:
    def __init__(self, name: str, phone: str, comment: str) -> None:
        self.name = name
        self.phone = phone
        self.comment = comment

    def for_save(self):
        return f'{self.name};{self.phone};{self.comment}'
    
    def find(self, word: str) -> bool:
        for item in [self.name, self.phone, self.comment]:
            if word.lower() in item.lower():
                return True
        return False
    
    def __add__(self, other):
        if isinstance(other, Contact):
            if other.name:
                self.name = other.name
            if other.phone:
                self.phone = other.phone
            if other.comment:
                self.comment = other.comment
        return self

    def len_fields(self) -> tuple[int, int, int]:
        return len(self.name), len(self.phone), len(self.comment)


class PhoneBook:
    def __init__(self, path: str = 'phone_book.txt') -> None:
        self.phone_book = {}
        self.original_book = {}
        self.path = path

    def open_file(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            contacts = file.readlines()
        for u_id, contact in enumerate(contacts, 1):
            contact = contact.strip().split(';')
            self.phone_book[u_id] = Contact(*contact)
        self.original_book = deepcopy(self.phone_book)


    def save_file(self):
        contacts = [contact.for_save() for contact in self.phone_book.values()]
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write('\n'.join(contacts))


    def next_id(self):
        return max(self.phone_book) + 1


    def new_contact(self, contact: list):
        self.phone_book[self.next_id()] = Contact(*contact)


    def search(self, word: str) -> dict[int, list[str, str, str]]:
        result = {}
        for u_id, contact in self.phone_book.items():
            if contact.find(word):
                result[u_id] = contact
        return result


    def edit(self, u_id: int, new: list) -> str:
        new = Contact(*new)
        contact = self.phone_book.get(u_id)
        contact += new
        self.phone_book[u_id] = contact
        return contact.name


    def delete(self, u_id: int) -> str:
        return self.phone_book.pop(u_id)[0]