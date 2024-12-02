from flask import Blueprint, request, jsonify
import os
import uuid
from utils import process_image

upload_bp = Blueprint("upload", __name__)
UPLOAD_FOLDER = "./uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# In-memory metadata storage
metadata = {}

@upload_bp.route("/upload", methods=["POST"])
def upload_image():
    file = request.files.get("image")
    if not file:
        return jsonify({"error": "No image provided"}), 400

    # Save the image with a unique identifier
    image_id = str(uuid.uuid4())
    image_path = os.path.join(UPLOAD_FOLDER, f"{image_id}.png")
    file.save(image_path)

    # Process the image to detect circular objects
    objects = process_image(image_path)

    # Save metadata
    metadata[image_id] = {
        "image_path": image_path,
        "objects": objects
    }

    return jsonify({"image_id": image_id, "objects": objects})
