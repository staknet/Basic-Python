import sys
import random
from enum import Enum

def rps(name = 'PlayerOne'):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_RPS():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSOR = 3

        player_choice = input(f"\n{name} please enter... \n1. Rock\n2. Paper\n3. Scissor\n\n")
        if player_choice not in ("1", "2", "3"):
            print(f"{name}, please enter 1, 2, or 3.")
            return play_RPS()

        player = int(player_choice)

        computer_choice = random.choice("123")
        computer = int(computer_choice)

        print(f"\n{name}, you chose {str(RPS(player)).replace('RPS.','')}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.','')} .\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
                
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉 {name}, you win!\n"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉 {name}, you win!\n"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉 {name}, you win!\n"
            elif player == computer:
                return "😲 Tie game!\n"
            else:
                python_wins += 1
                return f"🐍 Python wins!\nSorry, {name}... 😢"
        
        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nPython wins: {python_wins}")

        print(f"\nPlay again, {name}?")
        
        while True:
            playagain = input("\nPress Y for Yes & N for No:\n")
            if playagain.lower() not in ['y', 'n']:
                continue
            else:
                break

        if playagain.lower() == 'y':
            return play_RPS()
        else:
            print("\n🎉🎉🎉🎉🎉🎉")
            print("\nThank you for playing!") 
            if __name__ == "__main__":
                sys.exit(f"Bye {name}!")
            else:
                from lesson16_arcade import choose_game
                choose_game(name, welcome_back=True)
    return play_RPS


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n","--name", metavar="name",
        required=True, help="The name of the person to playing the game."
    )

    args = parser.parse_args()

    rock_paper_scissor = rps(args.name)
    rock_paper_scissor()