fileObj = open("C:/Python Programs/GITHUB/Practice/C2W.txt","r+")
print(fileObj.read())
print(type(fileObj))
print(type(open))
print(type(fileObj.read))



class A:
    def __init__(self):
        pass

    def add(self):
        self.a=10

obj=A()
obj.add()
print(type(A))
print(type(obj))
print(type(obj.add))
print(type(obj.__init__))



