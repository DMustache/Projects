from abc import *

class PId(ABC):
    @property
    @abstractmethod
    def id(self):
        pass

class Priced(ABC):
    @property
    @abstractmethod
    def price(self):
        pass

class Goods(PId, Priced):
    def __init__(self, p_id, p_price):
        self._id = p_id
        self._price = p_price

    @property
    def id(self):
        return self._id

    @property
    def id(self):
        return self._price

def show_id_and_price(info):
    print(f"id = {info.id}, price = {info.price}")

bread = Goods(1, 5)
show_id_and_price(bread)