import hashlib
def registration(users):
    login = input("Enter the login: ")
    password = input("Enter your password: ")
    password_hash = hashlib.sha256("{}".format(password).encode()).hexdigest()
    print(password_hash)

