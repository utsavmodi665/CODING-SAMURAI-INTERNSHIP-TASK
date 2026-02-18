"""
Number Guessing Game with GUI
Description: A number guessing game using Tkinter library where the user can guess a random number.
Skills: Tkinter for GUI, random number generation, conditionals
"""

import tkinter as tk
from tkinter import messagebox
import random


class NumberGuessingGame:
    def __init__(self, root):
        """Initialize the game with GUI components"""
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x350")
        self.root.resizable(False, False)
        
        # Game variables
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 10
        
        # GUI Components
        self.create_widgets()
        
    
    def create_widgets(self):
        """Create all GUI widgets"""
        # Title Label
        title_label = tk.Label(
            self.root, 
            text="🎯 Number Guessing Game", 
            font=("Arial", 18, "bold"),
            fg="#2E86AB"
        )
        title_label.pack(pady=15)
        
        # Instructions
        instructions_label = tk.Label(
            self.root,
            text="I'm thinking of a number between 1 and 100",
            font=("Arial", 10),
            fg="#555555"
        )
        instructions_label.pack(pady=5)
        
        # Attempts display
        self.attempts_label = tk.Label(
            self.root,
            text=f"Attempts: {self.attempts}/{self.max_attempts}",
            font=("Arial", 11),
            fg="#333333"
        )
        self.attempts_label.pack(pady=10)
        
        # Input Frame
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=15)
        
        guess_label = tk.Label(
            input_frame,
            text="Enter your guess:",
            font=("Arial", 12)
        )
        guess_label.grid(row=0, column=0, padx=5)
        
        self.guess_entry = tk.Entry(
            input_frame,
            font=("Arial", 12),
            width=10
        )
        self.guess_entry.grid(row=0, column=1, padx=5)
        self.guess_entry.bind('<Return>', lambda event: self.check_guess())
        
        # Submit Button
        submit_button = tk.Button(
            self.root,
            text="Submit Guess",
            font=("Arial", 12, "bold"),
            bg="#2E86AB",
            fg="white",
            activebackground="#1E6A8F",
            activeforeground="white",
            cursor="hand2",
            command=self.check_guess
        )
        submit_button.pack(pady=10)
        
        # Feedback Label
        self.feedback_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 12, "bold"),
            fg="#333333"
        )
        self.feedback_label.pack(pady=10)
        

         # Reset button
        reset_button = tk.Button(
            self.root, 
            text="Reset Game", 
             font=("Arial", 12, "bold"),
            bg="#2E86AB",
            fg="white",
            activebackground="#1E6A8F",
            activeforeground="white",
            cursor="hand2",
            command=self.reset
            )
        reset_button.pack(pady=5)
        
    def check_guess(self):
        """Check the user's guess against the target number"""
        guess = self.guess_entry.get()
        
        # Validate input
        if not guess:
            self.feedback_label.config(text="Please enter a number!", fg="#DC3545")
            return
            
        try:
            guess = int(guess)
        except ValueError:
            self.feedback_label.config(text="Invalid input! Enter a number.", fg="#DC3545")
            self.guess_entry.delete(0, tk.END)
            return
        
        # Check range
        if guess < 1 or guess > 100:
            self.feedback_label.config(text="Number must be between 1 and 100!", fg="#DC3545")
            self.guess_entry.delete(0, tk.END)
            return
        
        # Increment attempts
        self.attempts += 1
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")
        
        # Check guess
        if guess == self.target_number:
            self.handle_win()
        elif self.attempts >= self.max_attempts:
            self.handle_game_over()
        elif guess < self.target_number:
            self.feedback_label.config(text="Too low! Try a higher number.", fg="#FFC107")
        else:
            self.feedback_label.config(text="Too high! Try a lower number.", fg="#FF0101")
        
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()
    
    def handle_win(self):
        """Handle winning condition"""
        self.feedback_label.config(text=f"🎉 Correct! The number was {self.target_number}!", fg="#28A745")
        messagebox.showinfo(
            "Congratulations!",
            f"You guessed the number in {self.attempts} attempt(s)!"
        )
        self.guess_entry.config(state='disabled')
    
    def handle_game_over(self):
        """Handle game over condition"""
        self.feedback_label.config(
            text=f"Game Over! The number was {self.target_number}.", 
            fg="#DC3545"
        )
        messagebox.showinfo(
            "Game Over",
            f"Sorry, you've run out of attempts!\nThe number was {self.target_number}."
        )
        self.guess_entry.config(state='disabled')

        # Function to reset game
    def reset(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")
        self.feedback_label.config(text="", fg="#333333")
        self.guess_entry.config(state='normal')
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()
    
    def reset_game(self):
        """Reset the game to play again"""
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")
        self.feedback_label.config(text="", fg="#333333")
        self.guess_entry.config(state='normal')
        self.guess_entry.delete(0, tk.END)
        self.play_again_button.pack_forget()
        self.guess_entry.focus()


def main():
    """Main function to run the game"""
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
