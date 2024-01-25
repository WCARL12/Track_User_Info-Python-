import csv
FILE = 'Courses\python_studio_code\Python_assignment\Assignment_3\contacts.csv'

def display_command():
    print("Contact Manager\n")
    print('COMMAND MENU')
    print('list - Display all contacts')
    print('view - View a contact')
    print('add - Add a contact')
    print('del - Delete a contact')
    print('exit - Exit a program')

def file_to_list():
    contact_list = []
    with open(FILE, 'r') as csv_file:
        csv_read = csv.reader(csv_file)
        for line in csv_read:
            contact_list.append(line)
    return contact_list

def list_command(contact_list):
    for index, contact in enumerate(contact_list):
        print(f'{index+1}. {contact[0]}')

def view_command(contact_list):
    number = int(input('Number: '))
    for index, contacts in enumerate(contact_list):
        if index == (number - 1):
            print(f'Name: {contacts[0]}')
            print(f'Email: {contacts[1]}')
            print(f'Phone: {contacts[2]}')

def add_command():
    name = input(f"Name: ")
    email = input(f"Email: ")
    phone = input(f"Phone: ")
    add_list= [name, email, phone]
    with open(FILE, 'a', newline='') as csv_file:
        csv_write = csv.writer(csv_file)
        csv_write.writerow(add_list)

def delete_command(contact_list):
    list_command(contact_list)
    delete_value = int(input('Give the number of the contact to delete: '))
    for index, contacts in enumerate(contact_list):
        if index == (delete_value - 1):
            contact_list.pop(index)
    with open(FILE, 'w', newline='') as csv_file:
        csv_write = csv.writer(csv_file)
        csv_write.writerows(contact_list)


def main():
    display_command()
    command = ''
    
    while True:
        contact_list = file_to_list()
        print()
        command = input('Command: ')

        if command == 'list':
            list_command(contact_list)

        elif command == 'view':
            view_command(contact_list)
        
        elif command == 'add':
            add_command()
        
        elif command == 'del':
            delete_command(contact_list)

        elif command == 'exit':
            break
    print('Bye!')

if __name__ == '__main__':
    main()
