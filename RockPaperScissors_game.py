import random
from typing import List


class PaperScissorsRock:
    """Main class for Rock Paper Scissors game."""
    def __init__(self, player_name: str):
        self.choices: List[str] = ['paper', 'scissors', 'rock']
        self.player_name: str = player_name
    
    def get_player_choice(self):
        player_choice: str = input(f'Enter a choice from({self.choices}):')
        if player_choice.lower() in self.choices:
            return player_choice
        else:
            print (f'please enter valid choice from {self.choices}.')
            return self.get_player_choice()

    def get_computer_choice(self):
        computer_choice: str = random.choice(self.choices)
        return computer_choice

    def decide_winner(self, player_choice: str, computer_choice: str) -> str:
        """Method to decide game winner based on the rules.

        :param player_choice: The player's choice
        :param computer_choice: The computer's choice
        :return: Game outcome as a string
        """
        if computer_choice == player_choice:
            return "It is a Tie!"
        else:
            winner_choices = [('rock', 'scissors'), ('scisors', 'paper'), ('paper', 'rock')]
            for choices in winner_choices:
                if (player_choice == winner_choices[0]) & (computer_choice == winner_choices[1]):
                    return 'player win!'
        
            return 'computer win!'


    def play(self):
        """Main method to play Rock, Paper, Scissors"""
        player_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        print(f'computer choice: {computer_choice}')
        print (self.decide_winner(player_choice, computer_choice))


if __name__ == '__main__':
    game = PaperScissorsRock('ali')

    while True: 
        game.play()
        continue_game = input('If you want to play again enter any key else enter q/Q to exit')
        if continue_game.lower() == 'q':
            break 