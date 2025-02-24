import tkinter as tk
import random
import time

class FlashcardApp(tk.Frame):
    def __init__(self, master, flashcards):
        super().__init__(master)
        self.master = master
        self.flashcards = flashcards
        self.known_cards = []
        self.unknown_cards = flashcards.copy()
        self.current_index = 0
        self.is_flipped = False
        self.study_unknown_only = False
        self.review_all = False

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

        self.known_var = tk.BooleanVar()
        self.known_checkbox = tk.Checkbutton(self.button_frame, text="Known", variable=self.known_var, command=self.toggle_known, bg="#4e4e4e", fg="#ffffff", selectcolor="#4e4e4e", width=10, height=2)
        self.known_checkbox.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

        self.study_unknown_button = tk.Button(self.button_frame, text="Study Unknown", command=self.toggle_study_unknown, bg="#4e4e4e", fg="#ffffff", width=20, height=2)
        self.study_unknown_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.review_all_button = tk.Button(self.button_frame, text="Review All", command=self.start_review_all, bg="#4e4e4e", fg="#ffffff", width=20, height=2)
        self.review_all_button.grid(row=2, column=2, columnspan=2, pady=10)

        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=1)
        self.button_frame.grid_columnconfigure(2, weight=1)
        self.button_frame.grid_columnconfigure(3, weight=1)

        self.show_question()

    def get_current_flashcards(self):
        if self.review_all:
            return self.flashcards
        return self.unknown_cards if self.study_unknown_only else self.flashcards

    def show_question(self):
        self.is_flipped = False
        current_flashcards = self.get_current_flashcards()
        if not current_flashcards:
            self.reset_review_all()
            return
        card = current_flashcards[self.current_index]
        self.known_var.set(card in self.known_cards)
        self.question_label.config(text=card['question'])

    def show_answer(self):
        self.is_flipped = True
        current_flashcards = self.get_current_flashcards()
        card = current_flashcards[self.current_index]
        self.question_label.config(text=card['answer'])

    def flip_card(self):
        if self.is_flipped:
            self.show_question()
        else:
            self.show_answer()

    def next_card(self):
        current_flashcards = self.get_current_flashcards()
        self.current_index = (self.current_index + 1) % len(current_flashcards)
        self.show_question()

    def prev_card(self):
        current_flashcards = self.get_current_flashcards()
        self.current_index = (self.current_index - 1) % len(current_flashcards)
        self.show_question()

    def shuffle_cards(self):
        current_flashcards = self.get_current_flashcards()
        random.shuffle(current_flashcards)
        self.current_index = 0
        self.show_question()

    def toggle_known(self):
        current_flashcards = self.get_current_flashcards()
        card = current_flashcards[self.current_index]
        if self.known_var.get():
            if card in self.unknown_cards:
                self.unknown_cards.remove(card)
            if card not in self.known_cards:
                self.known_cards.append(card)
        else:
            if card in self.known_cards:
                self.known_cards.remove(card)
            if card not in self.unknown_cards:
                self.unknown_cards.append(card)
        self.show_question()

    def toggle_study_unknown(self):
        self.review_all = False  # Ensure review_all is turned off
        self.study_unknown_only = not self.study_unknown_only
        self.current_index = 0
        self.show_question()

    def start_review_all(self):
        self.review_all = True
        self.current_index = 0
        self.show_question()

    def reset_review_all(self):
        self.review_all = False
        self.current_index = 0
        self.show_question()
