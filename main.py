import os
import sys


sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))
import classes.MainWindow as MainWindow
from functions import barcode_function, utils




if __name__ == "__main__":
        app = MainWindow.Application()
        print("Starting application...")
        app.run()
        print("Application closed")



