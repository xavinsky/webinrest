===========
Description
===========

What is rest2web ?
------------------

rest2web is a Webserver for publish restructured text to html document 
in folder structure with a navigation menu.

Install
-------

Install in wheezy debian environement ::

    sudo su
    aptitude install python-docutils python-magic
    tar zxvf rest2web.tgz
    mv rest2web /usr/local/lib
    ln -s /usr/local/lib/rest2web/rest2web /usr/local/bin
    ln -s /usr/local/lib/rest2web/searchinfiles.py /usr/local/lib/python2.7/dist-packages/
    mkdir /etc/rest2web
    cp -r /usr/local/lib/rest2web/config/ /etc/rest2web

Configure
---------

Default config file is /etc/rest2web/rest2web.conf.
You can make another one or change it.
Read in the config file for informations.

Start
-----

Sample command line for start the server :: 

    # the file config default is /etc/rest2web/rest2web.conf

    # default is localhost:8000, and the folder shared is the curent folder.
    rest2web

    # for use another configuration file : 
    rest2web -c ~/myrest2web/rest2web.conf

    # precise the folder with ReStructuredText content to share with rest2web
    rest2web -d /var/www/restfolder

    # for change the hostname and the port.
    rest2web -n localhost -p 8000 

    # you can combine all the options
    # more option available in the config file. (just read it)
