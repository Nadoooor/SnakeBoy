import tkinter as tk
from tkinter import font as tkfont

class ClassicCounterApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configure main window
        self.title("Standard Tkinter GUI")
        self.geometry("400x300")
        self.configure(bg="#f0f0f0")  # Set window background color

        # Initialize state tracker
        self.counter = 0

        # Define custom fonts
        title_font = tkfont.Font(family="Helvetica", size=18, weight="bold")
        count_font = tkfont.Font(family="Helvetica", size=36, weight="bold")
        btn_font = tkfont.Font(family="Helvetica", size=14, weight="bold")

        # Title Label
        self.title_label = tk.Label(
            self, 
            text="Interactive Counter", 
            font=title_font,
            bg="#f0f0f0",
            fg="#333333"
        )
        self.title_label.pack(padx=20, pady=(40, 20))

        # Number Display Label
        self.count_label = tk.Label(
            self, 
            text=str(self.counter), 
            font=count_font,
            bg="#f0f0f0",
            fg="#007fff"  # Blue accent text
        )
        self.count_label.pack(padx=20, pady=10)

        # Button Layout Frame
        self.button_frame = tk.Frame(self, bg="#f0f0f0")
        self.button_frame.pack(padx=20, pady=20)

        # Decrement Button (-)
        self.minus_button = tk.Button(
            self.button_frame, 
            text="-", 
            width=5,
            font=btn_font,
            bg="#dcdcdc",
            fg="#333333",
            activebackground="#bfbfbf",
            command=self.decrease_count
        )
        self.minus_button.grid(row=0, column=0, padx=10)

        # Increment Button (+)
        self.plus_button = tk.Button(
            self.button_frame, 
            text="+", 
            width=5,
            font=btn_font,
            bg="#007fff",
            fg="white",
            activebackground="#005fcc",
            command=self.increase_count
        )
        self.plus_button.grid(row=0, column=1, padx=10)

    def increase_count(self):
        self.counter += 1
        self.count_label.config(text=str(self.counter))

    def decrease_count(self):
        self.counter -= 1
        self.count_label.config(text=str(self.counter))

if __name__ == "__main__":
    app = ClassicCounterApp()
    app.mainloop()
