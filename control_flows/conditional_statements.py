# this module file is create to practice python conditional_statements
# created by kamlesh on 10/07/2024  #

# name = 'sreeni'
# print("name is ", name)
#
# name2 = input("enter the name:")
# print("name2 is ",name2)
# print("type of name2 ",type(name2))
#
# age = float(input("enter the age value"))  # input method convert your input data as string
# print("age is ",age)
# print("type of age is ",type(age))

# if
# if-else
#if -elif
#if-elif-else


# if syntax
#
# if condition:
#     statements
# 4 spaces or 1 tab  we call indentation
# name = input("enter the name:")
# if name =='Sreeni':
#     print("hellow Sreeni , Good morning")

#if-else syntax
# if condition:
#     statements
# else:
#     statements

# name = input("enter name:")
# if name =='Sreeni':
#     print("Hellow Sreeni, Good morning")
# else:
#     print("Hellow Guest, Good morning")
#
# #if-elif syntax
# if condition:
#     statements
# elif condition:
#     statements
#
# name = input("enter name:")
# if name == 'Sreeni':
#     print("Hello Sreeni, Good Morning")
# elif name == 'Rahul':
#     print("Hello Rahul,Good morning")
# elif name == 'Ravi':
#     print("Hello Ravi ,Good morning")

#if -elif -else syntax
#
# if condition:
#     statement
# elif condition:
#     statement
# else:
#     statements

# name = input("enter name: ")
# if name == 'Sreeni':
#     print("hello Sreeni, good Morning")
# elif name == 'Rahul':
#     print("hello Rahul, good morning")
# elif name =='Ravi':
#     print("hello Ravi , Good morning")
# else:
#     print("hello Guest, Good morning")

# use cases of if-elif-else

# source - csv,json,parquet, txt, .dat, oracle, sqlserver, snowflake etc
# target - csv, json, parquet, txt, .dat, oracle, sqlserver, snowflake etc

# source_type = input("enter your source:").lower()
#
# if source_type == 'csv':
#     print("This is code to read csv files")
# elif source_type == 'json':
#     print("this is code to read json file")
# elif source_type == 'parquet':
#     print("this is code to read parquet file")
# elif source_type =='txt':
#     print("this is code for to read txt files")
# elif source_type == 'oracle':
#     print("this is code to read data from oracle db")
# elif source_type == 'sqlserver':
#     print("this is code for to read data from sqlserver db")
# else:
#     print("enter correct source, currently this code will handel csv, json, parquet,txt,oracle_db")

#user enters number and o/p should be displayed with characters 1-one, 2-two, 3-three --etc

# number = int(input("enter the number:"))
# print("type of number",type(number))
#
# if number == 0:
#     print("entered number is zero")
# elif number == 1:
#     print("entered number is one")
# elif number == 2:
#     print("entered number is two")
# elif number == 3:
#     print("entered number is three")
# elif number == 4:
#     print("entered number is four")
# elif number == 5:
#     print("entered number is  five")
# elif number == 6:
#     print("entered number is six")
# elif number == 7:
#     print("entered number is seven")
# elif number == 8:
#     print("entered number is eight")
# elif number == 9:
#     print("entered number is nine")
# elif number == 10:
#     print("entered number is ten")
# else:
#     print("entered number is not between 0 and 10, please retry")


# take a number using input method and
# print if num>0 as positive number,
# elif number = 0 print as zero
# else negative number

# number = int(input("enter number:"))
#
# if number > 0:
#     print("positve number")
# elif number == 0:
#     print("Zero")
# else:
#     print("negative number")

# take age using input method and
# print if age>=18 as eligible for vote
# else print not eligible and you will be eligible for vote in x years ( x should 18-entered age)

age = int(input('enter age value:'))
x = 18 - age

if age >= 18:
    print("you are eligible for vote")
else:
    print("you are not eligible for vote and you will be eligible for vote in x years:" , x)


