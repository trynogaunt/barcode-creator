import shutil

import text_to_image
import random
from PIL import Image, ImageDraw, ImageFont
import os
import img2pdf
from fpdf import FPDF

def main() -> None:
    '''Main app entry point.'''
    barcodes_list = []
    folder_path = 'barcodes'
    print_barcode = []
    width , height = 0 , 0

    os.makedirs(folder_path, exist_ok=True)

    for i in range(10):
        random_number = random.randint(1000000000000, 9999999999999)
        barcodes_list.append(random_number)
    
    pdf = FPDF(unit='pt', format='A4')
    pdf.add_page()
    x, y = 0, 0
    max_height = 0
    page_width = pdf.w - pdf.l_margin - pdf.r_margin
    page_height = pdf.h - pdf.t_margin - pdf.b_margin

    for img in print_barcode:
        print(img)
        image = Image.open(img)
        width, height = image.size

        # Scale image if it is too wide
        if width > page_width:
            scale = page_width / width
            width = page_width
            height = height * scale

        # Move to next row if image doesn't fit horizontally
        if x + width > page_width:
            x = 0
            y += max_height
            max_height = 0

        # Move to next page if image doesn't fit vertically
        if y + height > page_height:
            pdf.add_page()
            x, y = 0, 0
            max_height = 0

        pdf.image(img, x, y, width, height)
        x += width
        if height > max_height:
            max_height = height

    pdf.output("barcodes.pdf")

if __name__ == '__main__':
    main()