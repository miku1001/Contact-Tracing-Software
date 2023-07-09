# import tkinter, pillow library
import tkinter as tk
from PIL import ImageTk, image

# create class
class FrontPage(tk.Tk):
    # create main window
    def __init__(self):
        super().__init__()
        self.title("Covid-19 Contact Tracing App")

    # create background image for front page
    image = Image.open("Insert Image here") # image underway
    image = image.resize((900, 500), Image.NEAREST)
    self.bg_image = ImageTk.PhotoImage(image)

    self.bg_label = tk.Label(self, image = self.bg_image)
    self.bg_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

# create buttons
# add
# search

# create method for start button

# create method for search button