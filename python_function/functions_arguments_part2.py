"""This module file is create to practice python functions
created by kamlesh on 22/07/2024 """

# def calc(a, b):
#     print("sum of a & b is ", a + b)
#
# calc(3,4)
# def calc(a, b,c):
#     print("sum of a, b,c is ", a + b+c)
#
# calc(3,4,5)
#
# #calc(3,4,5,6) # if you want to give 4 parametrs then we have to creat
# new funcion for each increasing or decreasing parameters we have to modify fun
# for to avoi this we have to generate a function with variable arguments like * args.
# calc(2,3)

def calc(*args):     # (*args) are positional variable length arguments.
    # print(args)
    # print("type of args ", type(args))
    sum=0
    for i in args:
        sum= sum+i
    print(f"sum of {args} is ", sum)

# calc(3,4)  # sum of (3, 4) is  7
# calc(3,4,7,6,7,8,9,9,23,45)  #  positional variable length arguments.
# calc(3,4,7,6,7,8,9,9,23,45,23654,258963,123654,789654)    # 1196046
# calc(5)    # sum is 5. it will accept any no of arguments in only single function defination.
# calc()    # sum of () is 0.

def calc(*args):     # (*args) are positional variable length arguments.
    # print(args)
    # print("type of args ", type(args))  # type of args  <class 'tuple'>
    sum=0
    for i in args:
        sum= sum+i
    return sum    # here return will store o/p of function calc. and return that in print statement while calling fun.

sum_out = calc(3,4,7,6,7,8,9,9,23,45)
# print("sum_out ", sum_out)    # sum_out  121
#
# print(calc(3,4,7,6,7,8,9,9,23,45))  # 121
# print(calc(3,4) )         # 7

def calc(**kwargs):   # keyword variable lenth arguments
    print(kwargs)
    print("type of kwargs ", type(kwargs))  # type of kwargs  <class 'dict'>
    sum1= 0
    for i in kwargs.values():
        sum1 = sum1 + i
    print(f" sum of {kwargs} ", sum1)

# calc(10,20,30,20,30)  # TypeError: calc() takes 0 positional arguments but 5 were given.
              # becz we are given kwargs means we have to specify keyword variable length arguments
                # at the time of calling function.
# calc(a=10,b= 20, c= 20,d=30)   #  sum of {'a': 10, 'b': 20, 'c': 20, 'd': 30}  80


def greeting(**kwargs):
    print(kwargs)     # {'name': 'sreeni', 'message': 'how are you'} dictionary
    print_message = ('')
    for i in kwargs.values():
        print_message = print_message + ' '+ i
    print(print_message)

# greeting(name= 'sreeni',message = 'how are you')  #  sreeni how are you
# greeting(name= 'sreeni',message = 'how are you', message2 = 'good morning')  # sreeni how are you good morning.


def f(arg1, arg2, arg3=4, arg4=8):    # arg3,arg 4 are default arguments.
     print(arg1, arg2, arg3, arg4)


# f(3,2)         # here 3,2 are positional arguments
# f(10,20,30,40)    # 10,20,30,40 are positional arguments.
# f(25,50,arg4=100)   # 25, 50 are positional arguments. 4 is default arguments. arg4=100 is keyword arguments
# f(arg4=2,arg1=3,arg2=4)   # 2,3,4 keyword word args, arg3=4 is default arg

# f()          # TypeError: f() missing 2 required positional arguments: 'arg1' and 'arg2'
#f(arg3=10,arg4=20,30,40)    # SyntaxError: positional argument follows keyword argument
# f(4,5,arg2=6)           # TypeError: f() got multiple values for argument 'arg2'
# f(4,5,arg3=5,arg5=6)    # TypeError: f() got an unexpected keyword argument 'arg5'
# f(4,5,5,arg3=2)       # TypeError: f() got multiple values for argument 'arg3'


