import tkinter as tk

class OptionWindow(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Options")
        self.geometry("300x200")
        self.minsize(300, 200)
        self.maxsize(300, 200)
        self.build_widgets()

    def build_widgets(self):
        self.option_label = tk.Label(self, text="Options")
        self.option_label.pack(padx=10, pady=10)