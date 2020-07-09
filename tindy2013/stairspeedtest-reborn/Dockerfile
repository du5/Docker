FROM alpine

LABEL maintainer="elrepo <322252@gmail.com>"

ENV SPEEDTEST_MODE=all \
    TEST_SITE_PING=true \
    TEST_UPLOAD=false \
    PREFERRED_SS_CLIENT=ss-libev \
    PREFERRED_SSR_CLIENT=ssr-libev \
    PREFERRED_PING_METHOD=tcping \
    THREAD_COUNT=4 \
    LISTEN_ADDRESS=127.0.0.1 \
    TEST_NAT_TYPE=true \
    LISTEN_PORT=10870 \
    EXPORT_WITH_MAXSPEED=true \
    EXPORT_SORT_METHOD=none \
    MULTILINK_EXPORT_AS_ONE_IMAGE=true \
    SINGLE_TEST_FORCE_EXPORT=true \
    EXPORT_AS_NEW_STYLE=true \
    EXPORT_COLOR_STYLE=rainbow \
    SUB_LINK=https://baidu.com

COPY stairspeedtest_reborn_linux64_fc75385 /root/stairspeedtest

RUN apk add --no-cache tzdata jq imagemagick curl &&\
    cp -r -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime &&\
    apk del -f tzdata

WORKDIR /root/stairspeedtest

CMD sed -i "s|_SPEEDTEST_MODE_|${SPEEDTEST_MODE}|" pref.ini && \
    sed -i "s|_TEST_SITE_PING_|${TEST_SITE_PING}|" pref.ini && \
    sed -i "s|_TEST_UPLOAD_|${TEST_UPLOAD}|" pref.ini && \
    sed -i "s|_PREFERRED_SS_CLIENT_|${PREFERRED_SS_CLIENT}|" pref.ini && \
    sed -i "s|_PREFERRED_SSR_CLIENT_|${PREFERRED_SSR_CLIENT}|" pref.ini && \
    sed -i "s|_PREFERRED_PING_METHOD_|${PREFERRED_PING_METHOD}|" pref.ini && \
    sed -i "s|_THREAD_COUNT_|${THREAD_COUNT}|" pref.ini && \
    sed -i "s|_LISTEN_ADDRESS_|${LISTEN_ADDRESS}|" pref.ini && \
    sed -i "s|_TEST_NAT_TYPE_|${TEST_NAT_TYPE}|" pref.ini && \
    sed -i "s|_LISTEN_PORT_|${LISTEN_PORT}|" pref.ini && \
    sed -i "s|_EXPORT_WITH_MAXSPEED_|${EXPORT_WITH_MAXSPEED}|" pref.ini && \
    sed -i "s|_EXPORT_SORT_METHODs_|${EXPORT_SORT_METHODs}|" pref.ini && \
    sed -i "s|_MULTILINK_EXPORT_AS_ONE_IMAGE_|${MULTILINK_EXPORT_AS_ONE_IMAGE}|" pref.ini && \
    sed -i "s|_SINGLE_TEST_FORCE_EXPORT_|${SINGLE_TEST_FORCE_EXPORT}|" pref.ini && \
    sed -i "s|_EXPORT_AS_NEW_STYLE_|${EXPORT_AS_NEW_STYLE}|" pref.ini && \
    sed -i "s|_EXPORT_COLOR_STYLE_|${EXPORT_COLOR_STYLE}|" pref.ini && \
    ./stairspeedtest /u ${SUB_LINK} &&\
    sh upload.sh `ls results/*.png`