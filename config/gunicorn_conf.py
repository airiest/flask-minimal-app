import os

# Sever Socket
host = '0.0.0.0'
port = os.getenv('PORT', 9101)
bind = str(host) + ':' + str(port)

# Debugging
reload = True

# Logging
accesslog = '-'
loglevel = 'debug'

# Proc Name
proc_name = 'gunicorn-flask'

# Worker Processes
workers = 1
worker_class = 'sync'
