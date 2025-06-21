from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from app.services.s3_service import upload_file_to_s3

image_bp = Blueprint('image_routes', __name__)

@image_bp.route('/upload', methods=['POST'])
def upload_image():
    """
    Upload an image to S3
    ---
    consumes:
      - multipart/form-data
    parameters:
      - name: image
        in: formData
        type: file
        required: true
        description: Image to upload
    responses:
      201:
        description: Image uploaded successfully
      400:
        description: No image provided
      500:
        description: Server error
    """
    if 'image' not in request.files:
        return jsonify({"success": False, "error": "No image file provided"}), 400

    file = request.files['image']
    filename = secure_filename(file.filename)

    result = upload_file_to_s3(file, filename)

    if result['success']:
        return jsonify({"success": True, "data": {"imageUrl": result['url']}}), 201
    else:
        return jsonify({"success": False, "error": result['error']}), 500
