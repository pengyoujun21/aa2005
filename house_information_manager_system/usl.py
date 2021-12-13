"""
    用户显示层
"""
from bll import HouseManagerController
from model import HouseModel


class HouseManagerView:
    def __init__(self):
        self.__controller = HouseManagerController()

    def __display_menu(self):
        print("1键查看所有房源信息")
        print("2键查看总价最高的房源信息")
        print("3键查看面积最小的房源信息")

    def __select_menu(self):
        item = input("请输入选项：")
        if item == "1":
            self.__display_houses()
        elif item == "2":
            self.__output_house_by_max_total_price()
        elif item == "3":
            self.__output_house_by_min_area()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_houses(self):
        for house in self.__controller.list_houses:
            self.__show_house(house)

    def __output_house_by_max_total_price(self):
        house = self.__controller.get_house_by_max_total_price()
        self.__show_house(house)

    def __show_house(self, house: HouseModel):
        print("%d|%s|%s|%s+|%s|%s|%s|%s|%d|%d|%s" % (
            house.id, house.title, house.community, house.years, house.house_type, house.area, house.floor,
            house.description, house.total_price, house.unit_price, house.follow_info))

    def __output_house_by_min_area(self):
        house = self.__controller.get_house_by_min_area()
        self.__show_house(house)
