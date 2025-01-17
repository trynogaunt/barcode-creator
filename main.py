import os
import sys
import tkinter as tk
import toml

sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

import functions.barcode_function as bf
import functions.utils as utils
import functions.menu_function as mf
from classes.MainWindow import Application



if __name__ == "__main__":
    with open("app/core.toml") as f:
        config = toml.load(f)
        print("Loading configuration...")
        title = config["app"]["name"]
        for key, value in config.items():
            if key == "options":
                options = value
                print("Options loaded")
    app = Application(title=title, options=options)
    print("Starting application...")
    app.mainloop()
    print("Application closed")



