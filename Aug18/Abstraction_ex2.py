from abc import ABC, abstractmethod


class Father(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def Loan(self):
        pass


class Son(Father):

    def Loan(self):
        print(" Son will handle")


son_obj = Son("shiva")
son_obj.Loan()
