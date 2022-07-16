FROM ubuntu

LABEL maintainer="sanya namotchik na firewall first rang"

RUN apt update -y && apt install nginx curl software-properties-common -y
RUN add-apt-repository ppa:ondrej/php
RUN DEBIAN_FRONTEND=noninteractive TZ=Asia/Yekaterinburg apt-get -y install tzdata
RUN apt update -y && apt install php7.4-fpm php7.4-cli php7.4-common php7.4-mbstring php7.4-xmlrpc php7.4-soap php7.4-gd php7.4-xml php7.4-intl php7.4-mysql php7.4-cli php7.4-ldap php7.4-zip php7.4-mcrypt php7.4-curl php7.4-opcache php7.4-readline php7.4-xml php7.4-gd -y

RUN mkdir /wp
WORKDIR /wp
RUN curl -O https://ru.wordpress.org/latest-ru_RU.tar.gz
RUN tar -xvzf latest-ru_RU.tar.gz -C /var/www/html/
RUN mkdir /etc/nginx/certs/

COPY wp-config.php /var/www/html/wordpress/wp-config.php
COPY start.sh /wp/start.sh

RUN chmod +x start.sh
RUN chown root:root start.sh

VOLUME [/etc/nginx/certs/]
VOLUME [/etc/nginx/sites-enabled/]

EXPOSE 80 443
ENTRYPOINT ./start.sh