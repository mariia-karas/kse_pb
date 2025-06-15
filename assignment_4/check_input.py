def check_input(guess, secret_word, len_secret_word):
    if len(guess) != len_secret_word: 
        print("Wrong length. Expected ", len_secret_word)
        return "wrong_length"
    
       
    if guess == secret_word:
        print("You win!!!")
        return "win"

    return "continue"
