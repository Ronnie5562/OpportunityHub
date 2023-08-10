from user_info import main as user_info_main

def signUp():
    user_info_main()

def logIn(email, password):
    current_user = []
    status = ''
    suceess = False
    with open('users.csv') as db:
        users = db.readlines()
        users_list = [arr.split(', ') for arr in users]
        
        for user in users_list:
            if (user[2] == email and user[5] == password):
                current_user = user
                suceess = True
                break
            elif (user[2] == email):
                status = 'Wrong Password'
            else:
                status = 'User NOT found'
        
        (
            print(status)
            if not current_user
            else print(f"Welcome Back {current_user[0]}")
        )
    return suceess

if __name__ == "__main__":
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    logIn(email, password)