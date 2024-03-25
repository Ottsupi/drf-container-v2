import multiprocessing
import os

# Google Cloud Run default port is 8080
PORT = os.environ.get('PORT', default='8080')
HOST = '0.0.0.0'
bind = f'{HOST}:{PORT}'

cores = multiprocessing.cpu_count()

workers = (2 * cores) + 1
threads = 4
timeout = 0
