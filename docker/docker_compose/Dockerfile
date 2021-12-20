#Run with: docker build -t mything:1.0 .
# Base image is the splunk/splunk image
FROM splunk/splunk 

# Next set env variables, we did the same in the docker compose also
# Probably better to do this in docker compose
ENV SPLUNK_START_ARGS=--accept-license \
    SPLUNK_PASSWORD=password

#Run a linux command in the container
# You can have many RUN commands
RUN mkdir -p /tmp/newfolder

# Copy from server to container
COPY . /tmp/newfolder

# You have 1 CMD, it runs the server, once it's done the container goes down
CMD [ "start-service"]