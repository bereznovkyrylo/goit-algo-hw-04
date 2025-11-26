def parse_user_input(string):
    command,*args=string.split()
    return command,*args


def add_contact(args,contacts):                
    name=args[0]
    is_exist_contact=contacts.get(name,None)

    if is_exist_contact is not None:
        return f'Contact with name {name} already exist'
    else:            
        name,phone=args
        contacts[name]=phone
        return "Contact added."

def update_contact(args,contacts):
    name,phone=args

    contacts[name]=phone
    return "Contact updated."
  
def show_phone(name,contacts):
    return contacts[name]

def show_all(contacts):
    return list(contacts.items())
