#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import logging
import logging.config


logging.config.fileConfig('logger.conf')  #Using the configuration file


root_logger = logging.getLogger('root')
root_logger.debug('otomat root logger....')


# "application" code 
logger = logging.getLogger('main')
logger.info('test main logger')
logger.info('start import module \'mod\'...')

logger.debug('let\'s test dug infomation')

root_logger.info('finish test...')
