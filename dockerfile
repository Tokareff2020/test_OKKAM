FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /fastApiProject
WORKDIR /fastApiProject
ADD . /fastApiProject/
RUN pip install --upgrade pip && pip install -r requirements.txt
