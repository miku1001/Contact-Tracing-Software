import tkinter as tk
from PIL import ImageTk, Image
from functools import partial

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
        self.submit_button = tk.Button(self, text="Search", height=1, font=("Arial", 10), bg="white", command= self.reader)
        self.submit_button.place(x=34, y=120)

        # Create back to menu button
        self.submit_button = tk.Button(self, text="Back to Menu", height=1, font=("Arial", 12), bg="white", command=lambda: self.switch_frame(0))
        self.submit_button.place(x=410, y=450)

        # Create instruction
        self.search = tk.Label(self,text = "Check the information in the box below.", height=1, font=("Arial", 11))
        self.search.place(x=30, y=180)
        self.search.config(bg="#BAF8FA")

      # Create Canvas which will serve as the monitor
        self.canvas = tk.Canvas(self, width=700, height=220, bg="white", highlightthickness=1, highlightbackground="black")
        self.canvas.place(x=30, y=210)

    def reader(self):
        search_query = self.entry_search.get()

        # Clear canvas
        self.canvas.delete("all")

        # Read data from text file
        found_data = False

        # Read data from text file
        with open("contact_tracing_data.txt", "r") as file:
            for line in file:
                values = line.strip().split(", ")
                if values[1] == search_query:
                    info = {
                        "Date": values[0],
                        "Name": values[1],
                        "Contact Number": values[2],
                        "Email": values[3],
                        "Vaccination Status": values[4],
                        "Close Contact with Positive COVID-19 Case": values[5],
                        "Close Contact with Symptoms": values[6],
                        "Tested for COVID-19": values[7],
                        "Symptoms experienced in the past 7 days": values[8],
                        "Date of Last Visit": values[9],
                        "Places have been": values[10]
                        }
                    info_text = ""
                    for key, value in info.items():
                        info_text += f"{key}: {value}\n"
                    self.canvas.create_text(10, 10, anchor="nw", text=info_text, font=("Arial", 11), fill="black")
                    found_data = True
                    break
        if not found_data:
            self.canvas.create_text(10, 10, anchor="nw", text="No information found.", font=("Arial", 11), fill="black")
            
    # resize image 
    def resize_image(self, event):
        new_width = event.width
        new_height = event.height

        resized_image = self.image.resize((new_width, new_height), Image.NEAREST)
        self.bg_image = ImageTk.PhotoImage(resized_image)
        self.bg_label.configure(image=self.bg_image) 
