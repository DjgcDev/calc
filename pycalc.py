import tkinter as tk
def click(btn):
    if btn == "=":
            result.set(str(eval(result.get())))
    elif btn == "C":
        result.set("")
    else:
        result.set(result.get() + btn)
root = tk.Tk()
root.title("Calculator")
result = tk.StringVar()
entry = tk.Entry(root, textvariable=result, font=("Arial", 18), bd=8, bg="#FFF7D1", justify="right")
entry.grid(row=0, column=0, columnspan=4)
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]
for i, btn in enumerate(buttons):
    tk.Button(root, text=btn, bg="#8B5DFF", font=("Arial", 18), width=5, command=lambda b=btn: click(b)).grid(row=i//4 + 1, column=i % 4)
root.mainloop()
