import random

options = ["rock", "scissor", "paper"]


def choose_option():
    """finding out user choise with input and validating user answer
    with an if statement
    """
    user_choise = input("Choose your answer(rock, scissor, paper):\n")
    if user_choise not in options:
        print("Not an option!")
        choose_option()
    return user_choise


def computer_choise():
    """finding out computer choise with random import"""
    comp_choise = random.choice(options)
    return comp_choise


def main():
    """game run"""
    continue_game = True
    while continue_game:
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

        continue_game = input('do you like to play more ? (y/n)')
        if continue_game == 'n':
            break


if __name__ == '__main__':
    main()