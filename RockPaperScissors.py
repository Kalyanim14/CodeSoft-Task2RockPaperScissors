import tkinter as tk
from tkinter import messagebox
import random

# Initialize scores
user_score = 0
computer_score = 0

# Function to generate computer's choice
def computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

# Function to determine the result of the game
def determine_winner(user, computer):
    global user_score, computer_score
    if user == computer:
        return "It's a Tie!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Scissors" and computer == "Paper") or \
         (user == "Paper" and computer == "Rock"):
        user_score += 1
        return "You Win!"
    else:
        computer_score += 1
        return "Computer Wins!"

# Function to update the game result
def play(user_choice):
    global user_score, computer_score
    comp_choice = computer_choice()
    result = determine_winner(user_choice, comp_choice)
    
    # Update the result label and score display
    result_label.config(text=f"Your Choice: {user_choice}\nComputer's Choice: {comp_choice}\nResult: {result}")
    score_label.config(text=f"Your Score: {user_score} | Computer's Score: {computer_score}")
    
    # Ask if the user wants to play again
    play_again_label.config(text="Do you want to play again? (Yes/No)", fg="blue")
    
# Function to handle play again
def play_again(answer):
    global user_score, computer_score
    if answer.lower() == "yes":
        result_label.config(text="Choose Rock, Paper, or Scissors to play again!")
        play_again_label.config(text="")
    else:
        result_label.config(text="Thanks for playing!")
        play_again_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("400x400")  # Set the window size

# Heading
heading = tk.Label(root, text="Rock, Paper, Scissors", font=("Helvetica", 18))
heading.pack(pady=20)

# Button to select Rock
rock_button = tk.Button(root, text="Rock", font=("Arial", 14), bg="#4CAF50", fg="white", command=lambda: play("Rock"))
rock_button.pack(pady=10)

# Button to select Paper
paper_button = tk.Button(root, text="Paper", font=("Arial", 14), bg="#2196F3", fg="white", command=lambda: play("Paper"))
paper_button.pack(pady=10)

# Button to select Scissors
scissors_button = tk.Button(root, text="Scissors", font=("Arial", 14), bg="#FFC107", fg="white", command=lambda: play("Scissors"))
scissors_button.pack(pady=10)

# Label to display the result of the game
result_label = tk.Label(root, text="Choose Rock, Paper, or Scissors to play!", font=("Arial", 12))
result_label.pack(pady=20)

# Label to display the score
score_label = tk.Label(root, text="Your Score: 0 | Computer's Score: 0", font=("Arial", 12))
score_label.pack(pady=10)

# Label to ask the user to play again
play_again_label = tk.Label(root, text="", font=("Arial", 12))
play_again_label.pack(pady=10)

# Ask if user wants to play again
def play_again_option():
    play_again_answer = play_again_label.cget("text").split(" ")[-1]
    play_again(play_again_answer)

# Button to confirm to play again
play_again_button = tk.Button(root, text="Play Again", font=("Arial", 12), bg="#FF5722", fg="white", command=play_again_option)
play_again_button.pack(pady=10)

# Run the application
root.mainloop()
