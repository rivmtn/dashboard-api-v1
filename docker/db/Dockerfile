FROM mysql:8.0.32

RUN microdnf install -y vim
RUN rm /etc/localtime
RUN ln -s /usr/share/zoneinfo/Asia/Seoul /etc/localtime

RUN chmod 755 /etc/mysql/conf.d
RUN chmod 755 /docker-entrypoint-initdb.d

COPY start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh

ENTRYPOINT ["/usr/local/bin/start.sh"]