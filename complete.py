import logging
 
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')



# BASIC CONFIGURATIONS 
# logging.basicConfig(level=logging.DEBUG)
# logging.debug('This will get logged')



# appending to the file
# logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
# logging.warning('This will get logged to a file-----------------')

# formatting the out put
# logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
# logging.warning('This is a Warning')

# logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
# logging.info('Admin logged in')


# logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
# logging.warning('Admin logged out')

# Loggign variable data
# name = 'bhaktha'
# logging.error('%s raised an error', name)
# logging.error(f'{name} raised an error')


# capturing stack traces
# a = 5
# b = 0

# try:
#     c = a/b
# except Exception as e:
#     logging.error('Exception occured', exc_info=True)

# classes and functions 
# logger = logging.getLogger('example_logger')
# logger.warning('This is warning')




# USING HANDLERS
# create a custom logger
# logger = logging.getLogger(__name__)

# create handlers
# c_handler = logging.StreamHandler()
# f_handler = logging.FileHandler('file.log')
# c_handler.setLevel(logging.WARNING)
# f_handler.setLevel(logging.ERROR)

# create formatter and add it to handlers
# c_format = logging.Formatter('%(name)s - %(message)s')
# f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# c_handler.setFormatter(c_format)
# f_handler.setFormatter(f_format)

# add handlers to the logger
# logger.addHandler(c_handler)
# logger.addFilter(f_handler)

# logger.warning('This is a warning')
# logger.error('This is an error')

# Other configuration methods
import logging.config

# logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)
# get the logger in the specified file 
# logger = logging.getLogger(__name__)
# logger.debug('This is a debug message')




# Updating with custom variable 
# a = input('Enter your number')

# logging.basicConfig(filename='varibale.log', filemode='a', format='%(asctime)s - %(message)s')
# logging.warning(f'The entered number is {a}')

# print('The log has been upadted')

import os
# print(os.getcwd())
# print(os.path.basename(__file__))

# logfile = os.path.basename(__file__).replace('py', 'log')
# print(logfile)

# a = input('Enter your number')
# logging.basicConfig(filename=logfile, filemode='a', format='%(asctime)s - %(message)s')
# logging.warning(f'The entered number is {a}')
# print('The log has been updated')

# logging.basicConfig()

# a = 10
# logging.basicConfig(filename='sample1.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
# logging.info(f'The entered number is {a}')

# logging.debug(f'The entered number is {a}')
# logging.info(f'The entered number is {a}')
# logging.warning(f'The entered number is {a}')
# logging.error(f'The entered number is {a}')
# logging.critical(f'The entered number is {a}')

# print('The log has been updated')



# a = input('Enter your number: ')
# logging.basicConfig(filename='sample2.log', filemode='a', level=logging.info, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.info(f'The entered number is {a}')

# a = input('Enter your number: ')
# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)
# logging.info(f'The entered number is {a}')


# import logging
# logging.basicConfig(filename='example1.log', encoding='utf-8', level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')



# myapp.py
import logging
# import mylib

# def main():
#     logging.basicConfig(filename='myapp.log', level=logging.INFO)
#     logging.info('Started')
#     # mylib.do_something()
#     logging.info('Finished')

# if __name__ == '__main__':
#     main()

# logfile = os.path.basename(__name__).replace('py', 'log')
# logging.basicConfig(filename=logfile, level=logging.INFO)
# logging.info('Started')
# logging.info('Finished')


# logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# logging.warning('is when this event was logged.')


logger = logging.getLogger(__name__)
print(logger)

















