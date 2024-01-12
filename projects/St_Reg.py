import tkinter as tk

def submit_registration():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    email = email_entry.get()
    gender = gender_var.get()
    program = program_var.get()

    registration_info = f"Registration Details:\nFirst Name: {first_name}\nLast Name: {last_name}\nEmail: {email}\nGender: {gender}\nProgram: {program}"
    registration_label.config(text=registration_info)

# Create the main window
root = tk.Tk()
root.title("Student Registration Form")

# Create labels
first_name_label = tk.Label(root, text="First Name:")
last_name_label = tk.Label(root, text="Last Name:")
email_label = tk.Label(root, text="Email:")
gender_label = tk.Label(root, text="Gender:")
program_label = tk.Label(root, text="Program:")

first_name_label.pack()
last_name_label.pack()
email_label.pack()
gender_label.pack()
program_label.pack()

# Create entry fields
first_name_entry = tk.Entry(root)
last_name_entry = tk.Entry(root)
email_entry = tk.Entry(root)

first_name_entry.pack()
last_name_entry.pack()
email_entry.pack()

# Create gender radio buttons
gender_var = tk.StringVar()
male_radio = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
female_radio = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")

male_radio.pack()
female_radio.pack()

# Create program selection dropdown
program_var = tk.StringVar()
program_var.set("Select Program")
program_options = ["Computer Science", "Electrical Engineering", "Mechanical Engineering", "Physics"]

program_menu = tk.OptionMenu(root, program_var, *program_options)
program_menu.pack()

# Create a "Submit" button
submit_button = tk.Button(root, text="Submit", command=submit_registration)
submit_button.pack()

# Create a label to display registration information
registration_label = tk.Label(root, text="")
registration_label.pack()

# Start the GUI application
root.mainloop()