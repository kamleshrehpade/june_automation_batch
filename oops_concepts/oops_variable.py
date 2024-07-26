"""This module file is create to practice python oops concepts- oops_variables
# created by kamlesh on 25/07/2024 """

class Calc:
    pi = 3.14    # class variable/ static variable. class variable you can access from anywhere in class.

    def __init__(self,a,b):
        self.a = a   # instance variable
        self.b = b   # instance variable
        e = 500 # local variable
        print("e value is ", e)     # 500
        print(" pi value", self.pi)  # 3.14

    def add(self):     # instance method
        print("inside add pi value", self.pi)  # 3.14 you can call pi from any method it will show the value.
        # print("inside add e value ", self.e)   # AttributeError: 'Calc' object has no attribute 'e'. you cannot call local varible e to other method. only call from same method where you have created.
        c = 100  # local variable
        d = 200  # local variable
        return self.a + self.b

    def sub(self):
        return self.a-self.b


obj = Calc(4,5)
print("id of obj",id(obj))   # id of obj 1474920595120

print(obj.add())   # inside add pi value 3.14
                     # 9. this return statement value like return self.a+self.b

obj2 = Calc(4,5)
print("id of obj2", id(obj2))   # id of obj2 1474920594928


