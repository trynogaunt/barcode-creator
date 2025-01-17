import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Barcode Generator")
        self.geometry("350x200")
        self.minsize(350, 200)
        self.maxsize(350, 200)
        self.build_widgets()
    
    def build_widgets(self):
        self.ean_label = tk.Label(self, text="Enter the barcode number: ")
        self.barcode_entry = tk.Entry(self)
        self.create_button = tk.Button(self, text="Create")
        self.import_csv_button = tk.Button(self, text="Import CSV")

        self.ean_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.barcode_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky="ew")
        self.import_csv_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        self.create_button.grid(row=2, column=2, padx=10, pady=10, sticky="se")

        # Configure grid columns and rows to expand and have minimum size
        self.grid_columnconfigure(0, weight=1, minsize=100)
        self.grid_columnconfigure(1, weight=1, minsize=50)
        self.grid_columnconfigure(2, weight=1, minsize=100)
        self.grid_rowconfigure(0, weight=1, minsize=100)
        self.grid_rowconfigure(1, weight=1, minsize=50)
        self.grid_rowconfigure(2, weight=1, minsize=100)

if __name__ == "__main__":
    app = Application()
    app.mainloop()


