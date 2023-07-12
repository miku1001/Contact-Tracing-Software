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
        self.info = tk.Label(self,text = "Please input your information. ", height=1, font=("Arial", 11))
        self.info.place(x=30, y=10)
        self.info.config(bg="#BAF8FA")

        # Date
        self.date = tk.Label(self, text = "Date", height = 1, font=("Arial", 12))
        self.date.place(x = 30, y =40)
        self.date.config(bg="#BAF8FA")

        # Date Entry
        self.entry_date = tk.Entry(self, width=30)
        self.entry_date.place(x=120, y=43)
        self.entry_date.insert(0, "MM/DD/YY")  # Set initial text
        self.entry_date.bind("<FocusIn>", self.clear_date_text)
        self.entry_date.config(fg="gray")
        
        # Name
        self.name = tk.Label(self, text = "Full Name", height = 1, font=("Arial", 12))
        self.name.place(x = 30, y =70)
        self.name.config(bg="#BAF8FA")

        # Name Entry
        self.entry_name = tk.Entry(self, width=40)
        self.entry_name.place(x=120, y= 73)
        self.entry_name.insert(0, "FIRSTNAME/LASTNAME/SURNAME")  # Set initial text
        self.entry_name.bind("<FocusIn>", self.clear_name_text)
        self.entry_name.config(fg="gray")

        # Contact label
        self.info = tk.Label(self,text = "Contact Details", height=1, font=("Arial", 12))
        self.info.place(x=390, y=43)
        self.info.config(bg="#BAF8FA")

        # Contact Number
        self.number = tk.Label(self, text = "Contact Number: ", height = 1, font=("Arial", 12))
        self.number.place(x = 390, y =70)
        self.number.config(bg="#BAF8FA")

        # CN Entry
        self.entry_number = tk.Entry(self, width=25)
        self.entry_number.place(x=520, y= 73)

        # Email
        self.email = tk.Label(self, text = "Email:", height = 1, font=("Arial", 12))
        self.email.place(x = 665, y =70)
        self.email.config(bg="#BAF8FA")

        # Email Entry
        self.entry_email = tk.Entry(self, width=25)
        self.entry_email.place(x=715, y= 73)
        self.entry_email.insert(0, "juan23@example.com")  # Set initial text
        self.entry_email.bind("<FocusIn>", self.clear_email_text)
        self.entry_email.config(fg="gray")

        # add division line
        self.line = tk.Canvas(self, width=900, height=1, bg="black", highlightthickness=0)
        self.line.place(x= 0, y=105)
        

        # Add radio button for covid information
        # Vaccination status
        self.vacc = tk.Label(self,text = "1. Vaccination Status", height=1, font=("Arial", 12))
        self.vacc.place(x=30, y=110)
        self.vacc.config(bg="#BAF8FA")
        
        # Vacc stat
        self.radio = tk.IntVar()
        self.stat1 = tk.Radiobutton(text="Not Yet",font=("Arial", 10),variable=self.radio,  value = "1")
        self.stat1.place(x=43, y= 135)
        self.stat1.config(bg="#BAF8FA")

        self.stat2 = tk.Radiobutton(text="1st Dose",font=("Arial", 10), variable=self.radio, value = "2")
        self.stat2.place(x=43, y= 157)
        self.stat2.config(bg="#BAF8FA")

        self.stat3 = tk.Radiobutton(text="2nd Dose",font=("Arial", 10), variable=self.radio, value = "3")
        self.stat3.place(x=43, y= 179)
        self.stat3.config(bg="#BAF8FA")

        self.stat4 = tk.Radiobutton(text="With Booster",font=("Arial", 10), variable=self.radio, value = "4")
        self.stat4.place(x=43, y= 201)
        self.stat4.config(bg="#BAF8FA")



    # Display text will be gone if the user click the entry
    def clear_date_text(self, event):
        self.entry_date.delete(0, tk.END)
    def clear_name_text(self, event):
        self.entry_name.delete(0, tk.END)
    def clear_number_text(self, evert):
        self.entry_number.delete(0, tk.END)
    def clear_email_text(self, event):
        self.entry_email.delete(0, tk.END)    
