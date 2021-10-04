FROM apache/zeppelin:0.9.0
USER root
WORKDIR /opt/zeppelin

#RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | apt-key add -

RUN apt-get update && \
apt-get -y install gnupg

RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | apt-key add -

RUN echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list && \
apt-get update && \
apt-get install -y mongodb-org-shell

WORKDIR ${Z_HOME}

RUN wget https://www.ine.es/experimental/movilidad/movilidad_cotidiana_marzo_junio_2020.zip
RUN apt-get install unzip
RUN unzip movilidad_cotidiana_marzo_junio_2020.zip
RUN rm movilidad_cotidiana_marzo_junio_2020.zip

CMD ["bin/zeppelin.sh"]
