# convert pdf files into images for OCR processing
import os
import fitz as PyMu


def convert_pdf_2_image(pdf_path):
    # Open the PDF file
    pdf_document = PyMu.open(pdf_path)
    
    # Create a new directory in the same location as the PDF
    base_dir = os.path.dirname(pdf_path)
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_folder = os.path.join(base_dir, f"{pdf_name}_images")

    # Ensure the output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    # Define the zoom factor (scaling)
    zoom = 2  # Increase this value for higher quality images (e.g., 2 for 200% zoom)
    matrix = PyMu.Matrix(zoom, zoom)  # Create a transformation matrix for zooming

    # Loop through each page and save as an image
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)  # Load a page
        pix = page.get_pixmap(matrix=matrix)  # Render page to an image
        output_path = os.path.join(output_folder, f"page_{page_num + 1}.png")
        pix.save(output_path)  # Save the image
        print(f"Saved {output_path}")
    
    # return new subdirectory that contains the images
    return output_folder