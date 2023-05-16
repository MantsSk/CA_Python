import random


def choose_word(words):
    return random.choice(words)


def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()


def main():

    words = ["apple", "banana", "orange", "kiwi", "grape"]
    attempts = 6

    print("Welcome to Hangman!")
    word = choose_word(words)
    guessed_letters = []

    while attempts > 0:
        print(display_word(word, guessed_letters))

        guess = input("Enter your guess: ").lower()
        if guess in guessed_letters:
            print("You have already guessed that letter. Try again!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            if set(word).issubset(set(guessed_letters)):
                print(
                    f"Congratulations! You guessed the word correctly: {word}")
                return
        else:
            attempts -= 1
            print(f"Incorrect guess! Attempts remaining: {attempts}")
    print(f"Game over! The word was: {word}")


main()
