from data import users
from data import emails
from registration import registration
from login import login
from send_email import send_email

def logout():
    return False


user_status = False
user_name = None

while True:

    try: 
        user_choice = int(input("Enter your choice: "))
    except Exception as e:
        print(e)
        user_choice = None
        

    if user_choice == 0:
        break


    elif user_choice == 1:
        if user_status is False:
            print("registration")
            registration(users) 
        else:
             print("You are registered and logged in")


    elif user_choice == 2:
        if user_status is False:
            print("login")
            user_status, user_name = login(users)
        else:
             print("You are registered and logged in")
       

    elif user_choice == 3:
        if user_status is True:
            print("send_email")
            send_email(users, emails, user_name)
        else:
             print("You are not logged in to send email")


    elif user_choice == 4:
        if user_status is True:
            user_status = logout()
        else:
             print("You are not logged in to logged out")
        print("logout")


    elif user_choice == 5:
         print(users)