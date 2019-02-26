#!/usr/bin/python
# -*- encoding: utf-8 _-*-
import logging

logger = logging.getLogger('file_logger')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='test_logger.log', mode='w', encoding='utf-8')
handler.setFormatter(logging.Formatter('[%(levelname)s] %(asctime)s [%(threadName)s] %(message)s'))
logger.addHandler(handler)

logger.info("这是一个INFO级别的日志信息")
logger.error("这是一个error级别的日志信息")
logger.warning("这是一个WARN级别的日志信息")

