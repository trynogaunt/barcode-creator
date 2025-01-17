import shutil
from barcode import Code128
from barcode.writer import SVGWriter, ImageWriter
import text_to_image
import random
from PIL import Image, ImageDraw, ImageFont
import os
import img2pdf
from fpdf import FPDF

def calculate_size(barcode) -> int:
    '''Calculate the size of the image to be created'''
    width = 0
    height = 0
    for i in range(len(str(barcode))):
        width += 45
        height += 5
    return width, height

def generate_barcode(v_barcode_number_list: list):

    pass

def main() -> None:
    '''Main app entry point.'''
    barcodes_list = []
    folder_path = 'barcodes'
    background = (240, 159, 31)
    colorText = (0, 0, 0)
    font = ImageFont.truetype("arial.ttf", 75)
    print_barcode = []
    width , height = 0 , 0

    os.makedirs(folder_path, exist_ok=True)

    for i in range(10):
        random_number = random.randint(1000000000000, 9999999999999)
        barcodes_list.append(random_number)
    
    for barcode in barcodes_list:
        os.makedirs(f"{folder_path}/{barcode}", exist_ok=True)
        print(f"Creating barcode folder: {barcode}")

        code = Code128(str(barcode), writer=ImageWriter(format="JPEG"))
        code.save(f"{folder_path}/{barcode}/barcode_{barcode}")
        print(f"Creating barcode: {barcode}")

        width, height =  calculate_size(barcode)[0], 280
        img = Image.new('RGB', (width, height), color = background)
        d = ImageDraw.Draw(img)
        d.text((10,10), str(barcode), fill=colorText, font=font)
        img.save(f"{folder_path}/{barcode}/number_{barcode}.jpeg")
        print(f"Creating barcode number: {barcode}")

        img_barcode = Image.open(f"{folder_path}/{barcode}/barcode_{barcode}.jpeg")
        img_arrow = Image.open("ressources/arrow_up.jpeg")
        final_img = Image.new('RGB', (img_barcode.size[0] + img_arrow.size[0], height), color=(255, 255, 255))

        final_img.paste(img_barcode, (0, 0))
        final_img.paste(img_arrow, (img_barcode.size[0], 0))
        final_img.save(f"{folder_path}/{barcode}/final_{barcode}.jpeg")

        print_barcode.append(f"{folder_path}/{barcode}/final_{barcode}.jpeg")

    print(print_barcode)
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