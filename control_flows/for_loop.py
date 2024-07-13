"""This module file is create to practice python for_loop
created by Kamlesh on 12/07/2024 """

# ls = [1, 2, 3, 4, 5]
# ls_squares = []
#
# for i in ls:
#     print("i value is:", i)
#     ls_squares.append(i * i)
#
# print(ls_squares)

# mul = 1
ls = [1, 2, 3, 4, 5]
# for i in ls:
#     mul = mul * i
#
# print("mul ", mul)

# sum = 0
# for i in ls:
#     sum = sum + i
#
# print("sum ", sum)

# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   #---list
# ls = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}   #-- set
# ls = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)      #-- tuple
#
# even_sum = 0
# odd_sum = 0
# for i in ls:
#     if i % 2 == 0:
#         even_sum = even_sum + i
#     else:
#         odd_sum = odd_sum + i
#
# print("even sum ", even_sum)
# print("odd sum ", odd_sum)
# print("total sum", even_sum + odd_sum)

#vowels- a,e,i,o,u
#str1 = "sky"
# str1 = "ETL Automation"
# for i in str1.lower():
#     if i in ['a','e','i','o','u']:
#         print("vowel is present")
#         break
#     else:
#         print("vowel is not present")
#         break

str1 ="ETL Automation"   #etlaUTOMATION
#str1 ="Sky"  #"sKY o/p
str2 =" "
for i in str1:
    if i.islower():
        str2= str2 + i.upper()
    elif i.isupper():
        str2 =str2 + i.lower()

print("str2",str2)

