# Import libraries
import tkinter as tk
from PIL import ImageTk, Image

# Create class for Info page
class InfoFrame(self):
    tk.Frame.__init__(self)

    # Import bg image
    image = Image.open("FFPAGE BG.png")
    image = image.resize((900, 500), Image.NEAREST)
    self.bg_image = ImageTk.PhotoImage(image)