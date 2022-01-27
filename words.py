import random

def load_words():
    a=["python",  "maths", "science", "himachal", "apple", "banana", "ridhu", "milk"]
    return a
    # WORDLIST_FILENAME =("words.txt")
    # inFile = open(WORDLIST_FILENAME)
    # line = inFile.readline()
    # word_list = line.split()  
    # return word_list

def choose_word():

    word_list = load_words()
    secret_word = random.choice(word_list)
    # print(secret_word)
    # print(len(secret_word))
    secret_word = secret_word.lower()

    return secret_word

