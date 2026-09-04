import tkinter as tk

# Create window
root = tk.Tk()
root.title("✨ Colorful Calculator ✨")
root.geometry("380x550")
root.resizable(False, False)
root.configure(bg="#1e1e2f")

# Display
display = tk.Entry(
    root,
    font=("Arial", 28, "bold"),
    bg="#ffffff",
    fg="#222222",
    justify="right",
    bd=0
)
display.pack(
    padx=20,
    pady=25,
    ipady=15,
    fill="x"
)


# Functions
def click(value):
    display.insert(tk.END, value)


def clear():
    display.delete(0, tk.END)


def delete():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])


def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# Button style
button_font = ("Arial", 18, "bold")

# Buttons
buttons = [
    ["C", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="]
]

# Colors
number_color = "#3b3b5c"
operator_color = "#ff8c42"
clear_color = "#ff4d6d"
equal_color = "#00c896"

# Create buttons
for row in buttons:
    frame = tk.Frame(root, bg="#1e1e2f")
    frame.pack(expand=True, fill="both", padx=15)

    for button in row:

        if button == "C":
            color = clear_color
            command = clear

        elif button == "⌫":
            color = "#9b59b6"
            command = delete

        elif button == "=":
            color = equal_color
            command = calculate

        elif button in ["+", "-", "*", "/", "%"]:
            color = operator_color
            command = lambda x=button: click(x)

        else:
            color = number_color
            command = lambda x=button: click(x)

        tk.Button(
            frame,
            text=button,
            font=button_font,
            bg=color,
            fg="white",
            activebackground="#ffffff",
            activeforeground="#222222",
            bd=0,
            command=command
        ).pack(
            side="left",
            expand=True,
            fill="both",
            padx=5,
            pady=5
        )


# Footer
tk.Label(
    root,
    text="💜 Learn with Rakshita 💜",
    font=("Arial", 12, "bold"),
    bg="#1e1e2f",
    fg="#ffffff"
).pack(pady=10)


# Run application
root.mainloop()