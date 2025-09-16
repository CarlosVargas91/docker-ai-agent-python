# declare whay image to use
FROM python:latest

# Create python virtual environment
# isolate python from system level
RUN python -m venv /opt/venv/

# Everything after works here
ENV PATH=/opt/venv/bin:$PATH

WORKDIR /app

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY ./src .

CMD ["python", "-m", "http.server", "8000"]
