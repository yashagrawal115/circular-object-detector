import cv2
import numpy as np

def process_image(image_path):
    """
    Processes the image to detect circular objects.
    Returns a list of objects with bounding box, centroid, and radius.
    """
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (9, 9), 2)

    circles = cv2.HoughCircles(
        blurred,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=30,
        param1=50,
        param2=30,
        minRadius=10,
        maxRadius=50
    )

    objects = []
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for i, (x, y, r) in enumerate(circles):
            objects.append({
                "id": f"{image_path}_{i}",
                "bounding_box": [x - r, y - r, x + r, y + r],
                "centroid": [x, y],
                "radius": r
            })

    return objects
