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
    with open("core.toml") as f:
        config = toml.load(f)
        color_mode = config["image"]["color_mode"]
        color = config["image"]["color"]
        height = config["image"]["height"]
    
    for img in img_path:
        image = Image.open(img)
        final_img_size += image.size
    
    
    final_img = Image.new(color_mode, final_img_size)
    previous_size = 0
    for index, img in enumerate(img_path):
        image = Image.open(img)
        final_img.paste(image, (previous_size, 0))
        previous_size += image.size[0]

    final_img.save("final_image.jpeg")