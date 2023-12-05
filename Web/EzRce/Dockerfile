FROM safoorsafdar/php-7.4.16-apache-buster

COPY ./src/ /var/www/html/
COPY ./sources.list /etc/apt/
COPY ./flag /flag

RUN chmod 777 -R /var/www/html/ && chmod 400 /flag && chmod u+s /usr/bin/find