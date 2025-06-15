import random
from check_input import check_input
from result import result

def game_round():

    words = ['apple','bread','candy','dream','eagle','flame','grape','house','input','joker']
    secret_word = random.choice(words)

    tries = 6
    len_secret_word = len(secret_word)

    print("Welcome to Wordle!")
    print(f"Guess the {len_secret_word}-letter word. You have {tries} tries.")

    while tries > 0:
        try: 
            guess = input(f"Attempt {7 - tries}/6 – Enter guess: ").strip().lower()


            status = check_input(guess, secret_word, len_secret_word)
            if status == "wrong_length":
                continue
            elif status == "win":
                break
 
            
            result_list = result(len_secret_word, guess, secret_word)


            print("Result:", ' '.join(result_list))
            tries -= 1
        except:
            print("An error occured. Follow all the instructions. ")

    else:
        print("You lose! The word was:", secret_word)
