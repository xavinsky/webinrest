===========
Description
===========

What is webinrest ?
------------------

webinrest is a Webserver for publish restructured text to html document 
in folder structure with a navigation menu.

Install
-------

see INSTALL.txt

Configure
---------

Default config file is /etc/webinrest/webinrest.conf.
You can make another one or change it.
Read in the config file for informations.

Start
-----

Sample command line for start the server :: 

    # the file config default is /etc/webinrest/webinrest.conf

    # default is localhost:8000, and the folder shared is the curent folder.
    webinrest

    # for use another configuration file : 
    webinrest -c ~/mywebinrest/webinrest.conf

    # precise the folder with ReStructuredText content to share with webinrest
    webinrest -d /var/www/restfolder

    # for change the hostname and the port.
    webinrest -n localhost -p 8000 

    # you can combine all the options
    # more option available in the config file. (just read it)
