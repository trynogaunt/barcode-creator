import os
import sys
import tkinter as tk

sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

import functions.barcode_function as bf
import functions.utils as utils
import functions.menu_function as mf
from classes.MainWindow import Application



if __name__ == "__main__":
    app = Application()
    print("Starting application...")
    app.mainloop()
    print("Application closed")



