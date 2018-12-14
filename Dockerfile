FROM python:3
WORKDIR /usr/src/app

COPY Python3HTTP_server.py ./
COPY WebServer.py ./
EXPOSE 9000
CMD python Python3HTTP_server.py 

