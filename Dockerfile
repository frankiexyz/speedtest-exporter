FROM alpine:latest

RUN apk update && apk add python2 py-pip
COPY ./exporter.py /
COPY ./requirements.txt /
RUN pip install -r /requirements.txt
EXPOSE 8090
CMD ["python2", "/exporter.py"]
