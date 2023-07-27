import tkinter as tk
import ast


def on_click(button_text):
    current_text = entry.get()

    if button_text == "=":
        try:
            # Safely evaluate the expression using the ast module
            result = eval_expr(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)


def eval_expr(expression):
    # Use the ast module to safely evaluate the expression
    return ast.literal_eval(expression)


# Create the main window
root = tk.Tk()
root.title("Advanced Calculator")

# Create and place widgets
entry = tk.Entry(root, font=("Arial", 20), width=15, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

row = 1
col = 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, font=("Arial", 20), width=5, height=2,
                       command=lambda text=button_text: on_click(text))
    button.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the main event loop
root.mainloop()
