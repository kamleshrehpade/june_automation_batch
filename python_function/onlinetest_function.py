"""This module file is create to practiceonline test on python functions
created by kamlesh on 22/07/2024 """


# def display_person(*args):
#     for i in args:
#         print(i)
#
# display_person(name="Emma", age="25")

def fun1(num):
    print(num)


def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d
    return inner_fun(a, b)

res = outer_fun(5, 10)
print(res)

def add(a, b):
    return a+5, b+5

result = add(3, 2)
print(result)


def display(**kwargs):
    for i in kwargs:
        print(i)

display(emp="Kelly", salary=9000)