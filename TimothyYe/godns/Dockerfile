FROM golang:alpine AS builder

WORKDIR /root/

RUN apk add --no-cache git &&\
    git clone https://github.com/TimothyYe/godns godns &&\
    cd /root/godns &&\
    go build -o godns cmd/godns/godns.go

FROM alpine

ENV IP_TYPE=IPV4 \
    IP_URL=http://get.ddns.tokyo/ip \
    INTERVAL=300 \
    SUB_DOMAINS=www \
    DOMAIN_NAME=example.com \
    TOKEN_ID=123456 \
    TOKEN_VALUE=gfj4bm3w052jan7v75o6o8fywphplmc4

WORKDIR /root/

COPY --from=builder /root/godns/godns /usr/local/bin/

COPY config.json /root/

CMD sed -i "s|IP_TYPE|${IP_TYPE}|"          config.json &&\
    sed -i "s|INTERVAL|${INTERVAL}|"        config.json &&\
    sed -i "s|DOMAIN_NAME|${DOMAIN_NAME}|"  config.json &&\
    sed -i "s|SUB_DOMAINS|${SUB_DOMAINS}|"  config.json &&\
    sed -i "s|TOKEN_ID|${TOKEN_ID}|"        config.json &&\
    sed -i "s|TOKEN_VALUE|${TOKEN_VALUE}|"  config.json &&\
    sed -i "s|IP_URL|${IP_URL}|"            config.json &&\
    godns