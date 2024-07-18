# Python3 program to convert image to pdf
# using img2pdf library

# importing necessary libraries
import img2pdf
from PIL import Image
import os

# taking input for image path
img_path = input(r"Enter Image Path: ").strip().strip('"')

# taking input for pdf path
pdf_path = input(r"Enter PDF Save Path (including filename, e.g., C:\path\to\file.pdf): ").strip().strip('"')

# converting paths to absolute paths and normalizing them
img_path = os.path.abspath(img_path)
pdf_path = os.path.abspath(pdf_path)

# opening image
image = Image.open(img_path)

# converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.filename)

# opening or creating pdf file
with open(pdf_path, "wb") as file:
    # writing pdf files with chunks
    file.write(pdf_bytes)

# closing image file
image.close()

# output
print("Successfully made pdf file")
