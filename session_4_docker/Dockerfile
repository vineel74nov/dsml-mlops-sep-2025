#python:3.10-slim debian variant of linux

# Using slim version to keep the image size small
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /flask-loan-app

# Copy the requirements file into the container at /flask-loan-app
COPY artefacts/requirements.txt /flask-loan-app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /flask-loan-app
COPY . /flask-loan-app

# Make port 8000 available to the world outside this container
CMD ["python", "-m", "flask", "--app", "hello.py", "run", "--host=0.0.0.0", "--port=8000"]