FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y libopencv-dev python3-opencv

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "main.py"]
