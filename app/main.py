from flask import Flask
from routes.upload import upload_bp
from routes.objects import objects_bp
from routes.mask import mask_bp

app = Flask(__name__)

# Register blueprints for modular routing
app.register_blueprint(upload_bp)
app.register_blueprint(objects_bp)
app.register_blueprint(mask_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
