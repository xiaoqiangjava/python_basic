#! /usr/bin/python
# -*- encoding: utf-8 -*-

from basic.compre_case import cards_tools

# 定义一个操作列表
action_list = ["1", "2", "3"]


def action():
    """
    处理用户输入的操作
    :return:
    """
    while True:
        # 打印欢迎界面，显示功能菜单
        cards_tools.show_menu()
        action_str = input("请选择操作功能：")
        # print("您选择的操作是：【%s】" % action_str)
        if action_str in action_list:
            if action_str == "1":
                # 新建名片
                cards_tools.add_card()
            elif action_str == "2":
                # 显示全部
                cards_tools.list_cards()
            else:
                # 查询名片
                cards_tools.query_card()
        elif action_str == "0":
            print("欢迎再次使用【名片管理系统】！")
            break
        else:
            print("您输入的操作有误，请重新选择！")


# 名片管理系统主程序入口
if __name__ == "__main__":
    # 处理用户的操作
    action()
