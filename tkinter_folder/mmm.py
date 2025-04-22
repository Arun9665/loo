
from tkinter import *
from PIL import ImageTk, Image  # Requires Pillow library

root = Tk()

# Alternative method: Setting a logo with PhotoImage (requires .png format)
logo = ImageTk.PhotoImage(Image.open(r"C:\Users\admin\Desktop\tkinter_folder\mango_icon.png"))
label = Label(root, image=logo)
label.pack()

root.mainloop()