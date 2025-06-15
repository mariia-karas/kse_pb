import random

words = ['apple',    'bread','candy',    'dream','eagle','flame','grape','house','input','joker']
x = random.random()
y = x * len(words)
z = int(y)
secret_word = words[z]

tries = 6
wl = len(secret_word)
w = secret_word

print("Welcome to Wordle!")
print("Guess the",wl,"-letter word. You have", tries, "tries.")

while tries!=0:
    guess = input("Attempt "+str(7 - tries)+"/6 – Enter guess: ").lower()
    
    if len(guess)!=wl:
        print("Wrong length. Expected", wl)
        continue

    if guess==w:
        print("You win!!!")
        break

    result=[]; i=0
    while i<wl:
        guess[i]
        if guess[i] ==w[i]:
             result.append("["+guess[i].upper()+"]")
        elif guess[i]in w:
            result.append("("+guess[i]+")")
        else:
            result.append(" "+guess[i]+" ")
        i+=1


   
    print("Result:", ' '.join(result))
    tries = tries - 1
else:
    final = secret_word
    print("You lose! The word was:", final)