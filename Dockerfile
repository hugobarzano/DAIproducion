FROM ubuntu:latest

#Autor
MAINTAINER Hugo Barzano Cruz <hugobarzano@gmail.com>
ENV PYTHONUNBUFFERED 1

# variables de ambiente

RUN sudo apt-get install -y git
RUN sudo git clone https://github.com/hugobarzano/DAIproducion.git

#Actualizar Sistema Base
RUN sudo apt-get -y update

RUN sudo apt-get install -y python-setuptools
RUN sudo apt-get -y install python-dev
RUN sudo apt-get -y install build-essential
RUN sudo easy_install pip
RUN sudo pip install --upgrade pip

RUN ls -la
RUN pwd
RUN cd DAIproducion/ && sudo pip install -r requirements.txt


# PRODUCCION
run pip install gunicorn

# servidor web y watchdog
run apt-get install -y supervisor nginx

#  configuraciones
run cp DAIproducion/supervisor.conf /etc/supervisor/conf.d/
run cp  DAIproducion/nginx-default /etc/nginx/sites-available/default

run sed -i 's/DEBUG = True/DEBUG= False/' practica4/settings.py

expose 80

cmd DAIproducion/collect_static.sh && supervisord
