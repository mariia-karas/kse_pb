import random
import string
def generate_password(length= 12, allow_symbols=False):
    symbols = string.ascii_letters + string.digits
    password_list = random.choices(symbols, k = length)
    symbols_with_punctuation = string.ascii_letters + string.digits + string.punctuation
    password_list_with_punct = random.choices(symbols_with_punctuation, k = length)

    if allow_symbols == False:
        print(password_list)
    else:
        print(password_list_with_punct)


generate_password(length=15)