from insert_to_db import save_to_db


def get_professional_domain():
    professional_domains = {
        "1": "Technology (Tech)",
        "2": "Healthcare",
        "3": "Finance",
        "4": "Education",
        "5": "Engineering",
        "6": "Marketing",
        "7": "Law",
        "8": "Entertainment",
        "9": "Science",
        "10": "Hospitality"
    }

    for x, y in professional_domains.items():
        print(f"\t{x}: {y}")
    
    while True:
        domain_num = input('Pick your domain from 1-10: ')
        
        if domain_num in professional_domains.keys():
            domain = ''
            for x, y in professional_domains.items():
                if domain_num == x:
                    domain = y

            return domain


def get_password():
    while True:
        password = input('Enter a secret password: ')
        confirm_password = input('Confirm your password: ')
        if (password == confirm_password):
            print('\033[32mPasswords match\033[0m')
            return password
        print('\033[31mPasswords do not match X\033[0m')


def get_user_details():
    # New users' personal information.
    firstname = input('Enter your first name: ')
    lastname = input('Enter your last name: ')
    email = input('Enter your email: ')
    job_preference = input('What kind of job do you want? ')
    password = get_password()
    my_domain = get_professional_domain()
    return firstname, lastname, email, job_preference, my_domain, password



# def save_to_users_csv(firstname, lastname, email, job_preference, my_domain, password):
#     # Saves the users' information into a file
#     with open('users.csv', 'a') as file:
#         file.write(
#             f"\n{firstname}, {lastname}, {email}, {job_preference}, {my_domain}, {password}"
#         )


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
    firstname, lastname, email, job_preference, my_domain, password = get_user_details()
    save_to_db(firstname, lastname, email, job_preference, my_domain, password=password, table="Users")

    experience_level = get_experience_level()
    if experience_level >= 5:
        mentorship_request = input('Do you want to be a mentor? [Yes / No]: ')
        if mentorship_request.lower() == 'yes':
            print('Welcome to the opportunityHub mentors platform')
            my_domain = get_professional_domain()
            # Save mentor details similarly to the Mentors table"
            save_to_db(firstname, lastname, email, job_preference, my_domain, exp_level=experience_level, table="Mentors")
            
            # with open('mentors.csv', 'a') as file:
            #     file.write(
            #         f"\n{firstname}, {lastname}, {email}, {job_preference}, {experience_level}, {my_domain}"
            #     )

    print('Welcome to the opportunity hub')


if __name__ == "__main__":
    main()


# Used for testing
# Bernice, Akudbilla, b.akudbilla@alustudent.com, Data analyst
# Ronald, Abimbola, r.abimbola@alustudent.com, Software engineer