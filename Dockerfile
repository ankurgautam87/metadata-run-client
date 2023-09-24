
FROM --platform=linux/amd64 python:3.8-slim-buster as build
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT [ "python3" ]
CMD [ "metadataclient.py" ]