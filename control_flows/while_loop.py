"""This module file is create to practice python operators
created by kamlesh on 17/07/2024 """

import timeit
# syntax
#  while condition:
#      statements
#
# while True:
#     print("inside while loop")  # printing "inside while loop" infinite times.
#                           # for to stop this we have to fail our condition which means for limiting
                      # we should fail our  condition at some where.

# num = 10
# while num <= 10:
#     print(num)    # print will 10 infinite times

# num = 10
# while num <= 10:
#     print(num)    # print will 10 infinite times so for to break/stop we give limit to this by adding one code in next line.
#     num = num+1  # num = 11 which means break the condition comes out or terminate from loop.

# num = 0
# while num <= 10:
#     print(num)
#     num = num+1
#
# print("hello this is after while loop")
#
# num = 0
# while num <= 10:
#     print(num)
#     if num == 5:
#         break
#     num = num+1

# num = 5
# while num > 0:
#     print(num)
#     num = num-1


# generally for_loop is faster than while_loop it depend on condition but
# ussually for_loop is faster than while_loop.

# Function to sum numbers using a for_loop
def sum_with_for_loop(n):
    total = 0
    for i in range(n):
        total += i
    return total

# Function to sum numbers using a while loop
def sum_with_while_loop(n):
    total = 0
    i = 0
    while i < n:
        total += i
        i += 1
    return total

# Measure execution time for the for loop
print("Time taken by for loop:", timeit.timeit(lambda: sum_with_for_loop(1000000000), number=1))

# Measure execution time for the while loop
print("Time taken by while loop:", timeit.timeit(lambda: sum_with_while_loop(1000000000), number=1))





