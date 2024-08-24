# convert images and processed text back into pdf format
import os
import fitz as pymu
from PIL import Image

def image_to_pdf(images_path):
    
    # # TEMPORARY: hardcode page path
    # image_path = images_path + '/page_1.png'
    
    # create a new pdf
    pdf_doc = pymu.Document()
    
    # loop through all the .png images to convert 
    for filename in os.listdir(images_path):
        if filename.endswith('.png'):
            
            # get dimensions of image
            image_path = os.path.join(images_path, filename)
            with Image.open(image_path) as img:
                w, h = img.size
                
            # create new pdf page with image's dimensions
            page = pdf_doc.new_page(width=w, height=h)
            
            # create rectangle the same size as page, insert image
            img_rect = pymu.Rect(0, 0, w, h)
            page.insert_image(rect=img_rect, filename=image_path)
            
 
    # save pdf
    output_path = os.path.join(images_path, 'output.pdf')
    pdf_doc.save(output_path)
    
    
    return


