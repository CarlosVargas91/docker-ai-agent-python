# declare whay image to use
FROM python:latest

# EXPOSE 8000

WORKDIR /app

# linux command to create a file
#RUN echo "Hello World" > index.html

# RUN mkdir -p /static_folder

# COPY local_folder to container_folder
# COPY ./static_html /static_folder

# Same destination folder
COPY ./src .


# python -m http.server 8000
# docker python is running on port 8000, so we need to map the port 8000 to the port 8000 of the host.
CMD ["python", "-m", "http.server", "8000"]
