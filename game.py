import random
import tkinter as tk
import pygame
from tkinter import messagebox

# Initialize pygame mixer for sound
pygame.mixer.init()

# Load sound files
win_sound = "win.wav"
lose_sound = "lose.wav"
tie_sound = "tie.mp3"
click_sound = "click.mp3"

# Choices
choices = ["rock", "paper", "scissors"]

# Score tracking
user_score = 0
computer_score = 0

# Colors for different results
WIN_COLOR = "#4CAF50"  # Green
LOSE_COLOR = "#FF5733"  # Red
TIE_COLOR = "#FFC300"  # Yellow
BG_COLOR = "#282C35"  # Dark Background
BUTTON_COLOR = "#3498db"  # Blue

# Function to determine winner
def determine_winner(user_choice):
    global user_score, computer_score

    # Play button click sound
    pygame.mixer.Sound(click_sound).play()

    computer_choice = random.choice(choices)
    result_text.set(f"💻 Computer chose: {computer_choice.capitalize()}")

    if user_choice == computer_choice:
        result_label.config(text="It's a tie! 🤝", fg=TIE_COLOR)
        root.config(bg=TIE_COLOR)
        pygame.mixer.Sound(tie_sound).play()
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        user_score += 1
        result_label.config(text="🎉 You win!", fg=WIN_COLOR)
        root.config(bg=WIN_COLOR)
        pygame.mixer.Sound(win_sound).play()
    else:
        computer_score += 1
        result_label.config(text="💻 Computer wins!", fg=LOSE_COLOR)
        root.config(bg=LOSE_COLOR)
        pygame.mixer.Sound(lose_sound).play()

    # Update score labels
    score_label.config(text=f"🏆 Scores - You: {user_score} | Computer: {computer_score}")

# GUI Setup
root = tk.Tk()
root.title("🎮 Rock-Paper-Scissors Game")
root.geometry("450x500")
root.config(bg=BG_COLOR)

# Title
tk.Label(root, text="✊ Rock - 📄 Paper - ✂️ Scissors", font=("Arial", 16, "bold"), bg=BG_COLOR, fg="white").pack(pady=10)

# Result Display
result_text = tk.StringVar()
result_text.set("Make Your Move!")
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 14), bg=BG_COLOR, fg="white")
result_label.pack(pady=10)

# Buttons for Choices
button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="🪨 Rock", font=("Arial", 14, "bold"), bg="#FF4500", fg="white",
                     width=10, height=2, command=lambda: determine_winner("rock"))
rock_btn.grid(row=0, column=0, padx=10, pady=5)

paper_btn = tk.Button(button_frame, text="📄 Paper", font=("Arial", 14, "bold"), bg="#32CD32", fg="white",
                      width=10, height=2, command=lambda: determine_winner("paper"))
paper_btn.grid(row=0, column=1, padx=10, pady=5)

scissors_btn = tk.Button(button_frame, text="✂️ Scissors", font=("Arial", 14, "bold"), bg="#4169E1", fg="white",
                         width=10, height=2, command=lambda: determine_winner("scissors"))
scissors_btn.grid(row=0, column=2, padx=10, pady=5)

# Score Display
score_label = tk.Label(root, text=f"🏆 Scores - You: {user_score} | Computer: {computer_score}", font=("Arial", 14), bg=BG_COLOR, fg="white")
score_label.pack(pady=10)

# Quit Button
exit_btn = tk.Button(root, text="❌ Exit Game", font=("Arial", 14, "bold"), bg="red", fg="white",
                     width=15, height=2, command=root.quit)
exit_btn.pack(pady=20)

# Run the GUI
root.mainloop()
