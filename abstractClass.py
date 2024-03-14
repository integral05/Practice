from abc import *

class A(ABC):

    @abstractmethod
    def one(self):
        print("Eleven")
        pass

    # @abstractmethod
    # def two(self):
    #     pass

    # @abstractmethod
    # def three(self):
    #     pass

class B(A):
    def one(self):
        super().one()
        super().__init__()
        print("TwentyOne")

obj = B()
obj.one()














