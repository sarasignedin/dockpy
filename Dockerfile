# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the necessary files
COPY . .

# Install required packages
RUN pip install -r requirements.txt

# Command to run the script
CMD ["python", "compliance_processor.py"]
