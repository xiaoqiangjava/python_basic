#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 名片管理系统功能模块

# 记录所有名片
card_list = []
table_head = ["姓名", "电话", "QQ", "邮箱"]


def show_menu():
    """
    欢迎界面，打印名片管理系统的欢迎界面
    :return:
    """
    print("*" * 60)
    print("* 欢迎使用【名片管理系统】v1.0：")
    print("* ")
    print("* 1. 新建名片")
    print("* 2. 显示全部")
    print("* 3. 查询名片")
    print("* ")
    print("* 0. 退出系统")
    print("*" * 60)


def add_card():
    """
    新增名片
    :return:
    """
    print("-" * 60)
    print("【新增名片：】")
    # 提示用户输入名片信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话号码：")
    qq_str = input("请输入QQ号码：")
    email_str = input("请输入电子邮箱：")
    # 将用户输入的信息保存到字典中
    card_dict = {"name": name_str, "phone": phone_str, "QQ": qq_str, "email": email_str}
    # 将名片信息保存到名片列表中
    card_list.append(card_dict)
    # 提示用户名片添加成功
    print("添加 %s 的名片成功！" % name_str)


def list_cards():
    """
    显示所有名片
    :return:
    """
    print("-" * 60)
    print("【显示所有名片：】")
    # 当没有添加名片是提示用户先添加名片
    if len(card_list) == 0:
        print("名片列表中没有名片记录，请先添加名片！")
        return
    # 打印表头
    for name in table_head:
        print("%-15s" % name, end="")
    # 打印分割线
    print("")
    print("-" * 70)
    # 遍历列表，依次输出字典信息
    for card_dict in card_list:
        for card_info in card_dict.values():
            print("%-16s" % card_info, end="")
        print("")
    print("-" * 70)


def query_card():
    """
    查询名片
    :return:
    """
    print("-" * 60)
    print("【查询名片：】")
    # 提示用户输入姓名搜索
    find_name = input("请输入要查询的姓名：")
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            # 如果存在查找的名片信息，显示名片详细信息
            for table_info in table_head:
                print("%-15s" % table_info, end="")
            print("")
            print("-" * 70)
            for card_info in card_dict.values():
                print("%-16s" % card_info, end="")
            print("")
            print("-" * 70)
            # 修改或者删除名片
            update_card(card_dict)
            break
    else:
        print("不存在【%s】的名片信息" % find_name)


def update_card(card_dict):
    """
    修改或者删除字典
    :param card_dict:
    :return:
    """
    action_str = input("请选择需要执行的操作：[1] 修改 [2] 删除 [0] 返回上级菜单：")
    if action_str == "1":
        print("请输入需要修改的值，不修改直接回车")
        card_dict["name"] = input_card_info(card_dict["name"], "姓名：")
        card_dict["phone"] = input_card_info(card_dict["phone"], "电话：")
        card_dict["QQ"] = input_card_info(card_dict["QQ"], "QQ：")
        card_dict["email"] = input_card_info(card_dict["email"], "邮箱：")
        print("名片修改成功！")
    elif action_str == "2":
        card_list.remove(card_dict)
        print("%s的名片删除成功！" % card_dict["name"])
    elif action_str == "0":
        pass
    else:
        print("您的输入有误！")


def input_card_info(dict_value, tip_input):
    """
    处理用户输入的名片信息，如果用户没有输入则返回字典中value，否则返回用户输入的信息
    :param dict_value: 原来字典中的value
    :param tip_input: 提示语
    :return: 修改后的字典value
    """
    input_value = input(tip_input)
    if input_value == "" or input_value is None:
        return dict_value
    else:
        return input_value
