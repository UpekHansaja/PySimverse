# Use Python 3.13
FROM python:3.13.0-slim
FROM --platform=linux/arm64 python:3.13-slim

# Install system dependencies (VERY IMPORTANT for video decoding)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6 \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

# Copy your project files
COPY . .

# Run your script
CMD ["python", "drone_video_stream.py"]