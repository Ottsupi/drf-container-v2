import os

# Google Cloud Run default port is 8080
PORT = os.environ.get('PORT', default='8080')
HOST = '0.0.0.0'
bind = f'{HOST}:{PORT}'

workers = 2
threads = 4
timeout = 0
