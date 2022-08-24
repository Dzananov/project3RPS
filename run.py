# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random


class RockScissorPaper:
    def __init__(self):
    self.options=["rock", "scissor", "paper"]
    self.user_win = 0
    self.computer_win = 0


while True:
    def User_input():
        user_input = input("Choose your option between: rock, scissor, paper" ).lower()
        if User_input() not in self.options():
            print("You have to choose between the options provided! Try again:")
            return User_input()
    def computer_input():
        Computer_input = random.choice(list(self.options))
    
    def check_winner():
            print(f"You chose {User_input()}, computer chose {computer_input()}.")
            if User_input() == computer_input():
                print(f"Both selected {User_input()}. It's a tie!")
            elif User_input() == "paper":
                if computer_input() == "rock":
                    self.user_win =+1
                    print("paper covers rock! You win!")
                    
                else:
                    self.computer_win+= 1
                    print("scissors cut paper! You lose.")
                    
            elif User_input() == "scissors":
                if computer_input() == "paper":
                    self.user_win += 1
                    print("scissor cut paper! You win!")

                else:
                    self.computer_win+= 1
                    print("Rock smashes scissors! You lose.")
                    
            elif User_input()== "rock":
                if computer_input() == "scissors":
                    self.user_win += 1
                    print("Rock smashes scissors! You win")
                    
                else:
                    self.computer_win += 1
                    print("paper covers rock! You lose.")
                    
