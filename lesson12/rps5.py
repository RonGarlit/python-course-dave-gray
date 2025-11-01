import sys
import random
from enum import Enum


def rps():
    # Initialize game statistics as local variables
    game_count = 0       # Tracks total games played
    player_wins = 0      # Tracks player victories
    python_wins = 0      # Tracks Python (computer) victories

    def play_rps():
        # Declare nonlocal variables to modify them from the outer scope
        nonlocal player_wins
        nonlocal python_wins

        # Define an Enum class for Rock, Paper, Scissors choices with numeric values
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
            return play_rps()  # Recursive call for new input
        # End of input validation if statement

        # Convert player choice to integer
        player = int(playerchoice)

        # Generate computer's random choice and convert to integer
        computerchoice = random.choice("123")
        computer = int(computerchoice)

        # Display both choices using Enum for readable output
        print("\nYou chose " + str(RPS(player)).replace('RPS.', '').title() + ".")
        print("Python chose " + str(RPS(computer)
                                    ).replace('RPS.', '').title() + ".\n")

        # Nested function to determine winner and update scores
        def decide_winner(player, computer):
            nonlocal player_wins  # Access outer scope variables
            nonlocal python_wins
            
            # Game logic with score tracking
            if player == 1 and computer == 3:  # Rock beats Scissors
                player_wins += 1
                return "🎉 You win!"
            elif player == 2 and computer == 1:  # Paper beats Rock
                player_wins += 1
                return "🎉 You win!"
            elif player == 3 and computer == 2:  # Scissors beats Paper
                player_wins += 1
                return "🎉 You win!"
            elif player == computer:  # Tie game
                return "😲 Tie game!"
            else:  # Computer wins
                python_wins += 1
                return "🐍 Python wins!"
        # End of decide_winner function definition

        # Get and display game result
        game_result = decide_winner(player, computer)
        print(game_result)

        # Update and display game statistics
        nonlocal game_count  # Access outer scope variable
        game_count += 1

        print("\nGame count: " + str(game_count))
        print("\nPlayer wins: " + str(player_wins))
        print("\nPython wins: " + str(python_wins))

        # Prompt player to play again
        print("\nPlay again?")

        # Input validation loop for play again decision
        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            # Only accept 'y', 'Y', 'q', or 'Q'
            if playagain.lower() not in ["y", "q"]:
                continue  # Keep asking for valid input
            else:
                break     # Valid input received, exit loop
        # End of while loop for play again input validation

        # Handle play again decision
        if playagain.lower() == "y":
            return play_rps()  # Recursive call to start new game
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            sys.exit("Bye! 👋")  # Exit the program gracefully
        # End of if-else block for replay decision

    # End of play_rps inner function definition
    
    return play_rps  # Return the inner function as a closure


# Create the game function using the closure pattern
play = rps()

# Start the game by calling the returned function
play()