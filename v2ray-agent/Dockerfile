FROM alpine

LABEL maintainer="elrepo <322252@gmail.com>"

RUN apk add --no-cache curl ca-certificates &&\
    curl https://down.v2ray.page/agents/$(curl https://down.v2ray.page/agents/latest -s) -s -o /root/agent &&\
    chmod +x /root/agent &&\
    apk del -f curl

WORKDIR /root

CMD ./agent