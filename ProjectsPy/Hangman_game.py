import random

def  draw(attempts):
    if(attempts == 10):
        print(attempts-1, "turns are left")
        return print("-----")
    elif(attempts == 9):
        print(attempts - 1, "turns are left")
        return print("-----\n"
      " 0")
    elif(attempts == 8):
        print(attempts - 1, "turns are left")
        print("-----\n"
              " 0\n"
              " |")
    elif(attempts == 7):
        print(attempts - 1, "turns are left")
        print("-----\n"
              " 0\n"
              " |\n"
              "/")
    elif(attempts == 6):
        print(attempts - 1, "turns are left")
        print("-----\n"
              " 0\n"
              " |\n"
              "/ \ ")
    elif(attempts == 5):
        print(attempts - 1, "turns are left")
        print("-----\n"
              "\ 0 \n"
              "  |\n"
              " / \ ")
    elif(attempts == 4):
        print(attempts - 1, "turns are left")
        print("-----\n"
              "\ 0 /\n"
              "  |\n"
              " / \ ")
    elif(attempts == 3):
        print(attempts - 1, "turns are left")
        print("-----\n"
              "\ 0 /|\n"
              "  |\n"
              " / \ ")
    elif(attempts == 2):
        print(attempts - 1, "turns are left")
        print("-----\n"
              "\ 0 /_|\n"
              "  |\n"
              " / \ ")
    elif(attempts == 1):
        print("You're dead!!! End Game!")
        print("-----\n"
              "  0_|\n"
              " /|\ \n"
              " / \ ")


def lenVetword(array, sizeword):
    for i in range(sizeword):
        array.append("_")

def verifyLetter(letter, word, sizeword, array):
    hit = 0
    for i in range(sizeword):
        if(letter == word[i]):
            array[i] = letter
            hit+=1
    return array, hit

def hangman():
    words = ["amada", "chair", "window", "keyboard", "smartphone", "table", "mouse"]
    finding = []
    random_word = random.choice(words)
    Amount_attempts = 10
    sizeWord = len(random_word)

    lenVetword(finding, sizeWord)
    Name = input("Enter your name: ")
    print("Welcome "+Name+"\n------------------\nTry to guess the word in less than 10 attempts")

    while(Amount_attempts > 0):
        joinLetters = ''.join(finding)
        if(joinLetters == random_word):
            print("Word is "+ random_word)
            print("You got it!!!")
            break
        else:
            print("Guess the word: ", *finding)
            letter = input()
            vetModify, hit = verifyLetter(letter, random_word, sizeWord, finding)
            if(hit == 0):
                draw(Amount_attempts)
                Amount_attempts -= 1
hangman()

