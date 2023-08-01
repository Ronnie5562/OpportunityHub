firstname = input('Enter your first name: ')

lastname = input('Enter your last name: ')

email = input('Enter your email: ')

job_preference = input('What kind of job do you want? ')

with open('users.csv', 'a') as file:
    file.write(f"{firstname}, {lastname}, {email}, {job_preference}")


While True:
    try:
        experience_level = int(input('How many years of experience do you have? '))
    except (ValueError, TypeError):
        print('invalid input')
    else:
        if (experience_level >= 5):
            mentorship_request = input('Do you want to be a mentor? [Yes / No]')
            if (mentorship_request == 'Yes'):
                print('Welcome to the opportunityHub mentors platform')
                with open('mentors.csv', 'a') as file:
                    file.write(f"{firstname}, {lastname}, {email}, {job_preference}")

        else:
            mentee = input('Do you need a mentor? ')
            # function


print('Thank you for joining opportunityHub')