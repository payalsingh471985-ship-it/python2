import tkinter as tk
import random

def play(choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    if choice == computer_choice:
        result = "It's a Tie!"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"
    result_label.config(text=f"Your choice: {choice}\nComputer choice: {computer_choice}\nResult: {result}")

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")
root.config(bg="#f0f0f0")

heading = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), bg="#f0f0f0")
heading.pack(pady=10)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="Rock", width=12, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="Paper", width=12, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="Scissors", width=12, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0", fg="blue")
result_label.pack(pady=20)

root.mainloop()
