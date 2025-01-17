import toml
import os
from barcode import Code128
from barcode.writer import SVGWriter, ImageWriter

#region functions
# Generate barcode images
def generate_barcode(barcode_data: list) -> list:
    """Generate barcode images"""
    with open("core.toml") as f:
        config = toml.load(f)
    # Get configuration
        folder_path = config["barcode"]["folder_target"]
        image_format = config["barcode"]["image_format"]

    # Create barcode folder
        print(f"Creating barcode folder: {barcode}") if os.makedirs(f"{folder_path}/{barcode}", exist_ok=True)\
        else print(f"Folder {barcode} already exists")


    # Generate barcode
    for barcode in barcode_data:
        code = Code128(str(barcode), writer=ImageWriter(format=image_format.upper()))
        code.save(f"{folder_path}/{barcode}/barcode_{barcode}")
    return barcode_data


def generate_pdf(print_barcode: list) -> None:
    """Generate PDF with barcode images"""
    # Generate PDF
    pass
#endregion