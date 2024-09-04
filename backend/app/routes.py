import os
from flask import Flask, Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import utils.pdf_processing as process_pdf

# Define a Blueprint for the routes
routes = Blueprint('routes', __name__)

UPLOAD_FOLDER = "uploads/"
ALLOWED_EXTENSIONS = [".pdf", ".jpg", ".jpeg", ".png"]


# upload file for processing route
@routes.route('/upload_pdf', methods=['POST'])
def upload_pdf():
    
    # ensure there is a file in request
    if 'file' not in request.files:
        return jsonify({"error": "No file"}), 400

    file = request.files['file']

    # If the user does not select a file
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400     
    
    # Secure the filename
    filename = secure_filename(file.filename)   
    
    # make sure file type is allowed
    if os.path.splitext(filename)[1] not in ALLOWED_EXTENSIONS:
        return jsonify({"Error": "Invalid file type"}), 400
    
    # create a directory with filename 
    file_directory = os.path.join(UPLOAD_FOLDER, os.path.splitext(filename)[0])

    # Ensure the directory exists
    if not os.path.exists(file_directory):
        os.makedirs(file_directory)

    # Save the file in the newly created directory
    file_path = os.path.join(file_directory, filename)
    file.save(file_path)

    return