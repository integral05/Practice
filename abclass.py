from abc import *

class Parent(ABC):

    def __init__(self):
        print("In Parent Class Constructor")
        # self.x=10
        # self.y=20

        super().__init__()

    @abstractmethod
    def anymethod(self):
        pass

    # def conmethod(self):
    #     print(self.x)
    #     print(self.y)


class Child(Parent):

    def __init__(self):
        print("In Child Constructor")

        super().__init__()

    def anymethod(self):
        p=100
        q=200


obj=Child()
print(type(Child))
print(type(Parent))
print(Child.__mro__)
# obj.conmethod()


