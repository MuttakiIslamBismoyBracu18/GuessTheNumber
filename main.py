import ipywidgets as widgets
from IPython.display import display, HTML, clear_output
import random

class GuessTheNumberGame:
    def __init__(self, num_levels=3):
        self.num_levels = num_levels
        self.current_level = 1
        self.score = 0
        self.secret_number = random.randint(1, 10 * self.current_level)

        # Create widgets
        self.level_label = widgets.HTML(value=f"<h2 style='color: blue;'>Level: {self.current_level}</h2>")
        self.score_label = widgets.HTML(value=f"<h2 style='color: green;'>Score: {self.score}</h2>")
        self.guess_input = widgets.IntText(value=0, description='Your Guess:')
        self.submit_button = widgets.Button(description='Submit Guess')
        self.output_label = widgets.HTML()
        self.hint_label = widgets.HTML(value='')

        # Set up event handlers
        self.submit_button.on_click(self.check_guess)

        # Display widgets
        display(HTML("<h1 style='color: purple;'>Guess the Number Game</h1>"))
        display(self.level_label, self.score_label, self.guess_input, self.submit_button, self.output_label, self.hint_label)

    def new_level(self):
        self.secret_number = random.randint(1, 10 * self.current_level)
        self.level_label.value = f"<h2 style='color: blue;'>Level: {self.current_level}</h2>"
        self.score_label.value = f"<h2 style='color: green;'>Score: {self.score}</h2>"
        self.output_label.value = ''
        self.hint_label.value = ''

    def check_guess(self, b):
        guess = self.guess_input.value
        if guess == self.secret_number:
            self.output_label.value = "<p style='color: green;'>Correct! You guessed the number!</p>"
            self.score += 10 * self.current_level
            self.current_level += 1
            if self.current_level <= self.num_levels:
                self.new_level()
            else:
                self.end_game()
        elif guess < self.secret_number:
            self.output_label.value = "<p style='color: red;'>Incorrect. Try again!</p>"
            self.hint_label.value = "<p style='color: orange;'>Hint: Your guess is too low!</p>"
        else:
            self.output_label.value = "<p style='color: red;'>Incorrect. Try again!</p>"
            self.hint_label.value = "<p style='color: orange;'>Hint: Your guess is too high!</p>"

    def end_game(self):
        self.output_label.value = f"<h2 style='color: purple;'>Game Over!</h2><p style='color: green;'>Final Score: {self.score}</p>"

# Instantiate and start the game
game = GuessTheNumberGame(num_levels=3)
