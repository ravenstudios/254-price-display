#! /bin/bash
cd /home/pi/254-price-display
source  bin/activate 2> /tmp/price_display_error.log
cd /home/pi/254-price-display/price_display
python3 manage.py runserver 8080  2> /tmp/price_display_error.log
