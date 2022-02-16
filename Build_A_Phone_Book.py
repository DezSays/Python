#I am unsure how to upload this as an mp4, so I will just be uploading to git.

phonebook = {
    'Alice':'703-493-1834',
    'Bob':'857-384-1234',
    'Beth':'484-584-2923',
    'Dez':'706-301-6789',
    'Dwight':'362-852-7426'
}

def searchName():
    name = input("Search for a name ")
    
    if name in phonebook:
        print(f'{name} {phonebook[name]}')
    else: 
        print("I'm sorry, I cannot seem to find that contact. ")

def addContact():
    name = input("Enter a name ")
    phonenumber = input("Enter a phone number: ")
    
    phonebook[name] = phoneNumber
def deleteContact():
    print(f'''
Delete Contacts 
''')
    name = input("Insert a name to delete: ")
    if name in phonebook:
        del phonebook[name]
    else:
        print("No contact to delete :( ")
def listAllEntries():
    print('''
Phone Book Contacts
''')
    for name, phonenumber in phonebook.items():
        print(f'{name}\t\t{phonenumber}')


def menu():
    selection = int(input("""
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit    
"""))
    
    return selection 

endProgram = False

while not endProgram:
    
    selection = menu()
    
    
    if selection == 1:
        searchName()
    elif selection == 2:
        addContact()
    elif selection == 3:
        deleteContact()
    elif selection == 4:
        listAllEntries()
    elif selection == 5:
        endProgram = True




