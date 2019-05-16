import logging
import sys


class Logger:
    DEFAULT_PROGNAME = "NAAS_PYTHON_CLIENT"

    def __init__(self, log_file=None):
        handlers = [logging.StreamHandler(sys.stdout)]
        if log_file:
            handlers.append(logging.FileHandler(log_file))
        logging.basicConfig(
            level=logging.INFO,
            handlers=handlers
        )
        self.logger = logging.getLogger()

    def warn(self, message, progname=DEFAULT_PROGNAME):
        self.logger.warning(progname + ": " + message)

    def debug(self, message, progname=DEFAULT_PROGNAME):
        self.logger.debug(progname + ": " + message)

    def fatal(self, message, progname=DEFAULT_PROGNAME):
        self.logger.critical(progname + ": " + message)

    def error(self, message, progname=DEFAULT_PROGNAME):
        self.logger.error(progname + ": " + message)

    def info(self, message, progname=DEFAULT_PROGNAME):
        self.logger.info(progname + ": " + message)

