""" This file is created to practice python arithmatic_operators
    created by: kamlesh r on 08/07/2024"""

# a = 5
# b = 3
#
# print(a+b)
# print(a-b)
# print(a*b)
# print("a/b", a/b)    # o/p always in float
# print("a//b floor division",a//b)  #floor division o/p = floor(a/b)   o/p is in int
# print(a%b)
# print(a**b)

# a = 1
# b = 2
# c = 10
# d = 30
#
# #PEMDAS RULE  #BODMAS
#
# print("(8+2)*3/2",(8+2)*3/2)
# print("(8+2)/2*3",(8+2)/2*3)
#
# print("(8+2)/(2*3)",(8+2)/(2*3))
# print("(8+2)/3**2+3*2",(8+2)/3**2+3*2) # 10/3**2+3*2 -->10/9+3*2 --->1.111+3*2 --->1.111+6

a = 20
b = 10
c = 15
d = 5

e = (a+b)*(c/d)  # (20+10)*(15/5) --> 30*(15/5) --> 30*3.0 -->90.0
print("value of (a+b)*(c/d) is:",e)

e = (a+b)*c/d
print("value of (a+b) * c/d is", e)

e = ((a+b)*c)/d
print("value of ((a+b)*c)/d is", e)

e = (a+b)*(c/d)
print("value of (a+b)*(c/d) is", e)

e = a + (b*c)/d
print("value of a + (b*c) / d is ", e)