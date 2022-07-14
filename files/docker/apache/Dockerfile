FROM ubuntu

LABEL maintainer="sanya namotchik na firewall first rang"

RUN apt update -y && apt install apache2 curl software-properties-common -y
RUN add-apt-repository ppa:ondrej/php
RUN DEBIAN_FRONTEND=noninteractive TZ=Asia/Yekaterinburg apt-get -y install tzdata
RUN apt update -y && apt install php7.4 php7.4-mysql libapache2-mod-php7.4 php7.4-cli php7.4-cgi php7.4-gd -y

RUN a2enmod rewrite
RUN service apache2 restart

RUN mkdir /wp
WORKDIR /wp
RUN curl -O https://ru.wordpress.org/latest-ru_RU.tar.gz
RUN tar -xvzf latest-ru_RU.tar.gz -C /var/www/
RUN touch /var/www/wordpress/.htaccess

COPY wp-config.php /var/www/wordpress/wp-config.php
COPY default.conf /etc/apache2/sites-enabled/000-default.conf 
COPY apache.conf /etc/apache2/sites-available/apache.conf

EXPOSE 80 443
CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]