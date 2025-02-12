# # Use an official base image
# FROM ubuntu:latest

# # Set the working directory
# WORKDIR /app

# # Copy the current directory contents into the container
# COPY . /app

# # Install any necessary dependencies (example: Python3)
# RUN apt-get update && apt-get install -y python3-pip python3-venv git nodejs npm

# # Define environment variables (if needed)
# # ENV MY_VAR=my_value

# # Expose a specific port (example: port 80)
# EXPOSE 8000

# # Create virtual environment and activate it
# ENV VIRTUAL_ENV=/opt/venv
# RUN python3 -m venv $VIRTUAL_ENV
# ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# # Install FastAPI and Uvicorn using pip
# RUN pip3 install fastapi uvicorn uv httpx python-dateutil requests numpy

# RUN git config --global user.name "TDS Tool" \
#     && git config --global user.email "tds.tool@xyz.com"

# # Run a command when the container starts (example: bash shell)
# CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]



# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install necessary dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends git nodejs npm && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create virtual environment and activate it
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install FastAPI, Uvicorn, and other Python dependencies using pip
RUN pip install --no-cache-dir fastapi uvicorn uv httpx python-dateutil requests numpy

# Configure Git
RUN git config --global user.name "TDS Tool" \
    && git config --global user.email "tds.tool@xyz.com"

# Expose the application port
EXPOSE 8000

# Run the application using Uvicorn
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
