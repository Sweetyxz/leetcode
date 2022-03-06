import logging
from logging import debug

logging.basicConfig(format='%(levelname)s:%(funcName)s:%(message)s', level=logging.DEBUG)

def func():
    logging.debug('debug 信息')

if __name__ == '__main__':
    func()
