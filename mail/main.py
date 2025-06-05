import hashlib
from data import users
from data import emails

def registration(users):
            login = input("Enter the login: ")
            password = input("Enter your password: ")
            password_hash = hashlib.sha256("{}".format(password).encode()).hexdigest()
            if login in users:
                print("User name is alredy taken")
            else: 
                users.update({login: password_hash})

def login(users):
    name = input("Enter name: ")
    password = input("Password: ")
    password_hash = hashlib.sha256("{}".format(password).encode()).hexdigest()
    if name not in users:
        print("User not registrated:")
    else: 
         if password_hash == users[name]:
              print("You are logged in")
              return True, name
    return False, None
        

def send_email(users, emails, sender):
    recipient = input("enter recipient: ")
    mail = input("Enter some text: ")
    if recipient not in users:
          print("Recipient is not registered")
    else:
         emails.append({"sender": sender, "recipient" : recipient, "email" : mail})
    print(emails)

     


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