class Master:
    def __init__(self):
        print("In Master Constructor")



class Parent1(Master):
    #def __init__(self):
    pass
        
        
class Parent2(Master):
    pass
    #def __init__(self):
     #   print("In Constructor 2")

class Parent3(Parent1,Parent2):
    def __init__(self):
        print("In Constructor 3")

class Parent4(Parent1,Parent2):
    def __init__(self):
        print("In Constructor 4")

class Parent5(Parent4,Parent3):
    def __init__(self):
        print("In Constructor 5")

obj=Parent5()
