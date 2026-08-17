import random

words = ["python", "hangman", "programming", "computer", "keyboard"]

def play_hangman():
    word = random.choice(words)          
    guessed_letters = []                 
    attempts_left = 6                    

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    while attempts_left > 0:

        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        print("\nWord: " + display)

        if "_" not in display:
            print("You guessed the word! It was:", word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
        else:
            attempts_left -= 1
            print(f"Wrong! Attempts left: {attempts_left}")

    if attempts_left == 0:
        print("\n Game over! The word was:", word)

if __name__ == "__main__":
    play_hangman()
