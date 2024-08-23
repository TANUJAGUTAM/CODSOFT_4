import random

# Function to get the user's choice
def user_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        choice = input("Please pick rock, paper, or scissors: ").lower()
        if choice in choices:
            return choice
        print("Hmm, that doesn't look right. Please try again.")

# Function to get the computer's random choice
def computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to decide who won
def decide_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "user"
    else:
        return "computer"

# Function to show the results of the game
def show_results(user, computer, winner):
    print(f"\nYou chose: {user}")
    print(f"The computer chose: {computer}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("Congrats, you win!")
    else:
        print("The computer wins this time.")

# Function to ask if the user wants to play again
def play_again():
    while True:
        answer = input("Do you want to play again? (yes or no): ").lower()
        if answer in ["yes", "no"]:
            return answer == "yes"
        print("Please just type 'yes' or 'no'.")

# The main function that runs the game
def main_game():
    user_score = 0
    computer_score = 0

    while True:
        user = user_choice()
        computer = computer_choice()
        winner = decide_winner(user, computer)
        show_results(user, computer, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"\nScoreboard: You {user_score} - {computer_score} Computer")

        if not play_again():
            print("Thanks for playing! Final scores:")
            print(f"You {user_score} - {computer_score} Computer")
            break

# Make sure the game runs if the script is executed
if __name__ == "__main__":
    print("Welcome to the Rock-Paper-Scissors game!")
    main_game()
