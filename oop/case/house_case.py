#! /usr/bin/python
# -*- encoding: utf-8 -*-

# 摆放家具，房子有户型，总面积，家具名称列表等属性
# 家具有名字和占地面积
# 要求将三件家具添加到房子中


class HouseItem:
    """
    家具类，有名字和占地面积两个属性
    """

    def __init__(self, name, area):
        """
        初始化属性
        :param name: 名称
        :param area: 占地面积
        """
        self.name = name
        self.area = area

    def __str__(self):
        """
        自定义输出
        :return: 家具信息
        """
        return "%s 占地面积 %.2f" % (self.name, self.area)


class House:
    """
    房子类：户型，总面积，剩余面积，家具列表
    """

    def __init__(self, house_type, area):
        """
        初始化属性
        :param house_type: 户型
        :param area: 总面积
        """
        self.house_type = house_type
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.item_list = []

    def __str__(self):
        # python中可以自动将()中的代码连接到一起
        return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
                % (self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self, item):
        """
        添加家具
        :param item: 家具
        :return:
        """
        # 判断面积，如果家具面积大于房子剩余面积，提示家具太大
        if item.area > self.free_area:
            print("%s 的面积太大了" % item.name)
            return
        # 将家具的名称添加到间距列表中
        self.item_list.append(item.name)
        # 计算家具剩余面具
        self.free_area -= item.area


# 1. 创建家具
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)
print(bed)
print(chest)
print(table)

# 2. 创建房子
house = House("三室一厅", 100)

# 3. 添加家具
house.add_item(bed)
house.add_item(chest)
house.add_item(table)
print(house)
