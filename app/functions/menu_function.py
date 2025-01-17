import tkinter as tk
import os
import sys
from classes import OptionWindow , MainWindow


def open_option_windows(parent : MainWindow.Application , options : dict = None):
    print("Opening option window...")
    OptionWindow.OptionWindow(parent)

   