FROM bitnami/minideb

RUN apt-get update &&\
    apt-get install git curl build-essential libssl-dev zlib1g-dev -y &&\
    git clone https://github.com/TelegramMessenger/MTProxy /root/MTProxy &&\
    cd /root/MTProxy &&\
    make -j8 


FROM bitnami/minideb

LABEL maintainer="elrepo <322252@gmail.com>"

COPY --from=0 /root/MTProxy/objs/bin/mtproto-proxy /usr/bin/mtproto-proxy

ENV tlsHost=github.com \
    port=443 \
    secret=f943b7565311a54cbda26087abd6e32f \
    tag=db8a2c0396036b851d663ff8d7d3707d

RUN apt-get update &&\
    apt-get install curl xxd iproute2 grep -y &&\
    apt-get autoremove &&\
    rm -rf /var/lib/apt/lists/* &&\
    mkdir -p /telegram &&\
    curl -s https://core.telegram.org/getProxySecret -o /telegram/proxy-secret &&\
    curl -s https://core.telegram.org/getProxyConfig -o /telegram/proxy-multi.conf

CMD curl "https://$tlsHost" --tlsv1.3 -s -m 3 --retry 0 -o /dev/null || error=35 &&\
    if [ "35" = "$error" ]; then echo "域名[$tlsHost]不支持 tls 1.3 协议, 请更换伪装的域名"; error=0; exit; fi &&\
    IP="$(curl -s -4 ip.sb)" &&\
    secretAppend=`echo $tlsHost | tr -d \\\\n | xxd -p` &&\
    echo "一键链接: https://t.me/proxy?server=$IP&port=$port&secret=ee$secret$secretAppend" &&\
    INTERNAL_IP="$(ip -4 route get 8.8.8.8 | grep '^8\.8\.8\.8\s' | grep -Po 'src\s+\d+\.\d+\.\d+\.\d+' | awk '{print $2}')" &&\
    mtproto-proxy -d -p 2398 -H $port --aes-pwd /telegram/proxy-secret -u nobody /telegram/proxy-multi.conf --allow-skip-dh --nat-info "$INTERNAL_IP:$IP" -S $secret -P $tag -D $tlsHost