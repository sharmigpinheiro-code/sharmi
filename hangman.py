# ==========================================
# 🎮 HANGMAN GAME USING PYTHON
# Developed for CodeAlpha Internship
# Features:
# ✅ Difficulty Levels
# ✅ Hint System
# ✅ ASCII Art
# ✅ Score Tracking
# ✅ Replay Option
# ✅ User Friendly Interface
# ==========================================

import random

# Easy Words
easy_words = {
    "apple": "Fruit",
    "chair": "Furniture",
    "tiger": "Animal",
    "pizza": "Food",
    "water": "Liquid"
}

# Medium Words
medium_words = {
    "laptop": "Electronic Device",
    "diamond": "Precious Stone",
    "hospital": "Medical Place",
    "football": "Sport",
    "library": "Place with Books"
}

# Hard Words
hard_words = {
    "python": "Programming Language",
    "satellite": "Space Object",
    "microphone": "Audio Device",
    "architecture": "Building Design",
    "encyclopedia": "Large Knowledge Book"
}

# Hangman stages
hangman_stages = [
'''
   -----
   |   |
       |
       |
       |
       |
=========
''',
'''
   -----
   |   |
   O   |
       |
       |
       |
=========
''',
'''
   -----
   |   |
   O   |
   |   |
       |
       |
=========
''',
'''
   -----
   |   |
   O   |
  /|   |
       |
       |
=========
''',
'''
   -----
   |   |
   O   |
  /|\\  |
       |
       |
=========
''',
'''
   -----
   |   |
   O   |
  /|\\  |
  /    |
       |
=========
''',
'''
   -----
   |   |
   O   |
  /|\\  |
  / \\  |
       |
=========
'''
]

# Welcome Message
print("====================================")
print("🎮 WELCOME TO HANGMAN GAME 🎮")
print("====================================")

# Username
name = input("👤 Enter your name: ")

score = 0

while True:

    print(f"\nHello {name}! Choose Difficulty Level:")
    print("1️⃣ Easy")
    print("2️⃣ Medium")
    print("3️⃣ Hard")

    choice = input("👉 Enter your choice (1/2/3): ")

    if choice == "1":
        words = easy_words
        difficulty = "Easy"
    elif choice == "2":
        words = medium_words
        difficulty = "Medium"
    elif choice == "3":
        words = hard_words
        difficulty = "Hard"
    else:
        print("❌ Invalid Choice! Defaulting to Easy Level.")
        words = easy_words
        difficulty = "Easy"

    # Random word selection
    word = random.choice(list(words.keys()))
    hint = words[word]

    guessed_letters = []
    tries = 6

    print(f"\n🎯 Difficulty Level: {difficulty}")
    print(f"💡 Hint: {hint}")

    # Game Loop
    while tries > 0:

        display_word = ""

        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\n🔤 Word:", display_word)

        # Win condition
        if "_" not in display_word:
            print("\n🎉 Congratulations!", name)
            print("🏆 You guessed the word:", word)

            if difficulty == "Easy":
                score += 10
            elif difficulty == "Medium":
                score += 20
            else:
                score += 30

            print("⭐ Your Score:", score)
            break

        guess = input("\n👉 Guess a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single alphabet letter!")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter!")

        elif guess in word:
            guessed_letters.append(guess)
            print("✅ Correct Guess!")

        else:
            guessed_letters.append(guess)
            tries -= 1

            print("❌ Wrong Guess!")
            print(hangman_stages[6 - tries])
            print(f"❤️ Tries Left: {tries}")

    # Lose condition
    if tries == 0:
        print("\n💀 GAME OVER!")
        print("📌 The correct word was:", word)

    # Replay option
    replay = input("\n🔄 Do you want to play again? (yes/no): ").lower()

    if replay != "yes":
        print("\n====================================")
        print("🙏 Thanks for Playing!")
        print(f"🏅 Final Score of {name}: {score}")
        print("====================================")
        break