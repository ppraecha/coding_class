import tkinter as tk
import screen2 as s2


class Screen:
    def __init__(self, number):
        self.number = number
        self.root = tk.Tk()
        self.root.title("Screen 1")
        self.label = tk.Label(self.root, text=str(self.number))
        self.label.pack()
        self.button = tk.Button(self.root, text="Change Screen", command=self.change_screen)
        self.button.pack()
        self.root.mainloop()

    def change_screen(self):
        self.root.destroy()
        self.number += 1
        s2.Screen(self.number)
