"""This module file is create to practice python operators
created by kamlesh on 09/07/2024 """

# a = 10
# b = 20
# c = 10
# print("id of a", id(a))
# print("id of b ", id(b))
# print("id of c", id(c))
# print("a is c", a is c)
# print("a is b", a is b)
# print("a is not c", a is not c)
# print("a is not b", a is not b)

# ls1 = [1,2,3]
# ls2 = [1,2,3]
# print("id of ls1", id(ls1))
# print("id of ls2 ", id(ls2))
# print("ls1 is ls2", ls1 is ls2)    # false ( t1 and t2 occupy different memory location even values are same)
# print("ls1 is not ls2", ls1 is not ls2)   # true
#
# print("id of ls1[1]", id(ls1[1]))
# print("id of ls2[1] ", id(ls2[1]))
# print("ls1[1] is ls2[1]", ls1[1] is ls2[1])    # true
# print("ls1[1] is not ls2[1]", ls1[1] is not ls2[1])  # false


t1 =(1,2,3)
t2 =(1,2,3)
print("id of t1", id(t1))
print("id of t2 ", id(t2))

print("t1 is t2", t1 is t2)     # true ( t1 and t2 occupy same memory location)
