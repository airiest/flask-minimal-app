#!/bin/bash

gunicorn flask_app:app -k flask_sockets.worker -c ./config/gunicorn_conf.py -b 0.0.0.0:9000