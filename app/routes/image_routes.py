from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from app.services.s3_service import upload_file_to_s3 
image_bp = Blueprint('image_routes', __name__)

@image_bp.route('/upload', methods=['POST'])
def upload_images():
    files = request.files.getlist('images')

    if not files or files == []:
        return jsonify({"success": False, "error": "No image files provided"}), 400

    uploaded_urls = []
    for file in files:
        filename = secure_filename(file.filename)
        result = upload_file_to_s3(file, filename)

        if result['success']:
            uploaded_urls.append(result['url'])
        else:
            return jsonify({"success": False, "error": result['error']}), 500

    return jsonify({"success": True, "data": {"imageUrls": uploaded_urls}}), 201
