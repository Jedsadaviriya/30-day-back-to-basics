# contact book
# function 1: add contacts
# function 2: lookup contact
# function 3: delete contacts
# fucntion 4: list all contacts

contacts = {}

def add_contact(contacts, name, phone, email):
    lowername = name.lower()
    if lowername in contacts:
        while True:
            yn = input("This contact name already exists, do you want to overwrite it(y) or cancel(n)?: ")
            if yn == "y":
                contacts[lowername] = {"phone": phone, "email": email}
                break
            elif yn == "n":
                break
            else:
                print(f"{yn} is not an option")
    else:
        contacts[lowername] = {"phone": phone, "email": email}


add_contact(contacts, "Alice", "111", "a@email.com")
add_contact(contacts, "Alice", "222", "a2@email.com")  # this should trigger the overwrite prompt
add_contact(contacts, "Fish", "4750", "4750@email.com")

print(contacts)

def lookup_contact(contacts, name):
    lowername = name.lower()
    if lowername in contacts:
        results = contacts[lowername]
    else:
        results = f"{lowername} doesn't exist in the contacts list."
    return results

print(lookup_contact(contacts, "Alice"))
print(lookup_contact(contacts, "bob"))


def delete_contact(contacts, name):
    lowername = name.lower()
    if lowername in contacts:
        del contacts[lowername]
        results = f"{name} has been deleted"
    else:
        results = f"{name} does not exist"
    return results

print(delete_contact(contacts, "Alice"))


def list_contacts(contacts):
    results = []
    for key in contacts:
        results.append(f"{key}:  {contacts[key]}")
    return results
    

add_contact(contacts, "Bob", "222", "b@email.com")

print(list_contacts(contacts))
