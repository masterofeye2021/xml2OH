from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class KNXAddress():
    def __init__(self) -> None:
        self._config = ""
        self._dpt = ""
        self._isReading = False
        self._main_gw_main = ""
        self._main_gw_middle = ""
        self._main_gw_sub = ""

    def __str__(self) -> str:
        return f'{self.main_gw}, {self.main_gw_main}, {self.main_gw_middle}, {self.main_gw_sub}'
    
    def __config__(self):
        return self._config + "=\""
    
    def config(self, config: str):
        self._config = config

    def __dpt__(self):
        if not self._dpt:
            return ""
        return self._dpt + ":"

    def dpt(self, dpt: str):
        self._dpt = dpt

    def __main_gw_main__(self):
        if not self._main_gw_main:
            return ""
        return self._main_gw_main
     
    def main_gw_main(self, main_gw_main: str):
        self._main_gw_main = str(main_gw_main)

    
    def __main_gw_middle__(self):
        if not self._main_gw_middle:
            return ""
        return "/" +  self._main_gw_middle

    
    def main_gw_middle(self, main_gw_middle: str):
        self._main_gw_middle = str(main_gw_middle)

    def __main_gw_sub__(self):
        if not self._main_gw_sub:
            return ""
        return "/" + self._main_gw_sub
    
    
    def main_gw_sub(self, main_gw_sub: str):
        self._main_gw_sub =  str(main_gw_sub)

    def __isReading__(self):
        if self._isReading:
            return "<"
        return ""
    
    def isReading(self, isReading: bool):
        self._isReading = isReading
    

    def build(self) -> str:
        return self.__config__() + self.__dpt__() + self.__isReading__() + self.__main_gw_main__() + self.__main_gw_middle__() + self.__main_gw_sub__() + "\""


class Builder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @property
    @abstractmethod
    def build(self) -> None:
        pass

    @abstractmethod
    def dpt(self, dpt : str) -> None:
        pass

    @abstractmethod
    def isReading(self) -> None:
        pass

    @abstractmethod
    def main_gw_main(self) -> None:
        pass

    @abstractmethod
    def main_gw_middle(self) -> None:
        pass

    @abstractmethod
    def main_gw_sub(self) -> None:
        pass

class KnxBuilder(Builder):
    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._product = KNXAddress()

    def build(self) -> KNXAddress:

        product = self._product
        self.reset()
        return product
    
    def config(self, config: str) -> None:
        self._product.config(config)

    def dpt(self, dpt: str) -> None:
        self._product.dpt(dpt)

    def isReading(self, isReading: bool = False  ) -> None:
        self._product.isReading(isReading)

    def main_gw_main(self, main_gw_main: str) -> None:
        self._product.main_gw_main(main_gw_main)

    def main_gw_middle(self, main_gw_middle: str) -> None:
        self._product.main_gw_middle(main_gw_middle)

    def main_gw_sub(self, main_gw_sub: str) -> None:
        self._product.main_gw_sub(main_gw_sub)