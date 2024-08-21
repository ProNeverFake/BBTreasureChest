import logging
import colorlog

# default logger setup
handler = colorlog.StreamHandler()
handler.setFormatter(
    colorlog.ColoredFormatter(
        "%(log_color)s(%(levelname)s):[%(name)s]:%(message)s",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red,bg_white",
        },
    )
)

def setup_logger(name: str, level=logging.WARNING, special_handler=None):
    logger = logging.getLogger(name)
    if special_handler is None:
        logger.addHandler(handler)
    else:
        logger.addHandler(special_handler)
    logger.setLevel(level)
    logger.propagate = False
    return logger
