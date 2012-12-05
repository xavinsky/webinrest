#!/bin/sh
sudo aptitude install python-docutils python-magic python-argparse git supervisor
cd /usr/local/lib
git clone https://github.com/xaviermanach/webinrest.git
ln -s /usr/local/lib/webinrest/webinrest /usr/local/bin
ln -s /usr/local/lib/webinrest/searchinfiles.py /usr/local/lib/python2.`python -V 2>&1 | awk -F '.' '{print $2}'`/dist-packages/
mkdir /etc/webinrest
cp /usr/local/lib/webinrest/config/webinrest.conf /etc/webinrest
cp -r /usr/local/lib/webinrest/config/includes /etc/webinrest
mkdir -p /var/www/webinrest
cp /usr/local/lib/webinrest/config/supervisord/webinrest.conf /etc/supervisor/conf.d/
supervisorctl reread
supervisorctl reload

