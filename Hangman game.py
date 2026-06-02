evalimport random

HANGMAN = [
'''
 +---+
 |   |
     |
     |
     |
     |
=========
''',
'''
 +---+
 |   |
 O   |
     |
     |
     |
=========
''',
'''
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
''',
'''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
''',
'''
 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========
''',
'''
 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========
''',
'''
 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========
'''
]

words = {
    "Easy": ["apple", "house", "water"],
    "Medium": ["python", "laptop", "coding"],
    "Hard": ["developer", "algorithm", "database"]
}

score = 0

while True:
    print("\n=== ADVANCED HANGMAN ===")
    level = input("Choose Difficulty (Easy/Medium/Hard): ").title()

    if level not in words:
        print("Invalid choice!")
        continue

    word = random.choice(words[level])
    guessed = set()
    wrong = set()
    lives = 6
    hint_used = False

    while lives > 0:
        print(HANGMAN[6 - lives])

        display = " ".join(
            letter if letter in guessed else "_"
            for letter in word
        )

        print("Word:", display)
        print("Wrong Letters:", ", ".join(sorted(wrong)))
        print("Lives:", lives)
        print("Score:", score)

        if "_" not in display:
            print("\n🎉 You Won!")
            score += lives * 10
            break

        choice = input(
            "\nEnter letter or type HINT: "
        ).lower()

        if choice == "hint":
            if not hint_used:
                hint = random.choice(
                    [c for c in word if c not in guessed]
                )
                guessed.add(hint)
                hint_used = True
                print("💡 Hint:", hint)
            else:
                print("Hint already used!")
            continue

        if len(choice) != 1 or not choice.isalpha():
            print("Enter one valid letter!")
            continue

        if choice in guessed or choice in wrong:
            print("Already guessed!")
            continue

        if choice in word:
            guessed.add(choice)
            print("✅ Correct!")
        else:
            wrong.add(choice)
            lives -= 1
            print("❌ Wrong!")

    if lives == 0:
        print(HANGMAN[6])
        print("\n💀 Game Over!")
        print("Word was:", word)

    print("\nCurrent Score:", score)

    play = input("\nPlay Again? (y/n): ").lower()
    if play != "y":
        print("Final Score:", score)
        print("Thanks for playing! 👋")
        break