main_menu = ['Main menu',
             'Open file',
             'Save file',
             'Show all contacts',
             'Create contact',
             'Find contact',
             'Edit contact',
             'Delete contact',
             'Quit\n']

input_main_menu = 'Choose a command: '
input_main_menu_error = f'Make a choice from 1 to {len(main_menu) - 1}'

open_successful = 'Phone book has been loaded'
save_successful = 'Phone book has been saved'

empty_phone_book_error = 'Phone book is empty or not loaded.'

input_new_contact = ['Enter the name: ', 'Enter the phone number: ', 'Enter the comment:']
input_edit_contact = ['Enter the name or press ENTER (if no changes): ', 
                     'Enter the phone number or press ENTER (if no changes): ', 
                     'Enter the comment or press ENTER (if no changes):']

input_prompt_actions = ['search', 'edit', 'delete']

contact_actions = ['added', 'edited', 'deleted']

confirm_delete_contact = lambda x: f'Do you really want to delete - {x}? (Y/N): '

confirm_changes = 'New changes have been not saved. Do you want to save it? (Y/N): '

good_bye = 'Goodbye!'

def contact_successful_result(name: str, mode: int):
    return f'Contact {name} has been {contact_actions[mode]}.'

def input_prompt_action(mode: int):
    return f'Enter the key word to {input_prompt_actions[mode]}: '

def input_id_action(mode: int):
    return f'Enter ID to {input_prompt_actions[mode]}: '

def search_contact_error(word: str) -> str:
    return f'The prompt {word} is out of the phone book.'