FROM ubuntu

RUN apt update && \
    apt upgrade

RUN apt install -y python3-dev python3-pip

RUN pip install -r requirements.txt

COPY src/ /src/
COPY resources/ /resources/

WORKDIR /src

CMD ["python3", "rest.py"]
