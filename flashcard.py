import tkinter as tk
import random

class FlashcardApp(tk.Frame):
    def __init__(self, master, flashcards):
        super().__init__(master)
        self.master = master
        self.flashcards = flashcards
        self.current_index = 0
        self.is_flipped = False

        self.master.geometry("600x400")  # Set fixed window size
        self.master.configure(bg="#3a3b3c")  # Set background color

        self.question_frame = tk.Frame(self, bd=2, relief="solid", bg="#3e3e3e")
        self.question_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.question_label = tk.Label(self.question_frame, text="", font=("Arial", 18), wraplength=400, bg="#3e3e3e", fg="#ffffff", justify="center")
        self.question_label.place(relx=0.5, rely=0.5, anchor="center")

        self.button_frame = tk.Frame(self, bg="#3a3b3c")
        self.button_frame.pack(pady=10, fill="x")

        self.prev_button = tk.Button(self.button_frame, text="Previous", command=self.prev_card, bg="#4e4e4e", fg="#ffffff", width=10, height=2)
        self.prev_button.grid(row=0, column=0, padx=10)

        self.flip_button = tk.Button(self.button_frame, text="Flip", command=self.flip_card, bg="#4e4e4e", fg="#ffffff", width=10, height=2)
        self.flip_button.grid(row=0, column=1, padx=10)

        self.shuffle_button = tk.Button(self.button_frame, text="Shuffle", command=self.shuffle_cards, bg="#4e4e4e", fg="#ffffff", width=10, height=2)
        self.shuffle_button.grid(row=0, column=2, padx=10)

        self.next_button = tk.Button(self.button_frame, text="Next", command=self.next_card, bg="#4e4e4e", fg="#ffffff", width=10, height=2)
        self.next_button.grid(row=0, column=3, padx=10)

        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=1)
        self.button_frame.grid_columnconfigure(2, weight=1)
        self.button_frame.grid_columnconfigure(3, weight=1)

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
