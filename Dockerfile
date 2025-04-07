# Start from Ubuntu:22.04 as the base image
FROM ubuntu:22.04

# Set environment variables to avoid interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Update package lists and install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copying all files to docker
COPY . /app

# Set working directory inside the container
WORKDIR /app

# Install Python dependencies
RUN pip3 install --default-timeout=100 --no-cache-dir -r requirements.txt

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the Python application
CMD ["python3", "-m", "uvicorn", "API.api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]