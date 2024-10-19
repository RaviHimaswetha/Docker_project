# Use a slim version of Python as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY script.py .

# Create the directory for data files
RUN mkdir -p /home/data

# Copy the text files into the container
COPY home/data/IF.txt /home/data/
COPY home/data/AlwaysRememberUsThisWay.txt /home/data/

# Set the command to run the script
CMD ["python", "script.py"]
