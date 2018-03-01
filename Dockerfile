# Python Base Image from https://hub.docker.com/r/arm32v7/python/
FROM debian:jessie

# Set the working directory to /inventory-count
WORKDIR /server

# Copy the current directory contents into the container at /server
ADD . /server

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME Inventory

# Run app.py when the container launches
CMD ["python", "tabledef.py"]

LABEL vendor=AMMK\ Incorporated \
    com.ammk.is-beta= \
    com.ammk.is-production="" \
    com.ammk.version="0.0.2-beta" \
    com.ammk.release-date="2018-03-01"
