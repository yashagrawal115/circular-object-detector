from flask import Blueprint, jsonify
from routes.upload import metadata

objects_bp = Blueprint("objects", __name__)

@objects_bp.route("/objects/<image_id>", methods=["GET"])
def list_objects(image_id):
    if image_id not in metadata:
        return jsonify({"error": "Image ID not found"}), 404

    return jsonify(metadata[image_id]["objects"])

@objects_bp.route("/objects/<image_id>/<object_id>", methods=["GET"])
def object_details(image_id, object_id):
    if image_id not in metadata:
        return jsonify({"error": "Image ID not found"}), 404

    obj = next((obj for obj in metadata[image_id]["objects"] if obj["id"] == object_id), None)
    if not obj:
        return jsonify({"error": "Object ID not found"}), 404

    return jsonify(obj)
