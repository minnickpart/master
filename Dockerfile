# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN apt -y update
RUN apt install -y libsodium-dev curl sudo wget
# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV PYTHONUNBUFFERED=1
# RUN tmate
# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
