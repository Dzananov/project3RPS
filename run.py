import random

options = ["rock", "scissor", "paper"]


def choose_option():
    """finding out user choise"""
    user_choise = input("Choose your answer: ")
    if user_choise in ["rock"]:
        user_choise = "rock"
    elif user_choise in ["scissor"]:
        user_choise = "scissor"
    elif user_choise in ["paper"]:
        user_choise = "paper"
    else:
        print("wrong input")
        choose_option()
    return user_choise


def computer_choise():
    """finding out computer choise"""
    comp_choise = random.choice(options)
    return comp_choise


while True:
    user_choise = choose_option()
    comp_choise = computer_choise()

    if user_choise == comp_choise:
        print(f"Both selected {user_choise}. It's a tie!")
    elif user_choise == "paper":
        if comp_choise == "rock":
            print("paper covers rock! You win!")
        else:
            print("scissors cut paper! You lose.")

    elif user_choise == "scissors":
        if comp_choise == "paper":
            print("scissor cut paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    elif user_choise == "rock":
        if comp_choise == "scissors":
            print("Rock smashes scissors! You win")
        else:
            print("paper covers rock! You lose.")
