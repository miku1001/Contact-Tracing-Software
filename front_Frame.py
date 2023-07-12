# import tkinter, pillow library
import tkinter as tk
from PIL import ImageTk, Image

#import Infoframe
from information_page import InfoFrame

# create class
class FrontPage(tk.Tk):
    # create main window
    def __init__(self):
        super().__init__()
        self.title("Covid-19 Contact Tracing App")
        self.geometry("900x500")

    # create background image for front page
        self.image = Image.open("FRONTPAGE BG.png")  # Update the image file path
        self.bg_image = ImageTk.PhotoImage(self.image)

        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # create buttons    
        # add
        self.add_button = tk.Button(self, text="Add Data", command=self.switch_to_infoframe, width=12, height=1, font=("Arial", 18))
        self.add_button.place(x=518, y=290)

        # search
        self.search_button = tk.Button(self, text="Search", command=self.search, width=10, height=1, font=("Arial", 18))
        self.search_button.place(x=530, y=230)

        self.bind("<Configure>", self.resize_image)

    # create method for start button
    def start(self):
        self.switch_to_()

    def switch_to_infoframe(self):
        info_frame = InfoFrame()
        info_frame.place(x=0, y=0, relwidth=1, relheight=1)

    # create method for search button
    def search(self):
        print("Temporary")

    # resize image 
    def resize_image(self, event):
        new_width = event.width
        new_height = event.height

        resized_image = self.image.resize((new_width, new_height), Image.NEAREST)
        self.bg_image = ImageTk.PhotoImage(resized_image)

        self.bg_label.configure(image=self.bg_image)



if __name__ == "__main__":
    root = FrontPage()
    root.mainloop()