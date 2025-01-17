from asyncio import sleep
import os
import sys
import tkinter as tk

sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

import barcode_function as bf
import utils

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Barcode Generator")
        self.geometry("350x200")
        self.minsize(350, 200)
        self.maxsize(350, 200)
        self.build_menu()
        self.build_widgets()
    
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
        menubar.add_command(label="Options", command="")
        self.config(menu=menubar)

if __name__ == "__main__":
    app = Application()
    app.mainloop()



