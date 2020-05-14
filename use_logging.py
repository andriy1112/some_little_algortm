import os, platform, logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'), \
                                os.getenv('HOMEPATH'), \
                                'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'), 'test.log')

print('lon in', logging_file)

logging.basicConfig(
    lavel = logging.DEBUG,
    format = '%(asctime)s : %(levelname)s : %(massage)s',
    filename = logging_file,
    filemode = 'w',
)

logging.debug('program start')
logging.info('some move')
logging.warning('program is die')
print()