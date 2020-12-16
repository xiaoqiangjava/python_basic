#!/usr/bin/python
# -*- encoding: utf-8 -*-
import asyncio
import time


# Task对象：在事件循环中添加多个任务
# Task用于并发的调度协程，通过asyncio.create_task(协程对象)的方式创建Task对象，这样可以让协程对象加入事件循环中
# 等待被调度执行。除了使用asyncio.create_task()函数创建Task对象外，还可以使用底层的loop.create_task()或ensure_future()
# 函数。不建议手动实例化Task对象
# 注意：asyncio.create_task()函数是Python3.7加入的，之前的版本可以使用asyncio.ensure_future()函数来创建Task对象
async def func(param):
    print("start func..", param)
    await asyncio.sleep(1)
    print("end func..", param)


# 多个Task对象可以通过下面的方式来调度，但是这种写法不常见，常见的是将Task添加到一个列表中进行调度
async def main():
    print("start main..")
    # 创建Task对象，将func()协程对象添加到事件循环
    task1 = asyncio.create_task(func("task1"))
    task2 = asyncio.create_task(func("task2"))
    print(type(task1))
    print("end main..")
    # 当执行某协程遇到IO操作时，会自动化切换其他任务，此处的await是等待相应的协程全部执行完毕并获取结果
    ret1 = await task1
    ret2 = await task2  # await后面可以跟Task对象


# 常见的Task调度写法
async def main_main():
    print("start main_main")
    task_list = [asyncio.create_task(func("main_task1")), asyncio.create_task(func("main_task2"))]
    time.sleep(2)
    print("end main_main")
    done, pending = await asyncio.wait(task_list)  # 等待所有的协程执行完毕返回，返回值是一个元祖(done, pending)
    print(done)
    print(type(done))
    for result in done:
        print(type(result))
        result.exception()



# 调用协程
asyncio.run(main())
# asyncio.run(main_main())
