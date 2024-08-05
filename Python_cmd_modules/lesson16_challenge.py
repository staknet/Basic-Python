import argparse
import sys
import random


def guess_number_game(name='Player 1'):
    game_count = 0
    player_win = 0

    def guess_number():
        nonlocal game_count
        nonlocal player_win
        nonlocal name

        player_choice = int(input(f"\n{name}, guess which number I'm thinking of .. 1, 2, or 3.\n"))
        computer_choice = int(random.choice('123'))

        print(f"{name}, you chose {player_choice}.")
        print(f"I was thinking about the number {computer_choice}.")

        if player_choice not in (1,2,3):
            print(f"{name}, please choose numbers between 1, 2, and 3.")
        else: 
            if player_choice == computer_choice:
                game_count += 1
                player_win += 1
                print(f"{name}, you win! 🎉" )
            else:
                game_count +=1
                print(f"Sorry, {name}. Better luck next time. 😢")
        
        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_win}")
        winning_percentage = 0
        if game_count > 0:
            winning_percentage = 100*(player_win/game_count)
        
        print(f"Your winning percentage: {winning_percentage}%.")
        while True:
            playagain = input("\nPress Y for Yes & N for No:\n")
            if playagain.lower() not in ['y', 'n']:
                continue
            else:
                break

        if playagain.lower() == 'y':
            guess_number_game(name)
        else:
            print("\n🎉🎉🎉🎉🎉🎉")
            print("\nThank you for playing!") 
            if __name__ == "__main__":
                sys.exit(f"Bye {name}!")
            else:
                from lesson16_arcade import choose_game
                choose_game(name, welcome_back=True)
    return guess_number

if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="Personalizing the game")
        parser.add_argument('-n', '--name', metavar='name', required=True)

        args = parser.parse_args()
        play_guess = guess_number_game(args.name)
        play_guess()
