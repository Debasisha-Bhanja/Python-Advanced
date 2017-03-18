import pygogo as gogo
from pygogo import logger

#logger = gogo.Gogo(__name__).get_structured_logger(connid='1234')
logger.info('log message')
logger.debug('hello world')
logger.error('hello error')
