import toml
import os
from fpdf import FPDF
from barcode import Code128
from barcode.writer import SVGWriter, ImageWriter
from PIL import Image

#region functions
# Generate barcode images
def generate_barcode(barcode_data: list) -> list:
    """Generate barcode images"""
    with open("app/core.toml") as f:
        config = toml.load(f)
    # Get configuration
        folder_path = config["barcode"]["folder_target"]
        image_format = config["barcode"]["image_format"]

    # Create barcode folder
        print(f"Creating barcode folder: barcodes") if os.makedirs(f"barcodes", exist_ok=True)\
        else print(f"Folder barcodes already exists")


    # Generate barcode
    for barcode in barcode_data:
        code = Code128(str(barcode), writer=ImageWriter(format=image_format.upper()))
        code.save(f"{folder_path}/barcode_{barcode}")
    return barcode_data


def generate_pdf(print_barcode: list) -> None:
    """Generate PDF with barcode images"""
    with open("app/core.toml") as f:
        config = toml.load(f)
    # Get configuration
        folder_path = config["pdf"]["folder_target"]
        pdf_format = config["pdf"]["page_size"]
        pdf_unit = config["pdf"]["unit"]
        pdf_name = config["pdf"]["file_name"]
        pdf_image_width = config["pdf"]["image_width"]
        pdf_image_height = config["pdf"]["image_height"]

    # Create PDF
    pdf = FPDF(unit= pdf_unit, format=pdf_format)
    pdf.add_page()
    
    x, y = 0, 0
    max_height = 0
    page_width = pdf.w - pdf.l_margin - pdf.r_margin
    page_height = pdf.h - pdf.t_margin - pdf.b_margin

    for img in print_barcode:
        print(img)
        image = Image.open(img)
        resized_image = image.resize((round(image.size[0]/7), round(image.size[1]/7)))
        width, height = resized_image.size

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

    pdf.output(folder_path)
#endregion

