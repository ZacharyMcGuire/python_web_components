# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Copy the entrypoint script into the container
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# Set the entrypoint script to run when the container starts
ENTRYPOINT ["./entrypoint.sh"]
