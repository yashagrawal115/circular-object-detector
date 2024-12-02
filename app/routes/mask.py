from flask import Blueprint, jsonify, send_file
from routes.upload import metadata
import os
import cv2
import numpy as np

mask_bp = Blueprint("mask", __name__)
PROCESSED_FOLDER = "./processed"
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@mask_bp.route("/mask/<image_id>", methods=["GET"])
def get_mask(image_id):
    if image_id not in metadata:
        return jsonify({"error": "Image ID not found"}), 404

    # Generate the mask
    image_path = metadata[image_id]["image_path"]
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mask = np.zeros_like(gray)

    for obj in metadata[image_id]["objects"]:
        x, y, r = obj["centroid"][0], obj["centroid"][1], obj["radius"]
        cv2.circle(mask, (x, y), r, (255, 255, 255), -1)

    mask_path = os.path.join(PROCESSED_FOLDER, f"{image_id}_mask.png")
    cv2.imwrite(mask_path, mask)
    return send_file(mask_path, mimetype="image/png")
