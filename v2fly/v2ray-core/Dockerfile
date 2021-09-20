FROM alpine

LABEL maintainer="elrepo <322252@gmail.com>"

ENV port=80 \
    uuid=44E24D96-2105-4440-88A1-7D7DCAB327B5 \
    aid=0 \
    path=/ws

RUN apk add --no-cache curl unzip

COPY config.json /

WORKDIR /root

CMD rm -rf * &&\
    curl https://github.com/v2fly/v2ray-core/releases/download/v4.41.1/v2ray-linux-64.zip -Lo v2ray.zip &&\
    unzip v2ray.zip &&\
    rm -rf v2ray.zip &&\
    chmod +x v2ctl v2ray &&\
    cp /config.json . &&\
    sed -i "s|wsport|${port}|" config.json &&\
    sed -i "s|uuid|${uuid}|" config.json &&\
    sed -i "s|aid|${aid}|" config.json &&\
    sed -i "s|wsSettings.path|${path}|" config.json &&\
    ./v2ray
