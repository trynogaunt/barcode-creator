from PIL import Image, ImageDraw, ImageFont
import os
import csv
from tkinter import filedialog
import toml
from functions import barcode_function
import re

def calculate_size(barcode) -> int:
    '''Calculate the size of the image to be created'''
    width = 0
    height = 0
    for i in range(len(str(barcode))):
        width += 45
        height += 5
    return width, height

def merge_images(img_path : list) -> list:
    '''Merge list of images'''
    merged_img = []
    with open("app/core.toml") as f:
        config = toml.load(f)
        color_mode = config["image"]["color_mode"]
        format = config["image"]["image_format"]
        color = config["image"]["color"]
        height = config["image"]["height"]
        register_folder = config["image"]["register_folder"]
        barcodes_folder = config["barcode"]["folder_target"]
    

    
    for index, img in enumerate(img_path):
        image = Image.open(f"{barcodes_folder}/barcode_{img}.{format}")
        arrow_image = Image.open("app/ressources/arrow_up.jpeg")
        final_img = Image.new(mode=color_mode, size=[image.size[0] + arrow_image.size[0], image.size[1]], color=tuple(color))
        final_img.paste(image, (0, 0))
        final_img.paste(arrow_image, (image.size[0], 0))
        final_img.save(f"{register_folder}/{img}.jpeg")
        merged_img.append(f"{register_folder}/{img}.jpeg")
        print(merged_img[index])
    return merged_img

def create_barcode_from_csv():
    print("Creating barcode from CSV...")
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    print(f"Selected file: {file_path}")
    csv_data = csv.reader(open(file_path))
    cleaned_list = []
    for row in csv_data:
        row = re.sub(r"[^0-9]+", '', str(row))
        cleaned_list.append(row)

    barcode_data = barcode_function.generate_barcode(cleaned_list)
    merged_img = merge_images(barcode_data)
    barcode_function.generate_pdf(merged_img)
    print("Barcode created from CSV")    