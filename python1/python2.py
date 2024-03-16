import random

# List of words to choose from
word_list = ['python', 'java', 'computer', 'programming', 'language', 'hangman', 'keyboard', 'mouse']

# Select a word randomly from the list
secret_word = random.choice(word_list)
guessed_letters = []  # Letters the player has guessed
guesses_left = 7  # Number of incorrect guesses allowed

# Function to display the current state of the game
def display_game():
    display_word = [letter if letter in guessed_letters else '_' for letter in secret_word]
    print('Current word: ' + ' '.join(display_word))
    print('Guessed letters:', guessed_letters)
    print('Guesses left:', guesses_left)

# Main game loop
while guesses_left > 0:
    display_game()
    guess = input('Guess a letter: ').lower()

    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print('You already guessed that letter.')
        continue
    else:
        guessed_letters.append(guess)

    # Check if the guess is in the secret word
    if guess in secret_word:
        print('Good guess!')
        # Check if the player has won
        if all(letter in guessed_letters for letter in secret_word):
            print('Congratulations, you won! The word was:', secret_word)
            break
    else:
        guesses_left -= 1
        print('Oops! Wrong guess.')

    # Check if the player has run out of guesses
    if guesses_left <= 0:
        print('Sorry, you ran out of guesses. The word was:', secret_word)
        break
