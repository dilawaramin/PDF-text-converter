# convert images and processed text back into pdf format
import os
import json
import fitz as pymu
from PIL import Image

def image_to_pdf(images_path):
    """
    Converts a series of PNG images from a specified directory into a single PDF file.

    This function iterates over all PNG images in the given directory, creates a new PDF document,
    and inserts each image into a new page within the PDF. The dimensions of each PDF page match 
    the dimensions of the corresponding image. The resulting PDF is saved in the same directory 
    as the images with the filename 'output.pdf'.

    Args:
        images_path (str): The file path to the directory containing the PNG images to be converted.

    Returns:
        None: The function saves the generated PDF in the specified directory as 'output.pdf'.
    """
    
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
            
            ### insert text
            # rename .png files with .json 
            json_filename = filename.replace('.png', '.json')
            
            # path to json files, with new naming
            json_file_path = os.path.join(images_path, "json_results", json_filename)        
            print("json file path: " + json_file_path)
            
            # insert the textboxes
            text_to_pdf(page, json_file_path)
            
            # for json_file in os.listdir(json_files_path):
            #     json_path = os.path.join(json_files_path, json_file)
            #     text_to_pdf(page, json_path)
            
 
    # save pdf
    output_path = os.path.join(images_path, 'output.pdf')
    pdf_doc.save(output_path)
    
    
    return


def text_to_pdf(pdf_page:pymu.Page, json_file):
    
    with open(json_file, 'r', encoding='utf-8') as json_data:
        data = json.load(json_data)
        
        # iterate through each paragraph on a page
        for paragraph in data["paragraphs"]:  
            
            # get the bounding box value from the paragaph dictionary
            bounding_box = paragraph["bounding_box"]
            
            # get the coordinates of the bounding box
            points = [
                bounding_box["x_min"],
                bounding_box["y_min"],
                bounding_box["x_max"],
                bounding_box["y_max"]
            ]
            
            # unpack points list and create rect object
            rect = pymu.Rect(*points)
            
            # get the actual text from paragraph
            text = paragraph["text"]
            
            # insert textbook into page
            pdf_page.insert_textbox(rect, text)
            
            
    return