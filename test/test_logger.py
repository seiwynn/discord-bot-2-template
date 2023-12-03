import sys
import os
# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Now you can import the module
from utils.logger import logger
# rest of your code


logger.debug('This is a debug message')
logger.info('This is an informational message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

