def count_words(text):
    words = text.split()
    print(len(words))

count_words("apple mariia you")



def average_word_length(text):
    words = text.split()
    total_length = 0
    for word in words:
        total_length += len(word)

    return total_length/len(words)

