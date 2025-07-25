import logging
from logging.handlers import TimedRotatingFileHandler

log_handler = TimedRotatingFileHandler("terminalgpt.log", when="midnight", interval=1, backupCount=7)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[log_handler, logging.StreamHandler()]
)

logger = logging.getLogger(__name__)
