"""This module file is create to practice python functions
created by kamlesh on 18/07/2024 """

from  test1.func1 import calc

# from python_function.function_part1 import *
# * means import all the function which are already created.
# if you want to call only one or two function mention specifically there name while import

# from python_function.function_part1 import cal ,count_check ,calulation

from python_function.function_arguments import greeting,calc

#calc(6,7)
# calc(9,8)

# cal(8,9)
# count_check(11,12)
#
# calculation(5,7)      # o/p is (12, -2, 35, 0.7142857142857143)

# date 19-07-2024 class

# greeting()    # TypeError: greeting() missing 2 required positional arguments: 'name' and 'time'
    # latest created function will call at  the time of calling function.

# greeting('Rahul')   # TypeError: greeting() missing 1 required positional argument: 'time'
#               # which means if we calling  function for different module then it will call the latest function.

greeting('Rahul',23)    # Hello Guest

calc(10,20)  # 30
