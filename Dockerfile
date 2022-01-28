FROM ubuntu

RUN apt update && \
    apt upgrade

RUN apt install -y python3-dev python3-pip

RUN pip install -r requirements.txt

RUN python -m nltk.downloader popular -d ../resources/data/nltk_data

COPY form10/ /form10/
COPY resources/ /resources/

WORKDIR /form10

CMD ["python3", "main.py"]
