import os
import sys
import tkinter as tk
from functions import barcode_function as bf , utils , menu_function as mf
import toml

class Application(tk.Tk):
    def __init__(self , title : str="Barcode Generator" , options : dict= None):
        tk.Tk.__init__(self)
        with open("app/core.toml") as f:
            config = toml.load(f)
            print("Loading configuration...")
            title = config["app"]["name"]
            for key, value in config.items():
                if key == "options":
                    options = value
                    print(f"Options {options} loaded")
        self.title(title)
        self.geometry("350x200")
        self.minsize(350, 200)
        self.maxsize(350, 200)
        self.options = options
    
    def get_loaded_options(self):
        return self.options
    
    def create_barcode(self):
        print("Creating barcode...")
        barcode = self.barcode_entry.get()
        barcode_data = bf.generate_barcode([barcode])
        merged_barcodes = utils.merge_images(barcode_data)
        bf.generate_pdf(merged_barcodes)
    
    def build_widgets(self):
        self.ean_label = tk.Label(self, text="Enter the barcode number: ")
        self.barcode_entry = tk.Entry(self)
        self.create_button = tk.Button(self, text="Create", command=self.create_barcode)

        self.ean_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.barcode_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.create_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="se")

        # Configure grid columns and rows to expand and have minimum size
        self.grid_columnconfigure(0, weight=1, minsize=100)
        self.grid_columnconfigure(1, weight=1, minsize=100)
        self.grid_rowconfigure(0, weight=1, minsize=50)
        self.grid_rowconfigure(1, weight=1, minsize=50)

    def build_menu(self):       
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        importmenu = tk.Menu(filemenu, tearoff=0)
        importmenu.add_command(label="Fichier CSV", command= lambda: self.import_csv)
        menubar.add_cascade(label="Fichier", menu=filemenu)
        filemenu.add_cascade(label="Importer", menu=importmenu)
        menubar.add_command(label="Options", command= lambda: mf.open_option_windows(self, self.options))
        self.config(menu=menubar)
    
    def run(self):
        self.build_widgets()
        self.build_menu()
        self.mainloop()