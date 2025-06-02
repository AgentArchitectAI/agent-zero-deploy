# Dockerfile
# Custom Agent Zero with CAD support

FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    openscad \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p logs memory tmp work_dir webui/cad

# Expose port 80 (como la imagen oficial)
EXPOSE 80

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV WEB_UI_PORT=80
ENV WEB_UI_HOST=0.0.0.0

# Run the application with explicit port and host
CMD ["python", "run_ui.py", "--port=80", "--host=0.0.0.0"] 