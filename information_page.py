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
        self.stat3.place(x=170, y= 135)
        self.stat3.config(bg="#BAF8FA")

        self.stat4 = tk.Radiobutton(text="With Booster",font=("Arial", 10), variable=self.radio, value = "4")
        self.stat4.place(x=170, y= 157)
        self.stat4.config(bg="#BAF8FA")

        # Add checklist for symptoms
        # Symptoms
        self.vacc = tk.Label(self,text = "2. Symptoms experience in the past 7 days:", height=1, font=("Arial", 11))
        self.vacc.place(x=400, y=110)
        self.vacc.config(bg="#BAF8FA")

        # Checkbutton for symptoms
        self.symptom1 = tk.Checkbutton(self, text="Fever",fg="black", font=("Arial", 11)) 
        self.symptom1.place(x=420, y=135)
        self.symptom1.config(bg="#BAF8FA")

        self.symptom2 = tk.Checkbutton(self, text="Difficulty in breathing",fg="black", font=("Arial", 11)) 
        self.symptom2.place(x=420, y=157)
        self.symptom2.config(bg="#BAF8FA")

        self.symptom3 = tk.Checkbutton(self, text="Cough",fg="black", font=("Arial", 11)) 
        self.symptom3.place(x=420, y=179)
        self.symptom3.config(bg="#BAF8FA")

        self.symptom4 = tk.Checkbutton(self, text="Lost of sense of taste or smell",fg="black", font=("Arial", 11)) 
        self.symptom4.place(x=650, y=135)
        self.symptom4.config(bg="#BAF8FA")

        self.symptom5 = tk.Checkbutton(self, text="Sore throat",fg="black", font=("Arial", 11)) 
        self.symptom5.place(x=650, y=157)
        self.symptom5.config(bg="#BAF8FA")

        self.no_symptom = tk.Checkbutton(self, text="None of the above",fg="black", font=("Arial", 11)) 
        self.no_symptom.place(x=650, y=179)
        self.no_symptom.config(bg="#BAF8FA")

        # In contact with someone positive
        self.vacc = tk.Label(self,text = "3. Have you been in close contact with someone who has tested positive for " 
                             "COVID-19 in the past 14 days?", height=1, font=("Arial", 11))
        self.vacc.place(x=30, y=220)
        self.vacc.config(bg="#BAF8FA")

        # Yes or no
        self.radio = tk.IntVar()
        self.yes1 = tk.Radiobutton(text="Yes",font=("Arial", 10),variable=self.radio,  value = "1")
        self.yes1.place(x=40, y= 245)
        self.yes1.config(bg="#BAF8FA")

        self.no1 = tk.Radiobutton(text="No",font=("Arial", 10),variable=self.radio,  value = "2")
        self.no1.place(x=130, y= 245)
        self.no1.config(bg="#BAF8FA")

        # In contact with someone with symptoms
        self.vacc = tk.Label(self,text = "4. Have you been in close contact with someone who has symptoms "
                             "stated above?", height=1, font=("Arial", 11))
        self.vacc.place(x=30, y=280)
        self.vacc.config(bg="#BAF8FA")

        # Yes or no
        self.radio = tk.IntVar()
        self.yes2 = tk.Radiobutton(text="Yes",font=("Arial", 10),variable=self.radio,  value = "1")
        self.yes2.place(x=40, y= 305)
        self.yes2.config(bg="#BAF8FA")

        self.no2 = tk.Radiobutton(text="No",font=("Arial", 10),variable=self.radio,  value = "2")
        self.no2.place(x=130, y= 305)
        self.no2.config(bg="#BAF8FA")

        # In contact with someone with symptoms
        self.vacc = tk.Label(self,text = "5. Have you been tested for Covid-19 in the last 14 days? "
                             "stated above?", height=1, font=("Arial", 11))
        self.vacc.place(x=30, y=330)
        self.vacc.config(bg="#BAF8FA")

        # Tested?
        self.radio = tk.IntVar()
        self.yes_negative = tk.Radiobutton(text="Yes (Negative)",font=("Arial", 10),variable=self.radio,  value = "1")
        self.yes_negative.place(x=40, y= 370 )
        self.yes_negative.config(bg="#BAF8FA")

        self.yes_positive = tk.Radiobutton(text="Yes (Positive) ",font=("Arial", 10),variable=self.radio,  value = "2")
        self.yes_positive.place(x=40, y= 400)
        self.yes_positive.config(bg="#BAF8FA")
        
        self.yes_pending = tk.Radiobutton(text="Yes (Pending) ",font=("Arial", 10),variable=self.radio,  value = "2")
        self.yes_pending.place(x=200, y= 370)
        self.yes_pending.config(bg="#BAF8FA")

        self.not_tested = tk.Radiobutton(text="No ",font=("Arial", 10),variable=self.radio,  value = "2")
        self.not_tested.place(x=200, y= 400)
        self.not_tested.config(bg="#BAF8FA")

        # Insert submit button and Instruction
        self.vacc = tk.Label(self,text = "Check if your information is correct", height=1, font=("Arial", 11))
        self.vacc.place(x=340, y=430)
        self.vacc.config(bg="#BAF8FA")

        # subit button
        self.submit_button = tk.Button(self, text="Add Data", height=1, font=("Arial", 11))
        self.submit_button.place(x=420, y=460)



        



    # Display text will be gone if the user click the entry
    def clear_date_text(self, event):
        self.entry_date.delete(0, tk.END)
        self.entry_date.config(fg="black")
    def clear_name_text(self, event):
        self.entry_name.delete(0, tk.END)
        self.entry_name.config(fg="black")
    def clear_number_text(self, evert):
        self.entry_number.delete(0, tk.END)
        self.entry_number.config(fg="black")
    def clear_email_text(self, event):
        self.entry_email.delete(0, tk.END)
        self.entry_email.config(fg="black")  
