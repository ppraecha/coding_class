import tkinter as tk

root = tk.Tk()


def button_click(word):
    temp_label = tk.Label(root, text=word)
    temp_label.pack()


# Meanie Button
button1 = tk.Button(root, text="Don't Push", padx=30, pady=20, bg="white",
                    command=lambda: button_click("I told you not to press the button!"))
button1.pack()

# Kind Button
button2 = tk.Button(root, text="Please Push", padx=30, pady=20, bg="white",
                    command=lambda: button_click("Good Job!"))
button2.pack()

root.mainloop()
