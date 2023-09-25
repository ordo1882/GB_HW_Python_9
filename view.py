import text

def main_menu():
    print(text.main_menu[0])
    for i in range(len(text.main_menu)):
        if i:
            print(f'\t{i:>3}. {text.main_menu[i]}')
    while True:
        choice = input(text.input_main_menu)
        if choice.isdigit() and 0 < int(choice) < len(text.main_menu):
            return choice
        print(text.input_main_menu_error)


def print_message(msg: str):
    print('\n' + '='*len(msg))
    print(msg)
    print('='*len(msg) + '\n')


def show_contacts(book: dict, msg: str):
    if book:
        lens = [contact.len_fields() for contact in book.values()]
        max_size = [max(field) for field in zip(*lens)]
        print('\n' + '='* (sum(max_size) + 10))
        for u_id, contact in book.items():
            contact = contact.to_list()
            contact_str = '   '.join([f'{contact[i]:<{max_size[i]}}' for i in range(len(contact))])
            print(f'{u_id:>2} {contact_str}')
        print('=' * (sum(max_size) + 10) + '\n')
    else:
        print_message(msg)


def input_new_contact(msg: list) -> list[str, str, str]:
    contact = []
    for field in msg:
        contact.append(input(field))
    return contact


def input_info(msg: str):
    return input(msg)