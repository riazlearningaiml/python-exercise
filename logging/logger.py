import logging


logging.basicConfig(
    level = logging.CRITICAL,
    filename = 'app.log',
    filemode = 'w',
    format = '%(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S'
)
