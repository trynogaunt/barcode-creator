import tkinter as tk
import toml

class OptionWindow(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self)
        self.title("Options")
        self.geometry(f"300x200+{str(parent.winfo_x())}+{str(parent.winfo_y())}")
        self.minsize(300, 200)
        self.maxsize(300, 200)
        with open("app/core.toml") as f:
            config = toml.load(f)
            print("Loading configuration...")
            self.options = config["path"]["registering_folder"]
            print(f"Options {self.options} loaded")
            f.close()
        self.build_widgets()
        self.transient(parent)
        self.grab_set()

    def build_widgets(self):
        self.register_folder_text = tk.StringVar()
        self.register_folder_text.set(self.options)

        self.folder_label = tk.Label(self, text="Fichier de destination:")
        self.folder_entry = tk.Entry(self , textvariable= self.register_folder_text)

        self.folder_button = tk.Button(self, text="Parcourir", command="", width=10, height=10)
        self.option_label = tk.Label(self, text="Options")

        self.apply_button = tk.Button(self, text="Appliquer", command=self.apply_changes)

        self.option_label.pack(padx=10, pady=10)
        self.folder_label.pack(padx=10, pady=10)
        self.folder_entry.pack(padx=10, pady=10)
        #self.folder_button.pack(padx=10, pady=10)
        self.apply_button.pack(padx=10, pady=10)
    
    def apply_changes(self):
        self.options = self.register_folder_text.get()
        print(self.options)
        config = toml.load("app/core.toml")
        print(config)
        config["path"]["registering_folder"] = self.options
        f = open("app/core.toml", "w")
        toml.dump(config, f)
        f.close()
            #toml.dump(self.options, f))
    