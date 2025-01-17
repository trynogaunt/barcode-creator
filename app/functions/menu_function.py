import tkinter as tk
import os
import sys
from classes import OptionWindow , MainWindow


def open_option_windows(parent : MainWindow.Application):
    OptionWindow.OptionWindow(parent)
    print("Options")   