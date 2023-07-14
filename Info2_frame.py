import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
from information_page import InfoFrame


# Create class for Info page
class InfoFrame2(InfoFrame):
    def __init__(self, parent, switch_frame):
        super().__init__(parent, switch_frame)
        self.label = tk.Label(self, text="Frame 2")
        self.label.pack(pady=20)
        # Window won't be maximized
        parent.resizable(False, False)

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
        self.submit_button = tk.Button(self, text="Submit", height=1, font=("Arial", 11), bg="green", command=lambda: [self.submit_additional(), self.create_popup(), switch_frame(0), self.clear_fields()])
        self.submit_button.place(x=430, y=430)
    
    def submit_additional(self):
        time = self.entry_loc.get()
        place = self.entry_phb.get()
                
        additional_info_string = f"Date of Last Visit: {time}, "
        additional_info_string += f"Places have been: {place}\n"

        with open("contact_tracing_data.txt", "a") as file:
            file.write(additional_info_string)
    
    # Clear field after submission
    def clear_fields(self):
        self.entry_loc.delete(0, tk.END)
        self.entry_phb.delete(0, tk.END)



    # Create pop up notice
    def create_popup(self):
        messagebox.showinfo("Success!", "Your information was submitted sucessfully!!")
