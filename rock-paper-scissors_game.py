import random
import time
Name = input("What is your name?\n").title()
while True:
    wish_to_play = input("Would you like to play a game?(yes/no): ").lower()
    if wish_to_play == "no":
        print("Okay, No problem. See you next time")
        time.sleep(3)
        exit()
    elif wish_to_play == "yes":
        break
    else:
        print("Choose a valid option(yes/no)")

list = ["Paper", "Scissors", "Rock"]
while True:
    win_score = int(input("How much score to win?"))
    Scores = { Name : 0, "Computer" : 0}
    while Scores[Name] < win_score and Scores["Computer"] < win_score:
        while True:
            Player = input("please choose a choice(Rock, Paper, Scissors) : ").title()
            if Player not in list:
                print("enter a valid choice")
            else:
                break
        random.seed()
        weapon = random.randint(-3, 2)
        Computer = list[weapon]
        print( Name + " = " + Player )
        print("Computer = " + Computer)
        if Player == Computer:
            print("This is a tie")
        elif Player == "Rock" and Computer == "Scissors":
            print("You won")
            Scores[Name] += 1
            print(Scores)
        elif Player == "Paper" and Computer == "Rock":
            print("You won")
            Scores[Name] += 1
            print(Scores)
        elif Player == "Scissors" and Computer == "Paper":
            print("You won")
            Scores[Name] += 1
            print(Scores)
        elif Player == "Paper" and Computer == "Scissors":
            print("I won")
            Scores["Computer"] += 1
            print(Scores)
        elif Player == "Rock" and Computer == "Paper":
            print("I won")
            Scores["Computer"] += 1
            print(Scores)
        else:
            print("I won")
            Scores["Computer"] += 1
            print(Scores)
    if win_score == Scores["Computer"]:
        print("Computer won the game")
    else:
        print("Congratulations, you won the game")
    while True:
        play_again = input("Do you want to play again?(yes/no)\n").lower()
        if play_again == "no":
            print("Okay, Bye. See you next time")
            time.sleep(3)
            exit()
        elif play_again == "yes":
            break
        else:
            print("Choose a valid option(yes/no)")
