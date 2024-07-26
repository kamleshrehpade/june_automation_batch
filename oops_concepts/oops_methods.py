"""This module file is create to practice python oops concepts- oops_methods
# created by kamlesh on 25/07/2024 """

# class Calc:
#     pi = 3.14   #  class variable
#
#     def __init__(self,a,b):
#         self.a = a    # instance variable
#         self.b = b     # instance variable
#
#     def add(self):    # instance method  # if we are using atleast one instance variable then we call method as instance method.
#         return self.a + self.b
#
#     def sub(self):    # instance method
#         return self.a - self.b
#     @classmethod
#     def area_of_circle(cls,r):    # class method. here we are using atleast one class variable then we call method as class method and we shouldn't use any instance variable.
#         return cls.pi*r*r
#
#     @staticmethod
#     def area_of_square(l,b):   # static method  # if we are not using any of class or instance variable then we call method as static method.
#         return l*b
#
#
# obj = Calc(3,6)
# print(obj.add())  # 9
#
# print(obj.area_of_circle(4))   # 50.24
#
# print(obj.area_of_square(4,5))  # 20
#
# class read_data:
#     read_nosqldb = 'nosql db config'
#
#     def __init__(self,type_of_file, type_of_db):
#         self.type_of_file = type_of_file   # instance variable  1gb
#         self.type_of_db = type_of_db     # instance variable  1gb
#
#     def read_file(self):
#         return 'file_data'
#
#     def read_db(self):
#         return 'db_data'
#
#     @classmethod
#     def read_nosqldb(cls):
#         return 'nosqldb data'


# questions from students

class Calc:
    pi = 3.14   #  class variable

    def __init__(self,a,b):
        self.a = a    # instance variable
        self.b = b     # instance variable

    def add(self):    # instance method
        self.c = 360   # inside the instance method by using self method we can declare instance variable.
        return self.a + self.b

    def sub(self):    # instance method
        return self.a - self.b
    @classmethod
    def area_of_circle(cls,r):    # class method.
        return cls.pi*r*r

    @staticmethod
    def area_of_square(l,b):   # static method
        return l*b

obj = Calc(6,7)
# print("memory of obj", id(obj))

print(obj.__dict__)   # {'a': 6, 'b': 7}  here a,b are instance varible and now we added c in add method but
                   # we haven't call add method thats why not showing in value of c in result so for that we have

print(obj.add())    # 13 # after this we can again print instance variable by below command

print(obj.__dict__)   # {'a': 6, 'b': 7, 'c': 360} now all three instance varible got from class.

         #### 3) we can declare instance variables outside of the class by using object referance variable.

obj.d = 500  # declaring instance variable outside of the class by using object referance variable.

print(obj.__dict__)    # {'a': 6, 'b': 7, 'c': 360, 'd': 500} these are instance variables.

print(obj.a)   # 6. # we can access instance variable valueoutside of class by using object reference