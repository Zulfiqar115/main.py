import tkinter as tk
import random

def play_rps(user_choice):
    choices = ["Balakot", "Mansehra", "Islamabad"]
    computer_choice = random.choice(choices)

    result = ""
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "Balakot" and computer_choice == "Islamabad") or
        (user_choice == "Mansehra" and computer_choice == "Balakot") or
        (user_choice == "Islamabad" and computer_choice == "Mansehra")
    ):
        result = "You win!"
    else:
        result = "Computer wins!"

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# Create the main window
root = tk.Tk()
root.title("Balakot, Mansehra, Islamabad")

# Create labels
label = tk.Label(root, text="Choose your move:")
label.pack()

# Create buttons
Balakot_button = tk.Button(root, text="Balakot", command=lambda: play_rps("Balakot"))
Mansehra_button = tk.Button(root, text="Mansehra", command=lambda: play_rps("Mansehra"))
Islamabad_button = tk.Button(root, text="Islamabad", command=lambda: play_rps("Islamabad"))

Balakot_button.pack()
Mansehra_button.pack()
Islamabad_button.pack()

# Create a label for displaying the result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI application
root.mainloop()