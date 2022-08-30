FROM ubuntu:22.04
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
#disable input during install packages
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y apt-utils vim curl apache2 apache2-utils
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
RUN source myenv_linux/bin/activate
RUN pip install -r requirements.txt
RUN pip install ptvsd
#copy code and configuration
COPY portfolio_manager /code/

ADD ./http.conf /etc/apache2/sites-available/http.conf
# RUN a2ensite http.conf
# RUN a2enmod proxy
# RUN a2enmod proxy_http
# RUN a2enmod proxy_balancer
# RUN a2enmod lbmethod_byrequests
# RUN service apache2 start
# RUN service apache2 reload
EXPOSE 80
CMD ["apache2ctl", "-D", "FOREGROUND"]