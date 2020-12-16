#!/usr/bin/python
# -*- encoding: utf-8 -*-
import asyncio


# 协程函数
async def others():
    print("other start..")
    await asyncio.sleep(1)  # await + 可等待对象（协程对象，Task对象，Future对象）
    print("other end..")


# 协程函数定义
async def func():
    print("start..")
    await others()
    print("end..")


# 获取协程对象: 调用协程函数不会直接执行该函数，而是返回一个协程对象
result = func()
print(type(result))  # 直接调用协程函数，会有一个RuntimeWarning，表示协程函数没有等待

# 如果需要执行一个协程函数，必须通过事件循环来执行
# loop = asyncio.get_event_loop()   # 创建或者获取一个时间循环
# loop.run_until_complete(result)  # 将协程对象添加到事件循环中运行
asyncio.run(result)  # python3.7之后
