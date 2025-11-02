def parse_user_input(string):
    command,*args=string.split()
    return command,*args


def add_contact(args,contacts):
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
    #return contacts.values() better for task requirements
    for key in contacts:
        print(f"{key}: {contacts[key]}") # better for visibility