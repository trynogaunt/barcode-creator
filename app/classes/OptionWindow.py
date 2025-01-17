import tkinter as tk

class OptionWindow(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Options")
        self.geometry(f"300x200+{str(parent.winfo_x())}+{str(parent.winfo_y())}")
        self.minsize(300, 200)
        self.maxsize(300, 200)
        self.build_widgets()
        self.transient(parent)
        self.grab_set()

    def build_widgets(self):
        self.folder_label = tk.Label(self, text="Fichier de destination:")
        self.folder_entry = tk.Entry(self , textvariable="folder_target")
        self.folder_button = tk.Button(self, text="Parcourir", command="", width=10, height=10)
        self.option_label = tk.Label(self, text="Options")
        self.option_label.pack(padx=10, pady=10)
        self.folder_label.pack(padx=10, pady=10)
        self.folder_entry.pack(padx=10, pady=10)
        self.folder_button.pack(padx=10, pady=10)
    