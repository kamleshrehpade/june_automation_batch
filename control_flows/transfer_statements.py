"""This module file is create to practice python operators
created by kamlesh on 17/07/2024 """

# break : if we want break iteration(for/while loop) then we will use break keyword.
# continue( skip) : if we want to skip iteration then we will use continue keyword.
# pass : will be used to write syntactically correct code when we don't have logic.

#
# for i in range(1,11):
#     if i == 7:
#         break
#     print(i)
#
# print("*"*40)    # used for showing separation of result of above and below code
#
# for i in range(1,11):
#     if i == 7:
#         continue
#     print(i)

# if we want to complete terminate for loop after certain condition is satisfied then we used break
# if we want skip specific iteration then we will use contnue keyword.

# source = None
# target = 10
# for i in range(1,10):
#     if source == None:
#         break
#     print(i)
#
# source = None
# target = None
#
# for i in range(1,5):
#     if source is None or target is None:
#         break
#     print(i)

# source = None
# Target = None
#
# source1 = 10
# target1 = 11

# for i in range(1,5):
#     if source is None or Target is None:
#         continue
#     print(i)

# for i in range(1,5):
#     if i == 2:
#         continue
#     print(i)
#
# for i in range(1,10):
#     pass
#
# for j in range(1,11):
#     pass
#
# def azure_sql_db(connection_str):
#     pass

# Python program to demonstrate
# break statement

# s = 'geeksforgeeks'
# # # Using for loop
# for letter in s:
#
# 	print(letter)
# 	# break the loop as soon it sees 'e'
# 	# or 's'
# 	if letter == 'e' or letter == 's':
# 		break
#
# print("Out of for loop")
# print()
#
# i = 0
#
# # Using while loop
# while True:
# 	print(s[i])
#
# 	# break the loop as soon it sees 'e'
# 	# or 's'
# 	if s[i] == 'e' or s[i] == 's':
# 		break
# 	i += 1
#
# print("Out of while loop")

# Python program to
# demonstrate continue
# statement

# loop from 1 to 10
# for i in range(1, 11):
#
# 	# If i is equals to 6,
# 	# continue to next iteration
# 	# without printing
# 	if i == 6:
# 		continue
# 	else:
# 		# otherwise print the value
# 		# of i
# 		print(i, end = " ")

# Python program to demonstrate
# pass statement

s = "geeks"

# Empty loop
# for i in s:
# 	# No error will be raised
# 	pass

# Empty function
def fun():
	pass

# No error will be raised
fun()

# Pass statement
for i in s:
	if i == 'k':
		print('Pass executed')
		pass
	print(i)

