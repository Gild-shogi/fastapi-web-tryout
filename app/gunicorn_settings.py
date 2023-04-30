import os

# UNIXドメインソケット
socket_path = "unix:/tmp/asgi.sock"
# socket_path = "0.0.0.0:8000"

port = "8080"
bind = socket_path


# Debugging
reload = True

# Logging
accesslog = "-"
# loglevel = 'info'
loglevel = "debug"
logfile = "./log/app.log"
logconfig = None

# Proc Name
proc_name = "Infrastructure-Practice-FastAPI"

# Worker Processes
workers = 2
