def ask_for_action():
    # The entry point of the program
    while True:
        print('Do you have an account? ')
        print('1. SignUp: ')
        print('2. SignIn: ')
        option = input('')


def get_user_details():
    # New users' personal information.
    firstname = input('Enter your first name: ')
    lastname = input('Enter your last name: ')
    email = input('Enter your email: ')
    job_preference = input('What kind of job do you want? ')
    return firstname, lastname, email, job_preference


def save_to_users_csv(firstname, lastname, email, job_preference):
    # Saves the users' information into a file
    with open('users.csv', 'a') as file:
        file.write(f"\n{firstname}, {lastname}, {email}, {job_preference}")


def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def get_experience_level():
    while True:
        experience_level = input('How many years of experience do you have? ')
        if is_integer(experience_level):
            return int(experience_level)
        print('Invalid input. Please enter a valid number.')


def main():
    firstname, lastname, email, job_preference = get_user_details()
    save_to_users_csv(firstname, lastname, email, job_preference)

    experience_level = get_experience_level()
    if experience_level >= 5:
        mentorship_request = input('Do you want to be a mentor? [Yes / No]')
        if mentorship_request.lower() == 'yes':
            print('Welcome to the opportunityHub mentors platform')
            # Save mentor details similarly to "mentors.csv"
            with open('mentors.csv', 'a') as file:
                file.write(
                    f"\n{firstname}, {lastname}, {email}, {job_preference}, {experience_level}")
    else:
        mentee_request = input('Do you need a mentor? [Yes / No]')
        # Function to handle mentee request

    print('Welcome to the opportunity hub')


if __name__ == "__main__":
    main()

# Bernice, Akudbilla, b.akudbilla@alustudent.com, Data analyst
# Ronald, Abimbola, r.abimbola@alustudent.com, Software engineer
