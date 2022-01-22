import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

root = tk.Tk()
root.title("Load Image")
root.iconbitmap("./img_bin/ppicon.ico")

root.filename = filedialog.askopenfilename(initialdir="./", title="Select a Picture")
print(root.filename)

image1 = ImageTk.PhotoImage(Image.open(root.filename))
label = tk.Label(root, image=image1)
label.pack()

button = tk.Button(root, text="EXIT", command=root.destroy)
button.pack()

root.mainloop()
