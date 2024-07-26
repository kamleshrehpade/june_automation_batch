"""This module file is create to practice python functions name space
# created by kamlesh on 23/07/2024 """
#
# import builtins
#
# #list all built-in functions and exceptions
# print(dir(builtins))
#
# x = 'global'
# y = 100
#
# print("global variables outside of function",globals())
# print("local variables outside of function",locals())
#
# def outer_function():
#     global a
#     a = 10
#     b = 20
#     c = 30
#     print("global variables inside of function",globals())
#     print("local variables inside of function", locals())
#     print("x value", x)
#     print("y value ", y)
#     print("b value ", b)
#
#     def inner_function():
#         d = 137
#         c = 167
#         print("global variables inside of inner function",globals())
#         print("local variables inside of inner function ", locals())
#         print("d value ", d)
#         print("x,y,a ", x,y,a)
#         print("c value ", c)
#
#     inner_function()
#     # print(" d value ", d) # throws error because d is local variable for only inner function.
#              # so you can print value of d only inside function. not ouside of inner function
#              # otherwise it will throw error.
#
# outer_function()
# print("a value outside of function",a)    # 10 becoz its global variable here
# print("b value outside of fn ", b)  # throws error # NameError: name 'b' is not defined. becoz we call b outside of outer function.
#
# z = 200
# print("global variables outside of function", globals())
# print("local variables outside of function", locals())

a = 100
b = 20
e = 31
def out_function():
    a = 24
    c= 21
    print("global variables outside function",globals())  # 'a': 100, 'b': 20  # for to confuse they will ask
                                    # does it overrite no its not overrite. becoz a = 24 is local
                                    # variable for out_function and a= 100 is global varible forout fun.
    print("local variables outside of function",locals())  # {'a': 24, 'c': 21}
    print("e value ", e)    # 31

    def inner_function():
        print("value of a is", a)  # 24  # if a is not available in inner function then a is taken from enclosing space.
        d = 45
        e = 23
        print("e value", e)    # 23
        print("global variables outside of function", globals())   # 'a': 100, 'b': 20, 'e': 31
        print("local variables outside of function", locals())    # { 'd': 45, 'e': 23}
    inner_function()


out_function()
# print("a value ", a)  # 100 which is global.
print(" e value",e)   # 31