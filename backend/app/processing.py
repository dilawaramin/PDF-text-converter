import utils.image_processing as img_proc
import utils.ocr as ocr
import utils.pdf_processing as pdf_proc

def process_file(file_route):
    
    # convert file to OCR-able images
    file_images = img_proc.convert_pdf_2_image(file_route)
    
    # perform OCR operations
    ocr.perform_ocr_on_directory(file_images)
    
    # create a new OCR'd pdf
    processed_file_path = pdf_proc.image_to_pdf(file_images)
    
    return processed_file_path