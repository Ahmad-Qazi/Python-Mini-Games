print("Welcome to the guessing game!")
import random
mode = input("Choose a mode: hard, easy, or normal: ").lower()
easy = "easy"
hard = "hard"
normal = "normal"
if mode == easy:
    computer = random.randint(1, 10)
    max_attempts = 5
    attempts = 0
    while attempts < max_attempts:
        data = int(input("Enter a number between 1 and 10: "))
        attempts += 1
        if data > computer:
            print("Too high, try again.")
        elif data < computer:
            print("Too low, try again.")
        else:
            print("You win!")
            break
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {computer}.")
elif mode == hard:
    computer = random.randint(-500, 500)
    max_attempts = 8
    attempts = 0
    while attempts < max_attempts:
        data = int(input("Enter a number between -500 and 500: "))
        attempts += 1
        if data > computer:
            print("Too high, try again.")
        elif data < computer:
            print("Too low, try again.")
        else:
            print("You win!")
            break
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {computer}.")
elif mode == normal:
    computer = random.randint(1, 100)
    max_attempts = 6
    attempts = 0
    while attempts < max_attempts:
        data = int(input("Enter a number between 1 and 100: "))
        attempts += 1
        if data > computer:
            print("Too high, try again.")
        elif data < computer:
            print("Too low, try again.")
        else:
            print("You win!")
            break
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {computer}.")
else:
    print("Invalid mode selected.")
