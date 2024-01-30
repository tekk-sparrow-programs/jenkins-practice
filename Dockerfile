# Use the official Python image as the base image
FROM python:3.9

# Set the working directory
WORKDIR /helloworld

# Copy the requirements file into the container
COPY requirements.txt .

# Create a virtual environment and install dependencies
RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port your application will run on
EXPOSE 8080

# Set the command to run your application
CMD ["/bin/bash", "-c", "source venv/bin/activate && python helloworld.py"]
