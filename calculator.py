import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Miniräknare")
        self.root.geometry("300x400")

        self.expression = ""

        # Display
        self.display = tk.Entry(root, font=("Arial", 20), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            tk.Button(root, text=button, font=("Arial", 18), command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Clear button
        tk.Button(root, text="C", font=("Arial", 18), command=self.clear).grid(row=row, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        tk.Button(root, text="←", font=("Arial", 18), command=self.backspace).grid(row=row, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Configure grid weights
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

        # Bind keyboard events
        self.root.bind('<Key>', self.on_key_press)

    def on_button_click(self, char):
        if char == '=':
            try:
                self.expression = str(eval(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, self.expression)
            except:
                messagebox.showerror("Fel", "Ogiltigt uttryck")
                self.clear()
        else:
            self.expression += char
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

    def on_key_press(self, event):
        char = event.char
        if char in '0123456789.+-*/':
            self.on_button_click(char)
        elif event.keysym == 'Return':
            self.on_button_click('=')
        elif event.keysym == 'BackSpace':
            self.backspace()
        elif char.lower() == 'c':
            self.clear()

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)

    def backspace(self):
        self.expression = self.expression[:-1]
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()