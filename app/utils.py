from PIL import Image, ImageDraw, ImageFont
import os
import toml

def calculate_size(barcode) -> int:
    '''Calculate the size of the image to be created'''
    width = 0
    height = 0
    for i in range(len(str(barcode))):
        width += 45
        height += 5
    return width, height

def merge_images(img_path : list) -> None:
    '''Merge list of images'''
    final_img_size = 0
    with open("app/core.toml") as f:
        config = toml.load(f)
        color_mode = config["image"]["color_mode"]
        format = config["image"]["image_format"]
        color = config["image"]["color"]
        height = config["image"]["height"]
    

    
    for index, img in enumerate(img_path):
        image = Image.open(img)
        arrow_image = Image.open("app/ressources/arrow_up.jpeg")
        final_img = Image.new(mode=color_mode, size=final_img_size, color=color)
        final_img.paste(image, (previous_size, 0))
        previous_size += image.size[0]
        final_img.save(f"final_image.jpeg")