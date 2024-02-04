contacts={}

# обробляємо помилки введення користувача
def input_error(func):
    def inner(*args, **kwargs):
        function_name = str(func).split(" ")[1]
        try:
            return func(*args, **kwargs)
        except ValueError:
            if function_name == "add_contact":
                return  "\nPlease, enter again your command to add contact correctly. \
                \nGive me name and phone please\n"
            elif function_name == "change_contact":
                return  "\nPlease, enter again your command to change contact correctly. \
                \nGive me name and phone please\n"
        except IndexError:
            if function_name == "show_phone":
                return "\nPlease, enter again your command to show contact correctly. \
                \nGive me name please\n"
        except KeyError:
            if function_name == "show_phone":
                return "\nThere is no such contact yet. Add it please.\n"
    return inner

# функція розбиття введення користувача на
# окрема команду cmd та
# аргументи *args, введені після команди
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# функція додавання контакту до бази
@input_error
def add_contact(args, contacts: {}):
    name, phone = args
    contacts[name] = phone
    return "Contact added.\n"

# функція зміни номера контакту
@input_error
def change_contact(args, contacts: {}):
    name, phone = args
    contacts[name] = phone
    return "Contact updated.\n"

# функція показу номера контакта за його ім'ям
@input_error
def show_phone(args, contacts: {}):
    name = args[0]
    return f"Phone number for user {name} is -> {contacts[name]}\n"

# функція показу всіх контактів бази
def show_all(contacts: {}):
    all_contacts=""
    if len(contacts)>0:
        count_number=1
        for name, number in contacts.items():
            all_contacts+=str(count_number)+" - "+name+" "+str(number)+"\n"
            count_number+=1
        return all_contacts
    else:
        return "\nYour contacts database is empty!\nAdd contacts please.\n"

# головна логіка
def main():
    print("\nWelcome to the assistant bot!\n")
    while True:
        user_input = input("Enter your command: ")
        if user_input is not None:
            if  user_input in ["close", "exit"]:
                print("\nGood bye!\n")
                break
            elif user_input=="hello":
                print("\nHow can I help you?\n")
            elif len(user_input)==0:
                print("\nYou entered empty command! Please, try again.\n")
                continue
            else:
                entered_command, *args = parse_input(user_input)
                if entered_command=="add":
                    print(add_contact(args, contacts))
                elif entered_command=="change":
                    print(change_contact(args, contacts))
                elif entered_command=="phone":
                    print(show_phone(args, contacts))
                elif entered_command=="all" \
                    and len(args)==0:
                    print(show_all(contacts))
                else:
                    print("Invalid command.\n")

if __name__ == "__main__":
    main()    
