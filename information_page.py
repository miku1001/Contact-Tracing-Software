# Import libraries
import tkinter as tk
from PIL import ImageTk, Image

# Create class for Info page
class InfoFrame(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        # Import bg image
        image = Image.open("FFPAGE BG.png")
        image = image.resize((900, 500), Image.NEAREST)
        self.bg_image = ImageTk.PhotoImage(image)

        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Information label
        self.info = tk.Label(self,text = "Please input your information. ", height=1, font=("Arial", 12))
        self.info.place(x=30, y=10)
        self.info.config(bg="#BAF8FA")

        # Date
        self.date = tk.Label(self, text = "Date", height = 1, font=("Arial", 12)
        self.date.place(x = 30, y =40)
        self.date.config(bg="#BAF8FA")

        # Date Entry
        self.entry_date = tk.Entry(self, width = 30)
        self.entry_date.place(x=120, y=43)