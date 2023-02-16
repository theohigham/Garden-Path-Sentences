# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable for the spaCy model path
ENV SPACY_MODEL_PATH=/usr/local/lib/python3.9/site-packages/en_core_web_sm/en_core_web_sm-3.2.0

# Run garden.py when the container launches
CMD ["python", "garden.py"]
