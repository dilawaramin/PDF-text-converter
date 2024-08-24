# convert images and processed text back into pdf format
import os
import fitz as pymu
from PIL import Image

def image_to_pdf(images_path):
    
    # TEMPORARY: hardcode page path
    image_path = images_path + '/page_1.png'
    
    # create a new pdf
    pdf_doc = pymu.Document()
    
    # get size of the image
    with Image.open(image_path) as img:
        w, h = img.size
    
    # create a new pdf page, with images dimensions
    page = pdf_doc.new_page(width=w, height=h)
    
    # create rectangle across page, insert image
    img_rect = pymu.Rect(0, 0, w, h)
    page.insert_image(rect=img_rect, filename=image_path)
    print("Page created, image inserted")
    
    # save pdf
    output_path = os.path.join(images_path, 'output.pdf')
    pdf_doc.save(output_path)
    
    
    return


