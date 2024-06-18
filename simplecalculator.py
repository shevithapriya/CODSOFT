import tkinter as tk

def button_click(value):
    current = entry_field.get()
    entry_field.delete(0, tk.END)
    entry_field.insert(0, current + value)

def button_clear():
    entry_field.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry_field.get())
        entry_field.delete(0, tk.END)
        entry_field.insert(0, str(result))
    except Exception as e:
        entry_field.delete(0, tk.END)
        entry_field.insert(0, "Error")

# Function to exit the application
def exit_app():
    root.destroy()  # Destroys the main window and exits the application

# Create the main window
root = tk.Tk()
root.title("Basic Calculator")
root.configure(bg="#000000")  # Set background color to black

# Entry field for displaying input and output
entry_field = tk.Entry(root, width=35, borderwidth=5, bg="#FFFFFF")  # Set entry field background color to white
entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create buttons and place them in the grid
for button_text, row, column in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=20, bg="#333333", fg="#FFFFFF",  # Set button background and foreground color
                       command=lambda value=button_text: button_click(value))
    button.grid(row=row, column=column, padx=5, pady=5)

# Clear button
button_clear = tk.Button(root, text='Clear', padx=15, pady=20, bg="#666666", fg="#FFFFFF",  # Set clear button colors
                         command=button_clear)
button_clear.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Exit button
button_exit = tk.Button(root, text='Exit', padx=15, pady=20, bg="#666666", fg="#FFFFFF",  # Set exit button colors
                        command=exit_app)  # Bind exit_app function to command
button_exit.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

# Equal button
button_equal = tk.Button(root, text='=', padx=20, pady=20, bg="#666666", fg="#FFFFFF",  # Set equal button colors
                         command=button_equal)
button_equal.grid(row=4, column=2, padx=5, pady=5)

# Run the main loop
root.mainloop()
