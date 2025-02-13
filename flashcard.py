import tkinter as tk
import random

class FlashcardApp(tk.Frame):
    def __init__(self, master, flashcards):
        super().__init__(master)
        self.master = master
        self.flashcards = flashcards
        self.current_index = 0
        self.is_flipped = False

        self.question_label = tk.Label(self, text="", font=("Arial", 24))
        self.question_label.pack(pady=20)

        self.flip_button = tk.Button(self, text="Flip", command=self.flip_card)
        self.flip_button.pack(pady=10)

        self.next_button = tk.Button(self, text="Next", command=self.next_card)
        self.next_button.pack(side='right', padx=20)

        self.prev_button = tk.Button(self, text="Previous", command=self.prev_card)
        self.prev_button.pack(side='left', padx=20)

        self.shuffle_button = tk.Button(self, text="Shuffle", command=self.shuffle_cards)
        self.shuffle_button.pack(pady=10)

        self.show_question()

    def show_question(self):
        self.is_flipped = False
        self.question_label.config(text=self.flashcards[self.current_index]['question'])

    def show_answer(self):
        self.is_flipped = True
        self.question_label.config(text=self.flashcards[self.current_index]['answer'])

    def flip_card(self):
        if self.is_flipped:
            self.show_question()
        else:
            self.show_answer()

    def next_card(self):
        self.current_index = (self.current_index + 1) % len(self.flashcards)
        self.show_question()

    def prev_card(self):
        self.current_index = (self.current_index - 1) % len(self.flashcards)
        self.show_question()

    def shuffle_cards(self):
        random.shuffle(self.flashcards)
        self.current_index = 0
        self.show_question()
