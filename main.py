def email_validator():
    email = str(input('Enter your email: ')).strip()
    is_valid = False

    if email == '':
        print('Email should not be blank')
    else:
        if ' ' in email:
            print('Email should not contain spaces')
        elif '@' not in email:
            print('Email should contain @')
        elif email.count('@') != 1:
            print('Email should contain only one @')
        else:
            split_email = email.split('@')
            if '' in split_email:
                print('Email should not be blank before or after @')
            elif '.' not in split_email[-1]:
                print('Domain should contain a dot')
            elif split_email[-1].endswith('.'):
                print('Email should not end with a dot')
            else:
                is_valid = True

    if is_valid:
        print('Valid email!')
    else:
        print('Invalid email!')

    return is_valid

result = email_validator()