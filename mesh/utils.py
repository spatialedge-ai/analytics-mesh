import logging


def get_logger(level=logging.INFO, filename=None):
    """
    use the basics from analytics-mesh for this instead.
    """
    log = logging.getLogger()
    # we nuke the existing handlers whenever this function is called (else they stack)
    log.handlers = []
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s')
    log.setLevel(level)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    log.addHandler(stream_handler)
    if filename:
        file_handler = logging.FileHandler(filename)
        file_handler.setFormatter(formatter)
        log.addHandler(file_handler)
    return log

