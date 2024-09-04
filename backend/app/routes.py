import os
from flask import Flask, Blueprint, request, jsonify, send_file, Response, after_this_request
from werkzeug.utils import secure_filename
import processing
import uuid
import threading



# Define a Blueprint for the routes
routes = Blueprint('routes', __name__)



# Initialize "uploads" folder
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'backend', 'app', 'uploads')
# create if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
    
# allowed file types for processing
ALLOWED_EXTENSIONS = [".pdf", ".jpg", ".jpeg", ".png"]



# upload file for processing route
@routes.route('/upload_file', methods=['POST'])
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
    
    # create unique filename to avoid collisions
    unique_filename = f"{uuid.uuid4()}_{filename}"
    
    # make sure file type is allowed
    if os.path.splitext(filename)[1] not in ALLOWED_EXTENSIONS:
        return jsonify({"Error": "Invalid file type"}), 400
    
    # create a directory with filename 
    file_directory = os.path.join(UPLOAD_FOLDER, os.path.splitext(filename)[0])
    
    # Ensure the directory exists
    if not os.path.exists(file_directory):
        os.makedirs(file_directory)
        print("Directory created successfully!")

    # Save the file in the newly created directory    
    temp_file_path = os.path.join(UPLOAD_FOLDER, unique_filename)
    file.save(temp_file_path)
    
    
    try:
        # perform OCR operations on file
        processed_filepath = processing.process_file(temp_file_path)
        
        # Read the file into memory
        with open(processed_filepath, 'rb') as f:
            file_data = f.read()

        # Delete the processed file from disk
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
            print(f"Removed temp file: {temp_file_path}")
        if os.path.exists(processed_filepath):
            os.remove(processed_filepath)
            print(f"Removed processed file: {processed_filepath}")

        # Create and return a Response with the file data
        return Response(file_data, headers={
            'Content-Type': 'application/pdf',
            'Content-Disposition': f'attachment; filename={unique_filename};'
        })
    

    
    except Exception as e:
        # catch errors
        return jsonify({"error": str(e)}), 500

