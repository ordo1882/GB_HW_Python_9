import text
import view
import model

def search_func(msg: str):
    word = view.input_info(msg)
    result = model.search(word)
    view.show_contacts(result, text.search_contact_error(word))
    return result

def start():
    while True:
        choice = view.main_menu()
        match choice:
            case '1':
                model.open_file()
                view.print_message(text.open_successful)
            case '2':
                model.save_file()
                view.print_message(text.save_successful)
            case '3':
                view.show_contacts(model.phone_book, text.empty_phone_book_error)
            case '4':
                contact = view.input_new_contact(text.input_new_contact)
                model.new_contact(contact)
                view.print_message(text.contact_successful_result(contact[0], 0))
            case '5':
                search_func(text.input_prompt_action(0))
            case '6':
                if search_func(text.input_prompt_action(1)):
                    u_id = view.input_info(text.input_id_action(1))
                    new_contact = view.input_new_contact(text.input_edit_contact)
                    name = model.edit(int(u_id), new_contact)
                    view.print_message(text.contact_successful_result(name, 1))
            case '7':
                if search_func(text.input_prompt_action(2)):
                    u_id = view.input_info(text.input_id_action(2))
                    confirm_name = model.phone_book.get(int(u_id))[0]
                    if view.input_info(text.confirm_delete_contact(confirm_name)).upper() == 'Y':
                        name = model.delete(int(u_id))
                        view.print_message(text.contact_successful_result(name, 2))
            case '8':
                if model.original_book != model.phone_book:
                    if view.input_info(text.confirm_changes).upper() == 'Y':
                        model.save_file()
                view.print_message(text.good_bye)
                break