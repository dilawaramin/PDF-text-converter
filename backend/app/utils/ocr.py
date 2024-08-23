import pytesseract as PT
from PIL import Image


def perform_ocr_on_image(image_path):
    """
    Perform OCR on the given image and print text with bounding box coordinates.

    :param image_path: The path to the image file.
    """
    # Open the image file
    image = Image.open(image_path)
    
    # Perform OCR to get text
    text = PT.image_to_string(image)
    print(f'Text from {image_path}:\n{text}')
    
    # Perform OCR to get bounding boxes
    boxes = PT.image_to_boxes(image)
    
    # Process and print bounding box coordinates and corresponding text
    for box in boxes.splitlines():
        box = box.split(' ')
        text_char = box[0]  # The recognized character or text element
        x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
        print(f"Text: '{text_char}', Coordinates: (x: {x}, y: {y}, w: {w}, h: {h})")

# Example usage:
# perform_ocr_on_image('path_to_image.png')