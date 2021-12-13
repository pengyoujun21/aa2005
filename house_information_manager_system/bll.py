"""
    业务逻辑层
"""
import collections
from typing import List, Dict

from dal import HouseDao
from model import HouseModel


class HouseManagerController:
    def __init__(self):
        self.__list_houses = HouseDao.load()

    @property
    def list_houses(self) -> List[HouseModel]:
        return self.__list_houses

    def get_house_by_max_total_price(self) -> HouseModel:
        return max(self.__list_houses, key =lambda house: house.total_price)

    def get_house_by_min_area(self) -> HouseModel:
        # 类内可以使用属性(属性内部返回私有变量)
        return min(self.list_houses, key =lambda house: house.area)
