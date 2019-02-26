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

'''
format中可以用到的格式化信息:
%(name)s             --logger的名字
%(levelno)s          --数字格式的日志级别
%(levelname)s        --文本格式的日志级别
%(filename)s         --调用日志输出函数的模块的文件名
%(funcName)s         --调用日志输出函数的函数名
%(lineno)d           --调用日志输出函数的语句所在的代码行
%(asctime)s          --字符串格式的当前时间
%(threadName)s       --线程名
$(message)s          --用户输出的信息         
'''

