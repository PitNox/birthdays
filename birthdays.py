birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Rowan Atkinson': '01/6/1955'}

def print_birthdays():
    
    print('Welcome to the birthday dictionary. We know the birthdays of these people:')
    for name in birthdays:
        print(name)

def return_birthday(name):
    
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))

def name_is_valid(name):
    
    if len(name)>20:
        return False
    
    if name not in birthdays:
        return False
    
    if name.islower():
        return False

    return True


def just_the_surname(name):
    
    if name in birthdays:
        fullname = [name]
        fullname = fullname[0].split()

        return fullname[1]
        
