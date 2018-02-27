# Python Base Image from https://hub.docker.com/r/arm32v7/python/
FROM arm32v7/python:2.7.13-jessie

# Set the working directory to /inventory-count
WORKDIR /inventory-count

# Copy the current directory contents into the container at /app
ADD . /inventory-count

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME Inventory

# Run app.py when the container launches
CMD ["python", "invServer.py"]

LABEL vendor=AMMK\ Incorporated \
    com.ammk.is-beta= \
    com.ammk.is-production="" \
    com.ammk.version="0.0.1-beta" \
    com.ammk.release-date="2018-02-26"
