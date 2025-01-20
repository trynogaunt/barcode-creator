from tkinter import filedialog
import classes.MainWindow as MainWindow
import classes.OptionWindow as OptionWindow
import csv
import re

def open_option_windows(parent : MainWindow.Application , options : dict = None):
    print("Opening option window...")
    OptionWindow.OptionWindow(parent)




   