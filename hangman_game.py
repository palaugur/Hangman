import random
from hangman_art import logo,stages
from hangman_word_list import word_list, selected_category, category_name

chosen_word = random.choice(selected_category)

display = []
# text_empty = ""
lives = 6
hangman = stages[lives]
guessed_letters = []

for letter in chosen_word:
    if letter == " ":
        display.append(" ")
    else:
        display.append("_")

print(f"{logo}\n")

# print(chosen_movie)  # To test during coding

# for i in display:
#     text_empty += i
# print(text_empty)

print(f"{' '.join(display)}")
print(f"Category: {category_name}")

while "_" in display and lives > 0:
    print(hangman)

    guess_letter = input("Guess a letter: ").lower()
    if guess_letter in guessed_letters:
        print(f"You already guessed '{guess_letter}'")

    chosen_movie_backup = chosen_word.lower()
    if guess_letter in chosen_movie_backup:
        for index in range(len(chosen_word)):
            letter = chosen_movie_backup[index]
            if letter == guess_letter:
                display[index] = chosen_word[index]
    else:
        if guess_letter in guessed_letters:
            print("Not in the word!\n")

        else:
            lives -= 1
            print(f"Wrong letter! You lost one life:  {lives}")
            hangman = stages[lives]

    guessed_letters.append(guess_letter)
    print(f"{' '.join(display)}")
    print(f"Category: {category_name}" )

if "_" in display:
    print(f"Out of lives! The word was:  {chosen_word}")
    print(hangman)
else:
    print(f"Congratulations! You guessed the word: {chosen_word}")
