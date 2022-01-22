import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=45, borderwidth=10)
entry.grid(row=0, column=0, columnspan=4, padx=5, ipady=5)


def button_number(num):
    entry.insert(tk.END, num)


def clear():
    entry.delete(0, tk.END)


def addition():
    global first_num
    global state
    state = "+"
    first_num = entry.get()
    entry.delete(0, tk.END)


def minus():
    global first_num
    global state
    state = "-"
    first_num = entry.get()
    entry.delete(0, tk.END)


def multiply():
    global first_num
    global state
    state = "*"
    first_num = entry.get()
    entry.delete(0, tk.END)


def divide():
    global first_num
    global state
    state = "/"
    first_num = entry.get()
    entry.delete(0, tk.END)


def equal():
    global first_num
    global state
    if state is None:
        return
    second_num = entry.get()
    entry.delete(0, tk.END)
    if state == "+":
        entry.insert(0, int(first_num) + int(second_num))
    elif state == "-":
        entry.insert(0, int(first_num) - int(second_num))
    elif state == "*":
        entry.insert(0, int(first_num) * int(second_num))
    elif state == "/":
        entry.insert(0, int(first_num) // int(second_num))


# Number Button
button0 = tk.Button(root, text="0", padx=20, pady=15, borderwidth=3, command=lambda: button_number(0))
button1 = tk.Button(root, text="1", padx=20, pady=15, borderwidth=3, command=lambda: button_number(1))
button2 = tk.Button(root, text="2", padx=20, pady=15, borderwidth=3, command=lambda: button_number(2))
button3 = tk.Button(root, text="3", padx=20, pady=15, borderwidth=3, command=lambda: button_number(3))
button4 = tk.Button(root, text="4", padx=20, pady=15, borderwidth=3, command=lambda: button_number(4))
button5 = tk.Button(root, text="5", padx=20, pady=15, borderwidth=3, command=lambda: button_number(5))
button6 = tk.Button(root, text="6", padx=20, pady=15, borderwidth=3, command=lambda: button_number(6))
button7 = tk.Button(root, text="7", padx=20, pady=15, borderwidth=3, command=lambda: button_number(7))
button8 = tk.Button(root, text="8", padx=20, pady=15, borderwidth=3, command=lambda: button_number(8))
button9 = tk.Button(root, text="9", padx=20, pady=15, borderwidth=3, command=lambda: button_number(9))
# Sign Button
button_add = tk.Button(root, text="+", padx=20, pady=15, borderwidth=3, command=addition)
button_minus = tk.Button(root, text="-", padx=20, pady=15, borderwidth=3, command=minus)
button_multiply = tk.Button(root, text="x", padx=20, pady=15, borderwidth=3, command=multiply)
button_divide = tk.Button(root, text="/", padx=20, pady=15, borderwidth=3, command=divide)
button_equal = tk.Button(root, text="=", padx=20, pady=15, borderwidth=3, command=equal)
button_clear = tk.Button(root, text="C", padx=20, pady=15, borderwidth=3, command=clear)

button0.grid(row=5, column=0)
button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)
button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)

button_add.grid(row=5, column=3)
button_minus.grid(row=4, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=2, column=3)
button_equal.grid(row=5, column=2)
button_clear.grid(row=5, column=1)


first_num = 0
state = None
root.mainloop()
