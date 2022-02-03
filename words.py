import string
import random


def load_words():
    """
    Ye function kaafi jayada words ko load karne mai help karega
    """
    WORDLIST_FILENAME = "words.txt"
    print ("Loading word list from file...")
    inFile = open("/home/bharati/Downloads/e-sreedharan-master_1/e-sreedharan-master/hangman/words.txt", 'r')
    line = inFile.readline()
    word_list = line.split(' ')
    # print(word_list)
    print ("  ", len(word_list), "words loaded.\n")


    # word_list = ["navgurukul", "learning", "kindness"]
    return word_list
# print(load_words())



def choose_word():
    """
    word_list (list): list of words (strings)
    ye function ek word randomly return karega
    """
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()

    return secret_word
# print(choose_word())