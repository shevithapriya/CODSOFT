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
        
def exit_app():
    root.destroy()  

root = tk.Tk()
root.title("Basic Calculator")
root.configure(bg="#000000")  

entry_field = tk.Entry(root, width=35, borderwidth=5, bg="#FFFFFF")  
entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for button_text, row, column in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=20, bg="#333333", fg="#FFFFFF",  
                       command=lambda value=button_text: button_click(value))
    button.grid(row=row, column=column, padx=5, pady=5)

button_clear = tk.Button(root, text='Clear', padx=15, pady=20, bg="#666666", fg="#FFFFFF",  
                         command=button_clear)
button_clear.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

button_exit = tk.Button(root, text='Exit', padx=15, pady=20, bg="#666666", fg="#FFFFFF",  
                        command=exit_app)  
button_exit.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

button_equal = tk.Button(root, text='=', padx=20, pady=20, bg="#666666", fg="#FFFFFF", 
                         command=button_equal)
button_equal.grid(row=4, column=2, padx=5, pady=5)

root.mainloop()
