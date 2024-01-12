FROM python:latest
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN apt update -y
RUN apt install build-essential libpoppler-cpp-dev pkg-config python3-dev -y
RUN pip install -r requirement.txt
CMD exec gunicorn operations:app  --bind 0.0.0.0:8080 
