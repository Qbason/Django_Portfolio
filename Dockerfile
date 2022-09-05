FROM ubuntu:22.04
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
#disable input during install packages
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y apt-utils vim curl apache2 apache2-utils
RUN apt-get install -y alpine
# RUN apk add --no-cache apache2
# RUN apt-get install -y apache-mod-auth-gssapi apache-mod-auth-kerb apache-mod-auth-ntlm-winbind apache-mod-auth-openidc
# RUN apt-get install -y apache-mod-auth-radius apache-mod-fcgid apache2-brotli apache2-http2 apache2-ldap
# RUN apt-get install -y apache2-lua apache2-mod-authnz-external apache2-mod-perl apache2-mod-perl-dbg
# RUN apt-get install -y apache2-mod-realdoc apache2-proxy apache2-proxy-html apache2-ssl apache2-webdav
# RUN apt-get install -y baculum-api-apache2 baculum-web-apache2 nagios-apache otrs-apache2 patchwork-uwsgi-apache2
# RUN apt-get install -y perl-libapreq2
RUN apt-get -y install python3 libapache2-mod-wsgi-py3
#python3 and python the same (shortcut)
RUN ln /usr/bin/python3 /usr/bin/python
#install pip for python
RUN apt-get -y install python3-pip
#upgrade pip and install necessary packages
RUN pip install --upgrade pip
RUN apt install -y python3.10-venv
ENV PYTHONUNBUFFERED 1
RUN mkdir /code/
WORKDIR /code/
#install packages in venv python
COPY requirements.txt /code
RUN python3 -m venv myenv_linux
RUN source /code/myenv_linux/bin/activate && pip install -r requirements.txt && pip install ptvsd
#copy code and configuration
COPY ./portfolio_manager /code/portfolio_manager
#COPY http.conf
ADD ./http.conf /etc/apache2/sites-available/http.conf
#enable site-available
RUN a2ensite http.conf
RUN a2enmod proxy
RUN a2enmod proxy_http
RUN a2enmod proxy_balancer
RUN a2enmod lbmethod_byrequests
RUN a2dismod mpm_event
RUN a2dismod mpm_worker
RUN a2enmod mpm_prefork
RUN a2enmod authz_groupfile
RUN a2enmod headers
RUN a2enmod rewrite
RUN service apache2 start && service apache2 reload && service apache2 stop
# EXPOSE 80 443
# CMD ["apache2ctl", "-D", "FOREGROUND"]