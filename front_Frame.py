# import tkinter, pillow library
import tkinter as tk
from PIL import ImageTk, Image

# create class
class FrontPage(tk.Frame):
    # create main window
    def __init__(self, parent, switch_frame):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="Frame 0")
        self.label.pack(pady=20)

        # Window won't be maximized
        parent.resizable(False, False)

    # create background image for front page
        self.image = Image.open("FRONTPAGE BG.png")  # Update the image file path
        self.bg_image = ImageTk.PhotoImage(self.image)

        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # create buttons
        # add
        self.add_button = tk.Button(self, text="Add Data", command=lambda: switch_frame(1), width=12, height=1, font=("Arial", 18))
        self.add_button.place(x=518, y=290)

        # search
        self.search_button = tk.Button(self, text="Search", command=lambda: switch_frame(3), width=10, height=1, font=("Arial", 18))
        self.search_button.place(x=530, y=230)
        # exit button
        self.exit_button = tk.Button(self, text="Exit", command=lambda: quit(), width=10, height=1, font=("Arial", 18))
        self.exit_button.place(x=530, y=350)

    def show(self):
        self.pack()

    def hide(self):
        self.pack_forget()