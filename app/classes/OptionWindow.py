import tkinter as tk

class OptionWindow(tk.Toplevel):
    def __init__(self, parent, options : dict = None):
        tk.Toplevel.__init__(self, parent)
        self.loaded_options = options
        self.title("Options")
        self.geometry(f"300x200+{str(parent.winfo_x())}+{str(parent.winfo_y())}")
        self.minsize(300, 200)
        self.maxsize(300, 200)
        self.build_widgets()
        self.transient(parent)
        self.grab_set()
        

    def get_loaded_options(self):
        if self.loaded_options == None:
            print("No options loaded")
        else:
            return self.loaded_options

    def build_widgets(self):
        self.register_folder_text = tk.StringVar()
        self.register_folder_text.set(self.get_loaded_options()["path"]["registering_folder"])

        self.folder_label = tk.Label(self, text="Fichier de destination:")
        self.folder_entry = tk.Entry(self , textvariable= self.register_folder_text)

        self.folder_button = tk.Button(self, text="Parcourir", command="", width=10, height=10)
        self.option_label = tk.Label(self, text="Options")
        self.option_label.pack(padx=10, pady=10)
        self.folder_label.pack(padx=10, pady=10)
        self.folder_entry.pack(padx=10, pady=10)
        self.folder_button.pack(padx=10, pady=10)
    