# Base image
FROM python:3.9

# Update package list and install GDAL dependencies
RUN apt-get update && \
    apt-get install -y binutils libproj-dev gdal-bin

WORKDIR /shops_near_me

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy app files to container
COPY . .

# Set command to run app
CMD ["python", "manage.py", "runserver", "0.0.0.0:9812"]