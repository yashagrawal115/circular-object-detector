## Circular Object Detector
This Python-based API detects circular objects in uploaded images.

Features:

- Detects circles using the Hough Circle Transform.
- Generates metadata for detected objects (bounding boxes, centroids, radii).
- Provides a binary mask highlighting detected circles.
- Modular and scalable design with Docker support.
- 
### Installation
  #### Prerequisites:

       - Python 3.9+
       - Docker (optional, for containerized deployment)
  #### Steps:

      1. Clone the repository:
          Bash
          
          git clone https://your-username/circular-object-detector.git
          
          cd circular-object-detector
          
      2. Install dependencies:
          Bash
          
          pip install -r requirements.txt

      3. Run the Flask app:
          Bash
          python main.py
      
      4. Access the app at http://localhost:5000.

### API Endpoints
  #### 1. Upload Image

URL: /upload

Method: POST

Description: Uploads an image for processing and detects circular objects.

Request:

curl -X POST -F "image=@path/to/image.png" http://localhost:5000/upload

Response (JSON):


JSON
----
{

  "image_id": "unique-image-id",
  
  "objects": [
  
    {
    
      "id": "unique-object-id",
      
      "bounding_box": [x1, y1, x2, y2],
      
      "centroid": [cx, cy],
      
      "radius": r
      
    }
    
  ]
  
}


  #### 2. List Circular Objects

URL: /objects/<image_id>
Method: GET
Description: Returns a list of detected circular objects for a given image.
Request:
curl -X GET http://localhost:5000/objects/<image_id>
Response (JSON):
JSON
[
  {
    "id": "unique-object-id",
    "bounding_box": [x1, y1, x2, y2],
    "centroid": [cx, cy],
    "radius": r
  }
]
Use code with caution.

3. Get Circular Object Details

URL: /objects/<image_id>/<object_id>
Method: GET
Description: Retrieves details of a specific circular object.
Request:
curl -X GET http://localhost:5000/objects/<image_id>/<object_id>
Response (JSON):
JSON
{
  "id": "unique-object-id",
  "bounding_box": [x1, y1, x2, y2],
  "centroid": [cx, cy],
  "radius": r
}
Use code with caution.

  #### 4. Get Binary Mask

      URL: /mask/<image_id>
      
      Method: GET
      
      Description: Retrieves the binary mask of detected circular objects.
      
      Request:
      
      curl -X GET http://localhost:5000/mask/<image_id> --output mask.png
      
      Usage
      
      Running Locally:

Start the Flask app:
Bash
python main.py

Use the API endpoints described above.
Running with Docker:

Build the Docker image:
Bash
docker build -t circular-object-detector .

Run the container:
Bash
docker run -p 5000:5000 circular-object-detector

Access the app at http://localhost:5000.
Testing
You can install pytest and run unit tests:

Bash
pip install pytest
pytest tests/

### Project Structure
circular-object-detector/
├── app/
│   ├── main.py        # Entry point for Flask app
│   ├── utils.py        # Image processing utilities
│   └── routes/         # API endpoints
│       ├── upload.py
│       ├── objects.py
│       └── mask.py
│            
├── uploads/          # Persistent image uploads 
├── processed/        # Processed masks 
├── Dockerfile        # Docker configuration
├── requirements.txt  # Python dependencies
├── README.md         # Project documentation
└── tests/            # Unit tests
