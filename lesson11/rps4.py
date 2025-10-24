import sys
import random
from enum import Enum

# Global variable to track the number of games played
game_count = 0

def play_rps():
    # Define an Enum class to represent Rock, Paper, Scissors choices
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3
    # End of RPS Enum class definition
    
    # Get player input for their choice
    playerchoice = input(
        "\nEnter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")
    
    # Validate player input - must be 1, 2, or 3
    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3.")
        return play_rps()  # Recursively call function for new input
    # End of input validation if statement
    
    # Convert choices to integers for comparison
    player = int(playerchoice)
    computerchoice = random.choice("123")  # Randomly select computer choice
    computer = int(computerchoice)
    
    # Display choices using the Enum for user-friendly output
    print("\nYou chose " + str(RPS(player)).replace('RPS.', '').title() + ".")
    print("Python chose " + str(RPS(computer)
                                ).replace('RPS.', '').title() + ".\n")
    
    # Nested function to determine the game winner
    def decide_winner(player, computer):
        # Game logic: Rock(1) beats Scissors(3), Paper(2) beats Rock(1), 
        # Scissors(3) beats Paper(2)
        if player == 1 and computer == 3:
            return "🎉 You win!"
        elif player == 2 and computer == 1:
            return "🎉 You win!"
        elif player == 3 and computer == 2:
            return "🎉 You win!"
        elif player == computer:
            return "😲 Tie game!"
        else:
            return "🐍 Python wins!"
    # End of decide_winner function definition
    
    # Get and display game result
    game_result = decide_winner(player, computer)
    print(game_result)
    
    # Update and display global game count
    global game_count
    game_count += 1
    print("\nGame count: " + str(game_count))
    
    # Prompt player to play again
    print("\nPlay again?")
    
    # Input validation loop for play again decision
    while True:
        playagain = input("\nY for Yes or \nQ to Quit\n")
        # Continue looping until valid input (Y/y or Q/q) is received
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break
    # End of while loop for play again input validation
    
    # Handle play again decision
    if playagain.lower() == "y":
        return play_rps()  # Recursive call to start new game
    else:
        print("\n🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        sys.exit("Bye! 👋")  # Exit the program
    # End of if-else block for replay decision
    
# End of play_rps function definition

# Start the game by calling the play_rps function
play_rps()