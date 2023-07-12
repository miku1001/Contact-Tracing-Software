import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox

# Create class for Info page
class InfoFrame2(tk.Frame):
    def __init__(self, parent, switch_frame):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="Frame 2")
        self.label.pack(pady=20)

        # Import bg image
        image = Image.open("FFPAGE BG.png")
        image = image.resize((900, 500), Image.NEAREST)
        self.bg_image = ImageTk.PhotoImage(image)

        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Location
        self.loc = tk.Label(self,text = "When was your most recent visit to this location ?*", height=1, font=("Arial", 15))
        self.loc.place(x=30, y=70)
        self.loc.config(bg="#BAF8FA")

        self.entry_loc = tk.Entry(self, width=140)
        self.entry_loc.place(x=30, y= 110)

        # Places have been
        self.phb = tk.Label(self,text = "Since Then until today, what places have you been ? ", height=1, font=("Arial", 15))
        self.phb.place(x=30, y=160)
        self.phb.config(bg="#BAF8FA")

        self.entry_phb = tk.Entry(self, width=140)
        self.entry_phb.place(x=30, y= 200)

        # Insert submit button and Instruction
        self.info = tk.Label(self,text = "Check if your information is correct", height=1, font=("Arial", 11, "italic"))
        self.info.place(x=340, y=400)
        self.info.config(bg="#BAF8FA")

        # submit button
        self.submit_button = tk.Button(self, text="Submit", height=1, font=("Arial", 11), bg="green", command=lambda: [switch_frame(0), self.create_popup()])
        self.submit_button.place(x=420, y=430)
    

    def create_popup(self):
        messagebox.showinfo("Yehey!", "Your information is submittted sucessfully!!")
