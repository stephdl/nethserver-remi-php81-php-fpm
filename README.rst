=============================
nethserver-remi-php81-php-fpm
=============================

Configure default installation of PHP 8.1 running on FPM.
The default configuration of FPM is from remi repository and has
been customized to listen on port 9081 (template: ``/etc/opt/remi/php81/php-fpm.d/z_nethserver.conf``).

Adding new configuration
========================

If you need a new configuration, simply drop a file inside ``/etc/opt/remi/php81/php-fpm.d/``
directory and execute: ::

    signal-event nethserver-remi-php81-php-fpm-update
