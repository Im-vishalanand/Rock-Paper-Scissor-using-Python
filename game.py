import random
import tkinter as tk
from tkinter import font

def get_user_choice():
    user_choice = user_input.get().lower()
    if user_choice in ['rock', 'paper', 'scissors', 'lizard', 'spock']:
        play_game(user_choice)

def play_game(user_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors', 'lizard', 'spock'])
    determine_winner(user_choice, computer_choice)

def determine_winner(user_choice, computer_choice):
    result = tk.StringVar()

    if user_choice == computer_choice:
        result.set("It's a tie!")
    elif (user_choice == 'rock' and (computer_choice == 'scissors' or computer_choice == 'lizard')) or \
         (user_choice == 'paper' and (computer_choice == 'rock' or computer_choice == 'spock')) or \
         (user_choice == 'scissors' and (computer_choice == 'paper' or computer_choice == 'lizard')) or \
         (user_choice == 'lizard' and (computer_choice == 'paper' or computer_choice == 'spock')) or \
         (user_choice == 'spock' and (computer_choice == 'rock' or computer_choice == 'scissors')):
        result.set("Congratulations! You win!")
    else:
        result.set("Sorry, you lost.")

    result_label.config(text=result.get())

# Create the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors, Lizard, Spock")

# Set window dimensions and center it on the screen
window_width = 600
window_height = 300
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Set window background color and font styles
window.configure(bg='#F5F5F5')
title_font = font.Font(family='Arial', size=20, weight='bold')
button_font = font.Font(family='Arial', size=14)

# Create GUI elements
title_label = tk.Label(window, text="Rock, Paper, Scissors, Lizard, Spock", font=title_font, bg='#F5F5F5')
title_label.pack(pady=20)

user_input_label = tk.Label(window, text="Enter your choice:", font=font.Font(family='Arial', size=12), bg='#F5F5F5')
user_input_label.pack()

user_input = tk.Entry(window, font=font.Font(family='Arial', size=12))
user_input.pack(pady=10)

play_button = tk.Button(window, text="Play", command=get_user_choice, font=button_font, bg='#4CAF50', fg='white', width=10)
play_button.pack(pady=10)

result_label = tk.Label(window, text="", font=font.Font(family='Arial', size=14, weight='bold'), bg='#F5F5F5')
result_label.pack()

# Start the main event loop
window.mainloop()
