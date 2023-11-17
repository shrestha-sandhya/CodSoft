import tkinter as tk
from random import randint

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!", 0, 0
    elif (player == "rock" and computer == "scissor") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissor" and computer == "paper"):
        return "Player wins!", 1, 0
    else:
        return "Computer wins!", 0, 1

def play_round(player_choice_label, player_score_label, computer_score_label):
    choices = ["rock", "paper", "scissor"]
    player_choice = player_choice_label.get().lower()
    computer_choice = choices[randint(0, 2)]
    
    result, player_score, computer_score = determine_winner(player_choice, computer_choice)
    result_label.config(text=f"Computer plays {computer_choice}\n{result}")

    player_score_label.config(text=f"Player Score: {player_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

def on_quit():
    root.destroy()

root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
player_choice_label = tk.Entry(root)
play_button = tk.Button(root, text="Play", command=lambda: play_round(player_choice_label, player_score_label, computer_score_label))
result_label = tk.Label(root, text="")
player_score_label = tk.Label(root, text="Player Score: 0")
computer_score_label = tk.Label(root, text="Computer Score: 0")

instruction_label.grid(row=0, column=0, columnspan=2, pady=20)
player_choice_label.grid(row=1, column=0, padx=50, pady=20)
play_button.grid(row=1, column=1, pady=10)
result_label.grid(row=2, column=0, columnspan=2, pady=20)
player_score_label.grid(row=3, column=0, pady=10)
computer_score_label.grid(row=3, column=1, pady=10)

root.protocol("WM_DELETE_WINDOW", on_quit)


root.mainloop()
