import random

def choose_word():
    words = ["python", "hangman", "challenge", "programming", "developer", "computer", "science", "artificial", "intelligence"]
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        """,
        """
           ------
           |    |
           |
           |
           |
           |
        """,
        """
           ------
           |
           |
           |
           |
           |
        """,
    ]
    return stages[tries]

def hangman():
    word = choose_word()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    tries = 5

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please enter a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess not in word:
                print("Sorry, that letter is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job, that letter is in the word!")
                guessed_letters.append(guess)
                word_completion = "".join([letter if letter in guessed_letters else "_" for letter in word])
                if "_" not in word_completion:
                    guessed = True
        else:
            print("Invalid input. Please enter a single letter.")

        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congratulations! You guessed the word: " + word)
    else:
        print("Sorry, you ran out of tries. The word was: " + word)

if __name__ == "__main__":
    hangman()