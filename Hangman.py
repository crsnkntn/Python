from random import randint
from typing import List

# a somewhat limited word bank
words = ["Banana", "Minion", "Peter Parker Picked a Pickled Pepper", "Sea World"]

def get_random_word() -> str:
    global words
    i = randint(0, len(words) - 1)
    return words[i]

def print_hidden_word(word: str, found: List[bool]) -> None:
    output = ""
    for i, n in enumerate(word):
        if found[i]:
            output += n
        elif n == " ":
            found[i] = True
            output += "   "
        else:
            output += "_"
    print('\n{}\n'.format(output))


def hangman() -> None:
    word = get_random_word()
    found = [False] * len(word)
    while False in found:
        print_hidden_word(word, found)
        g = "___"
        while len(g) != 1:
            #print("Guess a letter: ", end='')
            g = input("Guess a letter: ")
        for i, n in enumerate(word):
            if n.lower() == g.lower():
                found[i] = True

    print("You guessed \"{}\" correctly! Play Again?".format(word), end='')
    a = ''
    while a != 'Y' and a != 'n':
        #print("(Y/n)", end='')
        a = input("(Y/n)")

    if a == 'Y':
        hangman()
        


if __name__ == "__main__":
    hangman()