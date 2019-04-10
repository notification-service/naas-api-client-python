import logging


class Logger:
    DEFAULT_PROGNAME = "NAAS_RUBY_CLIENT"

    def __init__(self):
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

