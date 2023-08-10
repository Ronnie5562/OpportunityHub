# entry point to the programm 

from signup_login import signUp, logIn
from fetch_jobs import get_jobs
from send_to_email import send_email
from user_info import get_professional_domain


print('\t\t\t\t Welcome to opportunityHub Menu driven Application ')


def welcome_users():
    # The entry point of the program
    while True:

        print('''
            1. LogIn
            2. Do not have an account? SignUp
            3. Exit the program
        ''')

        option = input('Choose One [1, 2, 3]: ')
        return option if option in ['1', '2', '3'] else print('Select a valid number [1, 2, 3]')


def ask_for_action():
    print('\t\t\t\t What will you like to do? ')
    print('''
        1. Get Job opportunities ?
        2. Get a mentor ?
        3. logout ?
    ''')
    action = input('Choose One [1, 2, 3]: ')
    return action if action in ['1', '2', '3'] else print('Select a valid number [1, 2, 3]')


# def fetch_job_opportunities():
#     position = input('What position are you looking for? ')
#     country = input('Which country do you need the job in? ')

#     jobs = get_jobs(position, country)
#     print(jobs)


def fetch_and_send_jobs():
    position = input('What position are you looking for? ')
    country = input('Which Location do you need the job in? ')

    job_list = get_jobs(position, country)
    email = input('Enter your email: ')
    send_email(email, job_list[:10], position)


def get_mentors(domain):
    with open('mentors.csv') as db:
        mentors = db.readlines()
        mentors_list = [arr.split(', ') for arr in mentors[1:]]

        your_mentors_list = []
        for mentor in mentors_list:
            if mentor[-1] == domain:
                your_mentors_list.append(mentor)

            if your_mentors_list:
                print(
                    "Here's a list of mentors in your domain that are willing to mentor you")
                for mentor in your_mentors_list:
                    print(mentor)
            else:
                print("We currently don't have a mentor for you")


logged_in = False

while True:
    # Implement it in a way that the app is interactive till the user logs out.
    option = welcome_users()

    if (option == '1'):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        logged_in = logIn(email, password)
    elif (option == '2'):
        signUp()
    elif (option == '3'):
        logged_in = False
        break

    if (logged_in):
        while True:
            action = ask_for_action()
            if (action == '1'):
                fetch_and_send_jobs()
            elif (action == '2'):
                my_domain = get_professional_domain()
                get_mentors(my_domain)
            else:
                break
