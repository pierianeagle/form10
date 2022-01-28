FROM ubuntu

RUN apt update && \
    apt upgrade -y

RUN apt install -y python3-dev python3-pip

# # fix me!
# RUN pip install -r requirements.txt
RUN pip install beautifulsoup4 nltk scikit-learn flask waitress

RUN python3 -m nltk.downloader popular -d ../resources/data/nltk_data

COPY src/ /src/
COPY resources/ /resources/

WORKDIR /src

CMD ["python3", "main.py"]
