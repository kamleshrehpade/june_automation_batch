"""This module file is create to practice python functions
created by kamlesh on 18/07/2024 """

def cal(a,b):              # function defination
    print("value of a is ", a)
    print("value of b is ", b)
    print("sum of a and b is ", a+b)
    #return a+b

# cal(10,20)  # function call to call specific function
#
# # cal(11,12)  # function call to call specific function
#
# cal(12.5, 15.2)
#
# cal('ETL','automation')

# a = float(input("enter value of a: "))
# b = float(input("enter value b: "))
# cal(a,b)

# real use cases for etl automation

# count_check(10,11)    # we cannot call the function before creation otherwise it will throw error
                   # like  NameError: name 'count_check' is not defined
                  # # always call the function after the defination of function
def count_check(source_count, target_count):
    if source_count == target_count:
        print("count is matching ")
    else:
        print("count is not matching and difference is ", source_count-target_count)

# count_check(10,11)   # always call the function after the defination of function

def calculation(a,b):          # function defination
    print("value of a is ", a)
    print("value of b is ", b)
    print("value of a+b is ", a+b)
    # return a+b
#
# sum1 = calculation(1,2)
#
# print(sum1)   # if you will not use return statement in fun defination then print statement will give o/p as None.

# the o/p of above function without return statement
# value of a is  1
# value of b is  2
# value of a+b is  3
# None

def calculation(a,b):          # function defination
    # print("value of a is ", a)
    # print("value of b is ", b)
    # print("value of a+b is ", a+b)
    return a+b

sum1 = calculation(1,2)

# print(sum1)      # o/p is 3.here which means return will store function result and then give result as 3.

def calculation(a,b):
     # print("value of a is ", a)
    # print("value of b is ", b)
    # print("value of a+b is ", a+b)
    return a + b, a - b, a * b , a/b

sum, sub, mul, div = calculation(4,6)

# print("sum ", sum)
# print("sub ",sub)
# print("mul ", mul)
# print("div ", div)

# print("sum , sub", sum , sub)

# print(calculation(5,7))  # o/p is (12, -2, 35, 0.7142857142857143) which in tuple form. # o/p of function is always in tuple form.

# functions practice questions 19/07/2024

#Write a function to check if two strings are anagrams of each other.
#Check Even or Odd
#Factorial Calculation
#Palindrome Check
# positive or negative
#nth Largest Element in an list

#Check Even or Odd
def is_even_odd(num):
    if num % 2 == 0:
        print("even number")
    else:
        print("odd number")
    return num

# is_even_odd(2)  # even number
# print(is_even_odd(2))      # 2 if we use return
# print(is_even_odd(2))      # 2 if we dont use return then the o/p will be None.

def is_even_odd(num):
    if num % 2 == 0:
        print("even number")
    else:
        print("odd number")
    return 1,2,3,'sreeni'

# is_even_odd(2)    # even number
# is_even_odd(5)   # odd number
# print(is_even_odd(2)) # (1, 2, 3, 'sreeni')  printing whatever we mention in which is used in function.
        # you can give anythinghardcoded value or o/p of function defn in return statement.

def calculation(a,b):
    return a+b,a-b,a * b,a/b

# calculation(5,10)  # we do not get anything from this fun call.because
  # we haven't use any print statement so for to store result we have used print statement.

# print(calculation(5,10))  # o/p (15, -5, 50, 0.5) after using return statement the o/p will be in tuple form.
# in return we can give a single value or multiple value its depend on you how much value you want specify accordingly into return statement.


def calculation(a,b):
    return a+b,a-b

sum1,sub1 = calculation(5,10)
# print(sum1)   # 15
# print(sub1)   # -5

# intervew question imp
def calculation(a,b):
    return 2
    return 1

sum1 = calculation(5,10)
print(sum1)   # 2 # if in fun there are two return statement then always 1st return statement will run. interview question.

