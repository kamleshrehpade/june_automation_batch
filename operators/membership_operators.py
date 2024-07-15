"""This module file is create to practice python operators
created by kamlesh on 09/07/2024 """

# membrship operators used on collection and order sequencing datatype like
# string, list , tuple, dictinary, set , frozenset

# str1 = 'ETL Automation'
#
# print("ETL in str1 ", 'ETL' in str1)  # True
# print("Auto in str1 ", 'Auto'in str1)    # True
# print("auto in str1 ", 'auto'in str1)  # False
# print("E in str1 ", 'E' in str1)     # True
# print("'S' in str1", 'S' in str1)     # False
#
# print("'E' not in str1 ", 'E'  not in str1)     # False
# print("'S' not in str1", 'S' not in str1)     # True

# ls1 = [1, 2, 3, 4]
#
# print(" 2 in ls1 ", 2 in ls1 )     # True
# print ("5 in ls1 ", 5 in ls1 )    # False
#
# print(" '3' in ls1 ", '3' in ls1 )   # False becoz '3' is string here  not int
# print(" 3 in ls1 ", 3 in ls1 )      # True int 3 is present in ls1
#
# ls2 = [1, 2, 3, [4, 5, 6]]
#
# print("[4, 5 ,6 ] in ls2 ", [4, 5, 6] in ls2)       # True
#
# ls1 = [1, 2, 3]
# ls2 = [1, 2, 3]
#
# print(" ls1 in ls2 ", ls1 in ls2 )  # false here values are same but entire list ls1 is not present in ls2.
# print(" ls1 in ls2 ", ls1 is ls2 )  # false  # both list have diff memory location
# print(" ls1 == ls2 ", ls1 == ls2)    # True
#
# ls1 = [1, 2, 3]
# ls2 = [1, 2, 3,[ 1,2, 3]]
#
# print(" ls1 in ls2 ", ls1 in ls2)  # True becoz ls1 = [1,2 3]complete list is present ls2.
#
# d1 = { 1:'ETL', 2: 'Automation', 3:'testing'}
#
# print(" 1 in d1 ", 1 in d1)   # True   # syntax - search for only keys
# print("3 in d1 ", 3 in d1)   # True
#
# print(" ETL in d1 ", 'ETL' in d1)   # False
#
# print(" d1. values ", d1.values())   #  dict_values(['ETL', 'Automation', 'testing'])
# print(" 'ETL in d1.values()", 'ETL' in d1.values())   # True  # search for values
# print("'testing' in d1.values() ", 'testing' in d1.values())   # True
#
# print(" 1 in d1.keys() ", 1 in d1.keys())   # True
# print(" 5 in d1.keys() ", 5 in d1.keys())   # False
#
# d1 = { 1:'ETL', 2: 'Automation', 3:'testing'}
# d2 = { 1:'ETL', 2: 'Automation', 3:'testing'}
#
# print("id of d1 ", id(d1))     #   memory location
# print("id of d2 ", id(d2))    #  memory location
# print(" d1 is d2 ", d1 is d2)   # False becoz both have diff memory location
# print(" d1 == d2 ", d1 == d2)   # True


d1 = { 1:'ETL', 2: 'Automation', 3:'testing'}
d2 = { 1:'ETL', 2: 'Automation', 4:'testing'}

print(" d1 is d2 ", d1 is d2)   # False becoz both have diff memory location
print(" d1 == d2 ", d1 == d2)  # False becoz key values are diff in d1 and d2

