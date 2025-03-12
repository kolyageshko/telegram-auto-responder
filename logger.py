import logging
import colorlog

def setup_logger():
    log_format = "%(log_color)s[%(asctime)s] %(levelname)s: %(message)s%(reset)s"
    log_colors = {
        "DEBUG": "cyan",
        "INFO": "bold_white",
        "SUCCESS": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red"
    }

    formatter = colorlog.ColoredFormatter(log_format, log_colors=log_colors, datefmt="%Y-%m-%d %H:%M:%S")

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logging.basicConfig(
        level=logging.INFO,
        handlers=[handler]
    )

    return logging.getLogger(__name__)

logger = setup_logger()