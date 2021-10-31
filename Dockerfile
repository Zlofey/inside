# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /docker_dir
COPY requirements.txt /docker_dir/
RUN pip install -r requirements.txt
COPY . /docker_dir/
