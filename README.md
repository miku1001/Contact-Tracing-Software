# COVIDTraceLink 🔗😷

***COVIDTraceLink*** is a specialized contact management software application designed to assist in the management and tracking 
of COVID-19 related contacts. It aims to help individuals, healthcare providers, and public health authorities effectively track, 
trace, and monitor potential COVID-19 exposures.


### Table of Contents
- [Tech](#tech)
- [Features](#feat)
- [Project Structure](#proj)
- [Run](#run)
- [How to run in IDE](#ide)
- [Contact](#contact)

### Tech <a name="tech"></a>
* **Object Oriented Programming** or **OOP** is a programming approach that focuses on objects. Objects are like building 
blocks that contain both data and actions. By using objects, we can make our code more organized, reusable, and easier to understand and maintain. 
* **Tkinter** is a Python library for creating graphical user interfaces (GUIs) that are widely used and come included with Python distributions. 
It provides a set of pre-built UI components, known as widgets, along with layout managers for arranging them within the application window.

Uses:
* <img src="https://logowik.com/content/uploads/images/python4089.logowik.com.webp" alt="Python Logo" width="20"> Python - Programming Language

### Features <a name="feat"></a>
- Add Information - COVIDTraceLink allows the user to input their basic contact tracing information such as name, and contact numbers without limit.
- Search - COVIDTraceLink also allows users to navigate the saved information in the database by entering the right name.
- Exit - This software also has an exit button that allows the user to close the application after using it.

### Project Structure <a name="proj"></a>
- main_prog.py: It handles the frame switching code, as well as the commands that are necessary to start the programs
- front_Frame.py: It handles the program for the menu page where it has the button to redirect to other frames.
- information_page.py: It handles the information frame, In contains different contact tracing questions such as name, date, contact, etc.
- Info2_frame.py: Like information_page.py, it also handles the additional covid contact tracing information.
- search_frame.py: It handles the program for navigating information from the database.
- contact_tracing_data.txt: It serves as the database, where all the information input by users is stored.

### Run <a name="run"></a>
     $ git clone https://github.com/miku1001/Contact-Tracing-Software.git
     $ cd Contact-Tracing-Software
     $ python main_prog.py
     $ python front_Frame.py
     $ python information_page.py
     $ python Info2_frame.py
     $ python search_frame.py
     
## How to run in IDE <a name="ide"></a>

To run this program, you need to:
1. Clone the repository from Github.

        $ git clone https://github.com/miku1001/Contact-Tracing-Software.git
2. Open your preferred IDE software on your computer.
3. Import the program in your IDE by selecting the cloned repository as the program directory to import the code.
4. Run the program.
   
    **Usage**
    - Input data: Click the "Add Information" button to start input data.
    - Search: Click the "Search" button to navigate saved information and type their name.
    - Exit: Click the "Exit" button and wait the program to close

### Contact☎️ <a name="contact"></a>
  For any questions or inquiries about this program, please contact:
  
  - Ted Paulo Feranil: pauloted.22@gmail.com
