"""This module file is create to practice python oops concepts- self_keyword
# created by kamlesh on 24/07/2024 """

# class Calc:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#         print("memory of self ", id(self))
#
#     def add(self):
#         print("hello this is add method")
#         return self.a+self.b
#
# obj =Calc(4,5)  # memory of self  1786803404704

# print("memory of obj", id(obj))   # memory of obj 1786803404704

   # ## memory of self and current obj is always same which means self variables like(a,b) are pointed to current object like(obj).
    ## self keyword is alwyas pointed to current object memory.

# print(obj.__dict__)   # {'a': 4, 'b': 5}. this will print all the variables available in current object (obj).
         # which means all self variables here(a,b) are stored into current object memory here(obj).

# print(obj.add())   # 9 which is o/p of line--> return self.a+self.b in add method.

# within the class to access current object elements(variables) we use self. for eg self.a+self.b

### for self. We can use any name like a,b,c,kelf, delf, kamlesh etc
### but recommended ot use self.
##example below
class Calc:
    def __init__(kelf,a,b):
        kelf.a = a
        kelf.b = b
        print("memory of self ", id(kelf))

    def add(kelf):
        # print("hello this is add method")
        return kelf.a+kelf.b


obj1 = Calc(9,8)      # memory of self  2632739798704

print("memory of obj1",id(obj1))   # memory of self  2632739798704

print(obj1.__dict__)   # {'a': 9, 'b': 8}

print(obj1.add())   # 17