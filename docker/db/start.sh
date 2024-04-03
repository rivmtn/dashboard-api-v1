#!/bin/sh

# 권한 변경
chmod 755 /var/run/mysqld/mysqld.sock
chmod 755 /etc/mysql/conf.d/my.cnf

# 원래의 entrypoint 실행
docker-entrypoint.sh mysqld