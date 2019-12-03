#Creating a dictionary called 'birthdays' containing famous people's names as key and their birthday date as values.

    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Rowan Atkinson': '01/6/1955'}

#Creating a function 'print_birthdays' to display, through a for loop, the names of the people whose birthday date we have.

def print_birthdays():
    print('Welcome to the birthday dictionary. We know the birthdays of these   people:')
    for name in birthdays:
        print(name)

#Creating a function 'return_birthday' to return the date of the requested famous person in the form of {famous person's name}'s birthday is {famous person's birthday date}; in case the requested famous person is not in our dictionary, we return the message 'Sadly, we don't have {famous person's name}'s birthday'.

def return_birthday(name):
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))

