import random
word_list = ["apple", "tiger", "dance", "cloud", "smart"]

# Randomly select a word
secret_word = random.choice(word_list)
guessed_letters = []  # To store correctly guessed letters
wrong_guesses = 0
max_wrong_guesses = 6

# Create a display with underscores for unguessed letters
display_word = ["_"] * len(secret_word)

print("🎮 Welcome to Hangman!")
print("Guess the word letter by letter.")
print("You have 6 chances for wrong guesses.\n")

while wrong_guesses < max_wrong_guesses and "_" in display_word:
    print("Word: ", " ".join(display_word))
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single alphabetic character.\n")
        continue

    if guess in guessed_letters or guess in display_word:
        print("🔁 You already guessed that letter. Try a different one.\n")
        continue

    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
        print("✅ Good job!\n")
    else:
        wrong_guesses += 1
        print(f"❌ Wrong guess! You have {max_wrong_guesses - wrong_guesses} tries left.\n")

    guessed_letters.append(guess)

# Game Result
if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("😞 You've run out of guesses. The word was:", secret_word)
