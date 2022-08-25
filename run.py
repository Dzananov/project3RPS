import random

options = ["rock", "scissor", "paper"]


class RockScissorPaper:
    def __init__(self):
        self.user_win = 0
        self.computer_win = 0


while True:
    def User_input():
        User_input = input("Choose your option(rock,scissor,paper)").lower()
        if User_input not in options:
            print("Try again, choose from the options!")
        User_input()

    def computer_input():
        computer_input = random.choice(options)
        print(f"You chose {User_input()}, computer chose {computer_input}.")

    def check_winner():
        if User_input() == computer_input():
            print(f"Both selected {User_input()}. It's a tie!")
        elif User_input() == "paper":
            if computer_input() == "rock":
                self.user_win += 1
                print("paper covers rock! You win!")
            else:
            self.computer_win += 1
            print("scissors cut paper! You lose.")

        elif User_input() == "scissors":
            if computer_input() == "paper":
                self.user_win += 1
                print("scissor cut paper! You win!")
            else:
                self.computer_win += 1
                print("Rock smashes scissors! You lose.")

        elif User_input() == "rock":
            if computer_input() == "scissors":
                self.user_win += 1
                print("Rock smashes scissors! You win")
            else:
                self.computer_win += 1
                print("paper covers rock! You lose.")