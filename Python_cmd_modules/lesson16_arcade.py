
import sys

def choose_game(name, welcome_back = False):
    while True:
        if welcome_back == True:
            print(f"\nWelcome back, {name} to the arcade menu.")


        player_choice = input(f'\nPlease choose a game:\n1 = Rock Paper Scissor\n2 = Guess My Number\n\nOr press "x" to exit the Arcade.\n')

        if player_choice.lower() == 'x':
            sys.exit(f"Bye {name}!")
        elif player_choice not in ["1", "2"]:
            print("Please enter a valid choice.")
        elif player_choice == "1":
            welcome_back = True
            from lesson16_RPS import rps
            rock_paper_scissor = rps(name)
            rock_paper_scissor()
        elif player_choice == "2":
            welcome_back = True
            from lesson16_challenge import guess_number_game
            guess_number = guess_number_game(name)
            guess_number()
    

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Personalization for the arcade.")

    parser.add_argument(
        '-n', '--name', metavar='name', required=True, help="The name of the player."
    )
    args = parser.parse_args()
    print(f"{args.name}, welcome to the arcade 🎮")
    choose_game(args.name)