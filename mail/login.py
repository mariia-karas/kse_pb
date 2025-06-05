import hashlib

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