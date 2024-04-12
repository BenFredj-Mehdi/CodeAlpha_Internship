from random import choice #we need this function to choose a word from our list

def choose_word():
    #your custom list of words
    words = ["hangman", "car", "keyboard", "programming", "game", "mouse", "algorithm", "debugging"]
    return choice(words)

def display_word(word, guessed_letters):  #To display the word updated with the guesses
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman(): #The main game that uses the other functions
    word = choose_word()
    guessed_letters = []
    attempts = 5

    print("Welcome to Hangman!\n\n ...loading...\n\n")
    print("Try to guess the word.\n")
    print(display_word(word, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect! You have",attempts,"attempts left.")
            if attempts == 0:
                print("Game over! The word was:", word)
                break
        else:
            print("Correct!")

        display = display_word(word, guessed_letters)
        print(display)

        if "_" not in display:
            print("Congratulations! You guessed the word:", word)
            break

if __name__ == "__main__":
    hangman()
