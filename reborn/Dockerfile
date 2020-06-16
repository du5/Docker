FROM alpine

LABEL maintainer="elrepo <322252@gmail.com>"

ENV EXCLUDE_REMARKS0=(剩余流量|到期时间|过期时间|官网地址|产品名称) \
    SPEEDTEST_MODE=all \
    TEST_SITE_PING=true \
    TEST_UPLOAD=false \
    PREFERRED_SS_CLIENT=ss-libev \
    PREFERRED_SSR_CLIENT=ssr-libev \
    PREFERRED_PING_METHOD=tcping \
    THREAD_COUNT=4 \
    LISTEN_ADDRESS=127.0.0.1 \
    LISTEN_PORT=10870 \
    EXPORT_WITH_MAXSPEED=true \
    EXPORT_SORT_METHOD=none \
    MULTILINK_EXPORT_AS_ONE_IMAGE=true \
    SINGLE_TEST_FORCE_EXPORT=true \
    EXPORT_AS_NEW_STYLE=true \
    EXPORT_COLOR_STYLE=rainbow \
    CUSTOM_COLOR_GROUPS=65535,65535,65535|32768,65535,0|65535,65535,0|65535,32768,49152|65535,0,0 \
    CUSTOM_COLOR_BOUNDS=0|65536|524288|4194304|16777216 \
    SUB_LINK=https://baidu.com

COPY stairspeedtest_reborn_linux64_v0.6.1-beta /root/stairspeedtest

RUN apk add --no-cache tzdata &&\
    cp -r -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime &&\
    apk del -f tzdata

WORKDIR /root/stairspeedtest

