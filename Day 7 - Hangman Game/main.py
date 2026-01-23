import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list
lives = 6
stages = hangman_art.stages

print(hangman_art.logo)
chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guesses = []

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in guesses:
        print("You already guessed this letter")
        continue

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
            guesses.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        print(f"{guess} is not in the word")
        print(stages[lives])
        lives -= 1
        guesses.append(guess)
        if lives == -1:
            game_over = True
            print(f"***********************YOU LOSE**********************")
            print(f"The word was: {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
