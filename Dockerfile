# Base image
FROM python:3.9

# Update package list and install GDAL dependencies
RUN apt-get update && \
    apt-get install -y binutils libproj-dev gdal-bin