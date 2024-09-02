from utils import pdf_processing as pdfProc
from utils import image_processing as imgProc
from utils import ocr
import config

# file to test with
PDF = config.DEFAULT_IMAGE_1

# convert pdf file from a directory into images
images1 = imgProc.convert_pdf_2_image(PDF)

# perform OCR on the images
ocr.perform_ocr_on_directory(images1)

# create new pdf
pdfProc.image_to_pdf(images1)