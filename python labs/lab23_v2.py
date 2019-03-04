#load csv file

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
#create contact list   
contacts = []
#use first line to create the keys
keys =lines[0].split(",")
#convert each list into its group of values and create dict for each contact 
for i in range(1,(len(lines))):
    line = lines[i].split(",")
    entry = dict(zip(keys, line))
    contacts.append(entry)

#CRUD functions:
def create():
    # name = input("What is your name?: ")
    f_fruit = input("what is your favorite color?: ")
    f_color = input("what is your favorite fruit?: ")
    line = (name, f_fruit, f_color)
    proceed = input(f"Is {line} correct? (y/n):")
    if proceed == "y":
        entry = dict(zip(keys, line))
        contacts.append(entry)
        return contacts
    else:
        create()
def retrieve():
    # name = input("What is your name?:")
    for i in range(len(contacts)):
        if name == contacts[i]["name"]:
            print(contacts[i])
            return contacts
def update():
    # name = input("What is your name?:")
    value = input(f'Which of these {keys} would you like to update: ')
    new_value = input(f"what is the new value for {value}:")
    proceed = input(f"Is {new_value} correct? (y/n):")
    if proceed == "y":
        if value in keys:
            for i in range(len(contacts)):
                if name == contacts[i]["name"]:
                    contacts[i][value] = new_value
                    return contacts
    else:
        update()
def delete():
    # name = input("What is your name?:")
    for i in range(len(contacts)):
            if name == contacts[i]["name"]:
                proceed = input(f'Are you sure you want to delete {contacts[i]}? (y/n):')
                if proceed == "y":
                    contacts.remove(contacts[i])
                    return contacts


#Crud loop:

while True:
    name = input("What is your name?: ")
    choice = input("Type 'c' to create, 'r' to retrieve, 'u' to update or 'd' to delete an entry: ").lower()
    if choice =='c':
        create()
    elif choice == 'r':
        retrieve()
    elif choice == 'u':
        update()
    elif choice == 'd':
        delete()
    # print(contacts)
    exit_string = input('type x to exit or any key to continue: ')
    if exit_string == 'x':
        break