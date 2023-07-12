import tkinter as tk

class ThankYouPage(tk.Tk):
    # create main window
    def __init__(self):
        super().__init__()
        self.title("Submitted sucessfully!")
        self.geometry("300x50")

        self.thankyou = tk.Label(self, text = "Information submitted sucessfuly!!", font=("Arial", 12))
        self.thankyou.place(x= 30, y= 10)

if __name__ == "__main__":
    root = ThankYouPage()
    root.mainloop()
