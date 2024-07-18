"""This module file is create to practice python for loop
created by kamlesh on 16/07/2024 """

#for loop + range()
# 1. generate 0-5000 numbers sum
# # 2 . prime numbers 0-100 numbers
# # 3. even and odd numbers for 1-400 numbers
# # 4 . squares of sum of 0-100 numbers
#

r = range(10)
#
# print("type of r ",type(r))
#
# print("value of r", r)

# range(stop): Generate the numbers from 0 to stop-1.
# range(start,stop): Generates numbers from start to stop-1.
# range(start, stop, step): Generates numbrs from start to stop-1 with a step of step.

# for i in r:
#     print(i)

# r2 = range(1,10)
#
# for i in r2:
#     print(i)

#r3 = range(0, 10, 2)
# r3 = range(0, 10, 3)
#
# print(r3)      # range(0, 10, 3)  for r2 use only with for or while loop (must).
#
# for i in r3:
#     print(i)

# generate 0-100 numbers sum
#sum = n*(n+1)/2
#
# r4 = range(0,101,1)
# sum1 =0
# for i in r4:
#     sum1 = sum1 + i
# print(sum1)

# factorial of number 5

# factorial1 = 1
# for i in range(1,6):
#     factorial1= factorial1 * i
#
# print("facorial1", factorial1)

# num = int(input("enter the value:"))
# factorial = 1
# for i in range(1,num+1):
#     factorial = factorial * i
#
# print("factorial", factorial)     # 5 facorial = 120

# syntax for nested for loop #

# for i in collections:
#     statements
#     for j in collections:
#         statements
#         for k in collections:
#             statements
#             for l in collections:
#                 statements
#
# for i in range(1,5):
#     print(i)
#     for j in range(5,9):
#         print(j)

# for i in range(1,5):
#     for j in range(5,9):
#         print(i,j)

# we want 2  numbers tables
# for i in range(2, 3):
#     for j in range(1,11):
#         print(f"{i} * {j} =", i * j)
#
# if we want to find 1 to 20 tables in python then

# for i in range(1,21):
#     for j in range(1,11):
#         print(f"{i}*{j}=",i*j)

# for i in range(1,4):
#     for j in range(10,12):
#         for k in range(20,23):
#             for l in range(30,32):
#                 print(i,j,k,l)

n = int(input("enter the number of rows: "))
for i in range(1,6):
    for j in range(1,6):
        print(i,end=' ')
    print()
#
# o/p
# enter the number of rows: 5
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5

# n = int(input("enter the number of rows: "))
# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=' ')
#     print()
#
# o/p of above code
# enter the number of rows: 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5