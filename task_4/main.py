from handlers import parse_user_input,add_contact,update_contact,show_phone,show_all
def main():
    contacts={}
    print("Welcome to the assistant bot!")
    try:
        while True:
            user_input=input('Enter a command: ').strip().lower()
            command,*args=parse_user_input(user_input)

            if command in ['exit','close']:
                print('Goodbye!')
                break
            elif command=='hello':
                print('How can I help you? ')

            elif command=='add' :
                name=args[0]
                is_exist_contact=contacts.get(name,None)

                if is_exist_contact is not None:
                    answer=input(f'Contact with name {name} already exist. Do you want to update contact? y/n ').strip().lower()
                    if answer=='y':
                        print(update_contact(args,contacts))
                    elif answer!='n':
                        print('Wrong command')
                    continue

                else:
                    print(add_contact(args,contacts))
 
                

            elif command=='change':
                print(update_contact(args,contacts))

            elif command=='phone':
                print(show_phone(args[0],contacts))

            elif command=='all':
                print(show_all(contacts))
            else:
                print("Invalid command.")
    except Exception as e:
        print(f'{e} with file')



if __name__=='__main__':
    main()