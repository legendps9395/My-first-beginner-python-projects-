import random
guess_no = random.randint(1, 100)
print(guess_no + random.randint(1, 100))
while True :
    try:
        guess = int(input("Guess a no between 1 and 100\n"))
        if guess < guess_no :
            print("Too low!")
        elif guess > guess_no :
            print("Too high!")
        else:
            print("Congratulaions! you guessed the number")
            break
    except ValueError:
        print("Please enter a valid no")

