import random

print("=" * 40)
print("      NUMBER GUESSING GAME")
print("=" * 40)

score = 0

while True:

    print("\nChoose Difficulty")
    print("1. Easy (1-20, 7 Attempts)")
    print("2. Medium (1-50, 6 Attempts)")
    print("3. Hard (1-100, 5 Attempts)")

    level = input("\nEnter choice: ")

    if level == "1":
        maximum = 20
        attempts = 7

    elif level == "2":
        maximum = 50
        attempts = 6

    elif level == "3":
        maximum = 100
        attempts = 5

    else:
        print("Invalid Choice")
        continue

    secret = random.randint(1, maximum)

    print(f"\nGuess a number between 1 and {maximum}")

    win = False

    while attempts > 0:

        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess == secret:
            print("\nCorrect!")
            print("You Won!")
            score += attempts * 10
            win = True
            break

        elif guess < secret:
            print("Too Low!")

        else:
            print("Too High!")

        attempts -= 1
        print("Attempts Left:", attempts)

    if not win:
        print("\nGame Over!")
        print("Correct Number was:", secret)

    print("\nCurrent Score:", score)

    again = input("\nPlay Again? (y/n): ").lower()

    if again != "y":
        break

print("\nFinal Score:", score)
print("Thank you for playing!")
