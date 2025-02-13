import json
import tkinter as tk
from tkinter import filedialog
from flashcard import FlashcardApp

def load_flashcards(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def main():
    root = tk.Tk()
    root.title("Flashcard App")

    file_path = filedialog.askopenfilename(title="Select Flashcards JSON File", filetypes=[("JSON files", "*.json")])
    if file_path:
        flashcards = load_flashcards(file_path)
        app = FlashcardApp(root, flashcards)
        app.pack(expand=True, fill='both')
        root.mainloop()

if __name__ == "__main__":
    main()
