from game_round import game_round

while True:
    game_round()
    try:
        again = input("Would ypu like to play again? (yes/no) ").strip().lower()
        if again != "yes":
            print("Thanks for the game!")
            break
    except:
        print("Use only latin letters: ")




