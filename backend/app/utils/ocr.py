import os
import json
import pytesseract as PT
from PIL import Image


########## paragraph/textbox version of function ##########

# def perform_ocr_on_directory(directory_path):
#     """
#     Perform OCR on all images in the given directory, save each image's text and bounding boxes to a JSON file.

#     :param directory_path: The path to the directory containing image files.
#     """
#     # Create a subdirectory for json files
#     json_output_dir = os.path.join(directory_path, 'json_results')
#     if not os.path.exists(json_output_dir):
#         os.makedirs(json_output_dir)
    
#     # Loop through all files in the directory
#     for filename in os.listdir(directory_path):
#         # Construct full file path
#         image_path = os.path.join(directory_path, filename)
        
#         # Check if it's a file and not a subdirectory
#         if os.path.isfile(image_path):
            
#             # Open the image file
#             image = Image.open(image_path)
            
#             # Perform OCR to get text and bounding boxes
#             data = PT.image_to_data(image, output_type=PT.Output.DICT)
            
#             # Prepare a list to hold paragraph data
#             paragraphs_data = []
#             current_paragraph = ""
#             current_bbox = [float('inf'), float('inf'), 0, 0]  # [x_min, y_min, x_max, y_max]
#             paragraph_number = 1  # Initialize the paragraph number
            
#             n_boxes = len(data['level'])
#             for i in range(n_boxes):
#                 # Continue collecting words within the same paragraph level
#                 if data['block_num'][i] == data['block_num'][i - 1] if i > 0 else True:
#                     current_paragraph += " " + data['text'][i]
#                     x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
#                     current_bbox[0] = min(current_bbox[0], x)
#                     current_bbox[1] = min(current_bbox[1], y)
#                     current_bbox[2] = max(current_bbox[2], x + w)
#                     current_bbox[3] = max(current_bbox[3], y + h)
#                 else:
#                     # Save the completed paragraph and its bounding box
#                     if current_paragraph.strip():
#                         paragraph_data = {
#                             "paragraph_number": paragraph_number,
#                             "text": current_paragraph.strip(),
#                             "bounding_box": {
#                                 "x_min": current_bbox[0],
#                                 "y_min": current_bbox[1],
#                                 "x_max": current_bbox[2],
#                                 "y_max": current_bbox[3]
#                             }
#                         }
#                         paragraphs_data.append(paragraph_data)
#                         paragraph_number += 1  # Increment the paragraph number
#                     current_paragraph = data['text'][i]
#                     current_bbox = [data['left'][i], data['top'][i], data['left'][i] + data['width'][i], data['top'][i] + data['height'][i]]
            
#             # Save the last paragraph if any
#             if current_paragraph.strip():
#                 paragraph_data = {
#                     "paragraph_number": paragraph_number,
#                     "text": current_paragraph.strip(),
#                     "bounding_box": {
#                         "x_min": current_bbox[0],
#                         "y_min": current_bbox[1],
#                         "x_max": current_bbox[2],
#                         "y_max": current_bbox[3]
#                     }
#                 }
#                 paragraphs_data.append(paragraph_data)
            
#             # Create the JSON object
#             json_data = {
#                 "filename": filename,
#                 "paragraphs": paragraphs_data
#             }
            
#             # Define the output JSON file name
#             output_filename = f"{os.path.splitext(filename)[0]}.json"
#             output_json_file = os.path.join(json_output_dir, output_filename)
            
#             # Write the JSON data to a file
#             with open(output_json_file, 'w', encoding='utf-8') as json_file:
#                 json.dump(json_data, json_file, indent=4)
            
#             print(f'OCR results for {filename} saved to {output_json_file}')
    
#     print()
#     return




########## character version of function ##########

def perform_ocr_on_directory(directory_path):
    """
    Perform OCR on all images in the given directory, save each character's text and bounding boxes to a JSON file.

    :param directory_path: The path to the directory containing image files.
    """
    # Create a subdirectory for json files
    json_output_dir = os.path.join(directory_path, 'json_results')
    if not os.path.exists(json_output_dir):
        os.makedirs(json_output_dir)
    
    # Loop through all files in the directory
    for filename in os.listdir(directory_path):
        # Construct full file path
        image_path = os.path.join(directory_path, filename)
        
        # Check if it's a file and not a subdirectory
        if os.path.isfile(image_path):
            
            # Open the image file
            image = Image.open(image_path)
            
            # Perform OCR to get text and bounding boxes
            data = PT.image_to_data(image, output_type=PT.Output.DICT)
            
            # Prepare a list to hold character data
            characters_data = []
            
            n_boxes = len(data['level'])
            for i in range(n_boxes):
                # Gather character-level data
                if data['text'][i].strip():  # Ensure the text is not empty
                    char_data = {
                        "char": data['text'][i],
                        "bounding_box": {
                            "x_min": data['left'][i],
                            "y_min": data['top'][i],
                            "x_max": data['left'][i] + data['width'][i],
                            "y_max": data['top'][i] + data['height'][i]
                        }
                    }
                    characters_data.append(char_data)
            
            # Create the JSON object
            json_data = {
                "filename": filename,
                "characters": characters_data
            }
            
            # Define the output JSON file name
            output_filename = f"{os.path.splitext(filename)[0]}.json"
            output_json_file = os.path.join(json_output_dir, output_filename)
            # Write the JSON data to a file
            with open(output_json_file, 'w', encoding='utf-8') as json_file:
                json.dump(json_data, json_file, indent=4)
            
            print(f'OCR results for {filename} saved to {output_json_file}')
    
    print()
    return