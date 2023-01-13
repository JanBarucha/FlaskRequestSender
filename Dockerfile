FROM ubuntu:latest

RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 --version

RUN pip install requests
RUN pip install httpx
RUN pip install matplotlib
RUN pip install flask
RUN pip install app
RUN pip install pytest





WORKDIR /usr/app/src



VOLUME /data

RUN mkdir templates
COPY app.py ./
COPY templates/. ./templates
COPY test_app.py ./


CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]