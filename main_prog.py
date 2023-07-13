import tkinter as tk
from front_Frame import FrontPage
from information_page import InfoFrame
from Info2_frame import InfoFrame2
from search_frame import SearchFrame


class ContactTracing(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Configure main application window
        self.title("Covid Contact Tracing App")
        self.geometry("900x500")

        self.frames = []
        self.current_frame = 0

        # Create three frame instances
        self.frame0 = FrontPage(self, self.switch_frame)
        self.frame1 = InfoFrame(self, self.switch_frame)
        self.frame2 = InfoFrame2(self, self.switch_frame)
        self.frame3 = SearchFrame(self, self.switch_frame)

        self.frames = [self.frame0, self.frame1, self.frame2, self.frame3]

        # Show the first frame
        self.show_frame(self.current_frame)

    def show_frame(self, frame_number):
        frame = self.frames[frame_number]
        frame.pack(fill="both", expand=True)
        self.current_frame = frame_number

    def switch_frame(self, frame_number):
        self.frames[self.current_frame].pack_forget()  # Hide the current frame
        self.show_frame(frame_number)  # Show the new frame

if __name__ == "__main__":
    app = ContactTracing()
    app.mainloop()
