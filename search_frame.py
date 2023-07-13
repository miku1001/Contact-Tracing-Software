import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox

# Create class for Info page
class SearchFrame(tk.Frame):
    def __init__(self, parent, switch_frame):
        tk.Frame.__init__(self, parent)
        self.switch_frame = switch_frame

        self.label = tk.Label(self, text="Search")
        self.label.pack(pady=20)

       # Create a separate frame for encapsulating the widgets
        content_frame = tk.Frame(self)
        content_frame.pack()

        # Import bg image
        self.image = Image.open("FFPAGE BG.png")
        self.bg_image = ImageTk.PhotoImage(self.image)
        self.bind("<Configure>", self.resize_image)

        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # resize image 
    def resize_image(self, event):
        new_width = event.width
        new_height = event.height

        resized_image = self.image.resize((new_width, new_height), Image.NEAREST)
        self.bg_image = ImageTk.PhotoImage(resized_image)
        self.bg_label.configure(image=self.bg_image) 