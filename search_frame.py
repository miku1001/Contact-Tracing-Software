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

        # Import bg image
        self.image = Image.open("FFPAGE BG.png")
        self.bg_image = ImageTk.PhotoImage(self.image)
        self.bind("<Configure>", self.resize_image)

        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.search = tk.Label(self,text = "Find saved information here:", height=1, font=("Arial", 11))
        self.search.place(x=30, y=30)
        self.search.config(bg="#BAF8FA")


        self.search = tk.Label(self,text = "Input Name", height=1, font=("Arial", 11))
        self.search.place(x=30, y=70)
        self.search.config(bg="#BAF8FA")

        # Enter Name
        self.entry_search = tk.Entry(self, width=40)
        self.entry_search.place(x=34, y=95)

        # Create Search Button
        self.submit_button = tk.Button(self, text="Search", height=1, font=("Arial", 10), bg="white")
        self.submit_button.place(x=34, y=135)


        self.search = tk.Label(self,text = "Check the information in the box below.", height=1, font=("Arial", 11))
        self.search.place(x=30, y=180)
        self.search.config(bg="#BAF8FA")

      # Create Canvas which will serve as the monitor
        self.canvas = tk.Canvas(self, width=400, height=220, bg="white", highlightthickness=1, highlightbackground="black")
        self.canvas.place(x=30, y=210)

    # resize image 
    def resize_image(self, event):
        new_width = event.width
        new_height = event.height

        resized_image = self.image.resize((new_width, new_height), Image.NEAREST)
        self.bg_image = ImageTk.PhotoImage(resized_image)
        self.bg_label.configure(image=self.bg_image) 
