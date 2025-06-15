def result(len_secret_word, guess, secret_word):
    result=[]

    for i in range(len_secret_word):
        if guess[i] == secret_word[i]:
             result.append("["+guess[i].upper()+"]")

        elif guess[i]in secret_word:
            result.append("("+guess[i]+")")

        else:
            result.append(" "+guess[i]+" ")
        i+=1

    return result