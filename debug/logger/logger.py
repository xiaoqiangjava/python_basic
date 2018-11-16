#! /usr/bin/python
# -*- encoding: utf-8 -*-
import logging


# python内建模块logging可以打印日志, 日志级别有: DEBUG, INFO, WARN, ERROR, FATAL
# 默认的级别是ERROR, 如果需要打印INFO或者DEBUG级别的日志, 需要修改日志的级别
logging.basicConfig(level=logging.INFO)
def evaluate():
    try:
        num_str = input("请输入一个数字: ")
        num = int(num_str)
        return 100 / num
    except ValueError as e:
        logging.error("请输入一个数字")
        logging.exception(e)
    except ZeroDivisionError as e:
        logging.info("%d is zero" % num)
        logging.error("输入的数不能为0")
        logging.exception(e)
    finally:
        logging.info("process end")


if __name__ == '__main__':
    evaluate()
    