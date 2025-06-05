import hashlib
def registration(users):
            login = input("Enter the login: ")
            password = input("Enter your password: ")
            password_hash = hashlib.sha256("{}".format(password).encode()).hexdigest()
            if login in users:
                print("User name is alredy taken")
            else: 
                users.update({login: password_hash})

