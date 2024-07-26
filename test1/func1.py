"""This module file is create to practice python functions
created by kamlesh on 18/07/2024 """

# projects
#    package1
#       modules1
#          functions1,2,3
#    package2
#       modules2
#          functions 4,5,6

# def calc(a,b):
#      print(f"sum of a and b is ",a + b)
#      print(f"substraction of two numbers ", a-b)
#      print(f"multiplication of two numbers ", a * b)
#      print(f"division of two numbers ", a/b)
#
# calc(6,7)

def calc(a,b,type):
     if type == 'add':
        print(f"sum of two numbers is ",a + b)
     elif type == 'sub':
       print(f"substraction of two numbers ", a-b)
     elif type == 'mul':
        print(f"multiplication of two numbers ", a * b)
     elif type =='div':
       print(f"division of two numbers ", a/b)
     else:
          print("incorrect type of calculation")

calc(10,20,'add')

