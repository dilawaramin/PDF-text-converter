from utils import image_processing as imgProc
from utils import ocr
import config

# convert pdf file from a directory into images
images1 = imgProc.convert_pdf_2_image(config.DEFAULT_PDF_2)

# perform OCR on the images
ocr.perform_ocr_on_directory(images1)