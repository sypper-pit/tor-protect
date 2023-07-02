FROM debian:latest

RUN apt-get update && apt-get install -y \
    tor 

COPY ./torrc /etc/tor/torrc
COPY ./default.conf /etc/nginx/conf.d/default.conf

RUN mkdir -p /var/lib/tor/hidden_service/ && chown -R debian-tor:debian-tor /var/lib/tor/hidden_service/ && chmod 700 /var/lib/tor/hidden_service/

CMD tor
