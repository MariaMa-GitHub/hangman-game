# HANGMAN GAME
import tkinter.messagebox
from tkinter import *
from random import choice
from words import word_list

# game settings
PROGRAM_NAME = "Hangman Game"
WINDOW_SIZE = "950x560"
BG_COLOR = "#A9A9A9"
GREEN_COLOR = "#F0FFF0"
PINK_COLOR = "#FFF0F5"
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# game class
class Program:

    # initialize settings
    def __init__(self):

        self.step = 0

        self.window = Tk()
        self.window.title(PROGRAM_NAME)
        self.window.config(padx=50, pady=50, bg=BG_COLOR)
        self.window.geometry(WINDOW_SIZE)
        self.window.resizable(width=0, height=0)

        self.word_label = Label(text="   " + PROGRAM_NAME + "   ", font=("Arial", 32, "bold"), bg="white", justify="center")
        self.word_label.grid(row=0, column=0, rowspan=2, padx=10, sticky="nswe")

        self.images = []
        for num in range(7):
            self.images.append( PhotoImage(file=f"images/{num+1}.png"))

        self.game_canvas = Canvas(width=400, height=400, bg="white", highlightthickness=2)
        self.game_image = self.game_canvas.create_image(200, 165, image=self.images[self.step])
        self.game_word = self.game_canvas.create_text(202, 345, width=380, text="", font=("Arial", 30, "normal"), justify="center")
        self.game_canvas.grid(row=0, column=1, columnspan=3, padx=10)

        self.input_canvas = Canvas(width=400, height=45, bg="white", highlightthickness=2)
        self.input_canvas.grid(row=1, column=1, columnspan=3, padx=10, pady=(10, 0))

        self.guess_label = Label(text=" Guess a letter:", font=("Arial", 16, "bold"), bg="white", justify="center")
        self.guess_label.grid(row=1, column=1, padx=(7, 0), pady=(12, 0))

        self.guess_entry = Entry(width=8, font=("Arial", 18, "bold"), highlightthickness=2)
        self.guess_entry.grid(row=1, column=2, padx=(0, 0), pady=(12, 0))
        self.guess_entry.focus()

        self.guess_button = Button(width=7, text="ENTER", font=("Arial", 12, "bold"), command=self.button_click)
        self.guess_button.grid(row=1, column=3, padx=(0, 15), pady=(13, 0))
        self.window.bind('<Return>', lambda event: self.button_click())

        self.generate_word()

        self.window.mainloop()

    # generate word
    def generate_word(self):

        self.guessed_letters = []
        self.guess_word = []
        self.chosen_word = ""

        while len(self.chosen_word) < 5:
            self.chosen_word = choice(word_list).lower()

        for char in self.chosen_word:
            self.guess_word.append("_")

        self.game_canvas.itemconfig(self.game_word, text=self.guess_word)

    # reset background
    def reset_background(self):

        self.game_canvas.config(bg="white")

    # guess letters
    def button_click(self):

        guess_letter = self.guess_entry.get().lower().strip()

        if len(guess_letter) == 1 and guess_letter in ALPHABET:

            if guess_letter in self.chosen_word:

                for index, letter in enumerate(self.chosen_word):
                    if guess_letter == letter:
                        self.guess_word[index] = guess_letter

                self.change_text(self.guess_word)

                if "_" not in self.guess_word:
                    self.game_canvas.config(bg=GREEN_COLOR)
                    self.update_game()

            else:

                if guess_letter not in self.guessed_letters:
                    self.change_image()

                if self.step >= 6:
                    self.game_canvas.itemconfig(self.game_word, text=self.chosen_word)
                    self.game_canvas.config(bg=PINK_COLOR)
                    self.update_game()

            self.guessed_letters.append(guess_letter)

        else:

            tkinter.messagebox.showinfo(title="ERROR", message="An error occurred. Please enter a valid letter.")

        self.guess_entry.delete(0, "end")
        self.guess_entry.focus()

    # change image
    def change_image(self):

        if self.step < 6:
            self.step += 1
            self.game_canvas.itemconfig(self.game_image, image=self.images[self.step])

    # change text
    def change_text(self, display_word):

        self.game_canvas.itemconfig(self.game_word, text=display_word)

    # update game
    def update_game(self):

        self.step = -1
        self.window.after(2000, self.change_image)
        self.window.after(2000, self.generate_word)
        self.window.after(2000, self.reset_background)


# game program
program = Program()
