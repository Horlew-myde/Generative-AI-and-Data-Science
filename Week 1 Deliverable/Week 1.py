import random

def start_persistent_game():

    player_tally = 0
    computer_tally = 0

    game_moves = ['rock', 'paper', 'scissors']

    print("--- Welcome to Rock, Paper, Scissors! ---")

    while True:
        print("\n" + "="*30)
        print(f"SCORE -> Player: {player_tally} | Computer: {computer_tally}")
        print("="*30)

        prompt_message = "Select your move (rock, paper, scissors) or type 'quit' to exit: "
        player_selection = input(prompt_message).lower()

        if player_selection == 'quit':
            print("\nThanks for playing!")
            print(f"Final Score -> Player: {player_tally} | Computer: {computer_tally}")
            break

        if player_selection not in game_moves:
            print("That's not a valid move. Please select again.")
            continue

        computer_selection = random.choice(game_moves)

        print(f"\nYour move: {player_selection.capitalize()} 🙋")
        print(f"Computer's move: {computer_selection.capitalize()} 🤖\n")

        if player_selection == computer_selection:
            print("This round is a draw! 🤝")
        elif (player_selection == 'rock' and computer_selection == 'scissors') or \
             (player_selection == 'paper' and computer_selection == 'rock') or \
             (player_selection == 'scissors' and computer_selection == 'paper'):
            print("You won this round! 🎉")
            player_tally += 1
        else:
            print("The computer won this round. 💻")
            computer_tally += 1

if __name__ == "__main__":
    start_persistent_game()