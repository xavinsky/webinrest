#!/bin/sh
sudo aptitude install python-docutils python-magic python-argparse git
cd /usr/local/lib
git clone https://github.com/xaviermanach/rest2web.git
ln -s /usr/local/lib/rest2web/rest2web /usr/local/bin
ln -s /usr/local/lib/rest2web/searchinfiles.py /usr/local/lib/python2.`python -V 2>&1 | awk -F '.' '{print $2}'`/dist-packages/
mkdir /etc/rest2web
cp -r /usr/local/lib/rest2web/config/* /etc/rest2web
mkdir -p /var/www/rest2web
