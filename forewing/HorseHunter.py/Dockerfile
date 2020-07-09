FROM python:3-alpine

LABEL maintainer="elrepo <322252@gmail.com>"

COPY 2eb49cd4d9987fc27d7dcba230ae106c86aaec38 /root/HorseHunter.py

WORKDIR /root/HorseHunter.py

RUN pip install -I -r requirements-api.txt

CMD sed -i "s|port=6675|host=\"0.0.0.0\", port=6675|" HorseHunterAPI.py && \
    python HorseHunterAPI.py