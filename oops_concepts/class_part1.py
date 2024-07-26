"""This module file is create to practice python oops concepts - constructor(init(self))
# created by kamlesh on 24/07/2024 """

# syntax of class
# class Name0ftheclass:
#     def __init__(self):
#         stmts
#
#     def method1(self):
#         stmts


# class Calc:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         print("hello this is constructor")
#
#     def add(self):
#         print("hello this is add method")
#         return self.a+self.b
#
#     def sub(self):
#         return self.a-self.b
#
# obj = Calc(4,5)    # hello this is constructor. which means no need to call this method explicitely it will automaticaly executed once per object
#                   ## obj is called a reference variable.
# obj.add()
#
# print(obj.add())   # 9
#
# obj2= Calc(7,8)  #  hello this is constructor. which means constuctor is automaticaly executed.
#
# obj.__init__(5,11)  # no need to call this method explicitely it will automaticaly executed once per object and if you can
#            # call this method explicitely you can call. normally no need to call this method. so here we can pass different value.
#        # so it will overrite the value 4, 5 by 5,11.
#
#
# print(obj.add())     # 16
# print(obj.sub())     # -6
#
# obj2 = Calc(7,9)
# obj3 = Calc(10,11)
#
# print(obj2.sub())    # -2


# class College:
#     def student(self):
#         print("this is student method")
#
# obj3 = College()   # no need to give any arguments it will automatically take self as variable.
#
# obj3.student()   # this is student method.

class College:
    def __init__(self):
        pass
    def __init__(self,a):
        self.a= a
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def student(self):
        print("this is student method")

# obj4 = College()    # TypeError: College.__init__() missing 2 required positional arguments: 'a' and 'b'.
             # which means if there are more number of constructor then it will take latest/last init method/constructor.

obj4 = College(6,7)  # it will run now.

obj4 = College(5)  # TypeError: College.__init__() missing 1 required positional argument: 'b'