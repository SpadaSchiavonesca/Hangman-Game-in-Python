import random

# Word list (expanded and categorized)
word_categories = {
    "fruits": [
        "apple", "banana", "pear", "strawberry",
        "orange", "grape", "pineapple", "apricot",
        "lemon", "coconut", "watermelon", "cherry",
        "papaya", "grapefruit", "peach", "kiwi",
    ],
    "animals": [
        "dog", "cat", "elephant", "giraffe",
        "lizard", "penguin", "lion", "tiger",
        "zebra", "bear", "monkey", "fish",
        "whale", "shark", "bird", "snake",
    ],
    # Add more categories as needed
}


def get_hangman_figure(incorrect_attempts):
    """Returns a string representation of the hangman
       based on incorrect attempts."""
    hangman_art = [
        # Initial state (no errors)
        r"""
        +---+
        |   |
            |
            |
            |
            |
        =========""",
        # Head
        r"""
        +---+
        |   |
        O   |
            |
            |
            |
        =========""",
        # Head and body
        r"""
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========""",
        # Head, body, and one arm
        r"""
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========""",
        # Head, body, and both arms
        r"""
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========""",
        # Head, body, both arms, and one leg
        r"""
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        =========""",
        # Full hangman (all limbs)
        r"""
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        ========="""
    ]
    return hangman_art[6 - incorrect_attempts]


def play_hangman(category):
    """Plays a game of Hangman with the chosen category."""

    word = random.choice(word_categories[category])
    word_length = len(word)
    guessed_letters = []
    incorrect_attempts = 6  # Standard hangman allows 6 incorrect guesses

    # Create a list to store the correctly guessed letters
    display_word = ["_"] * word_length

    while incorrect_attempts > 0 and "_" in display_word:
        print(get_hangman_figure(incorrect_attempts))
        print(" ".join(display_word))
        print(f"Incorrect attempts remaining: {incorrect_attempts}")

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i in range(word_length):
                if word[i] == guess:
                    display_word[i] = guess
        else:
            incorrect_attempts -= 1  # Decrement only once for each incorrect guess

    print(get_hangman_figure(incorrect_attempts))

    if "_" not in display_word:
        print(" ".join(display_word))
        print("Congratulations! You won!")
    else:
        print(f"You ran out of attempts. The word was {word}")


def display_welcome_message():
    """Displays a welcome message and the available categories."""
    print("Welcome to Hangman!")
    print("Available categories:")
    for category in word_categories:
        print(f"- {category}")


def get_category_choice():
    """Prompts the user to choose a category and validates the input."""
    chosen_category = input("Choose a category: ").lower()
    while chosen_category not in word_categories:
        print("Invalid category. Please choose from the list above.")
        chosen_category = input("Choose a category: ").lower()
    return chosen_category


if __name__ == "__main__":
    display_welcome_message()
    chosen_category = get_category_choice()
    play_hangman(chosen_category)
