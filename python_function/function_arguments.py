"""This module file is create to practice python functions
created by kamlesh on 19/07/2024 """

def greeting():        # in function defination parameters/ arguments are optional.
    print(" Hello Guest, Good morning ")

# greeting()   # o/p is Hello Guest, Good morning. which means arguments are optional while call the function.

def greeting(name):    # in function defination we use name as argument then while calling function we have to specify argument.
    if name == 'Rahul' :
        print(" Hello Rahul , Good morning")

# greeting()    # TypeError: greeting() missing 1 required positional argument: 'name'

# greeting('sreeni')   # o/p showing nothing because  in if condition is failing then it will not showing anything.
# greeting('Rahul')   #  Hello Rahul , Good morning

def greeting(name):
    if name == 'Rahul' :
        print(" Hello Rahul , Good morning")
    else:
        print(" Hello Guest , Good morning")

# greeting('sreeni')     # o/p is Hello Guest , Good morning

# greeting(name = 'sreeni')  # Hello Guest , Good morning

# greeting(name='Rahul')     # o/p is   Hello Rahul , Good morning.

def greeting(name, time):   # function def with two arguments
    if name == 'Rahul' and time <= 12 :
        print(" Hello Rahul, good morning")
    elif name =='Rahul' and time > 12 and time <=16:
        print(" Hello Rahul , Good Afternoone ")
    elif name == 'Rahul' and time > 16 and time <= 20:
        print("Hello Rahul , Good evening ")
    else:
        print("Hello Guest")

# greeting('Rahul')   # TypeError: greeting() missing 1 required positional argument: 'time'
          # because for calling function greeting('Rahul') the latest defination of call function having two arguments.

greeting('Rahul', 11)  # Hello Rahul, good morning

greeting('Rahul',23)   # Hello Guest

def calc(a,b):
    print("value of a ", a)
    print("value of b ", b)
    print("sum of a and b is ", a+b)


# calc(5,6)  # here 5, 6 are Positinal arguments and order is mandatory for positinal arguments. o/p is 11.function call with positinal arguments
# calc(a =10 , b= 20)  # here a=10 and b=20 are keyword arguments and order is not mandatory for keyword arguments. o/p is 30.function call with keyword arguments
# calc(b = 20 , a= 5)   # here order is not mandatory becoz function having keyword arguments. o/p is 25.
# calc(10, b=20)   # 10 is positinal argument and b= 20 is keyword arguments. it will run and o/p is 30.
# calc(a=10, 20)     # a=10 is keyword arg and 20 is positional arg. it will not run.
                 # we always need to provide keyword arg after positional argumrents.
                 # o/p is SyntaxError: positional argument follows keyword argument.

# calc(10,a=20)  #  TypeError: calc() got multiple values for argument 'a'.
# calc(b=20, 10)   # SyntaxError: positional argument follows keyword argument.


def calc(a,b,c=0,d=-1):       # here c and d are default parameters/argument.
    print("value of a ", a)
    print("value of b ", b)
    print("value of c ", c)
    print("value of d ", d)
    print("sum of a,b,c,d ", a+b+c+d)

# calc(10,20)  # 29 # c and d will be taken from function defination if you are not provided then.

# calc(10,20,100,200) # 330 # c and d values will be taken from fn call. which means it will overrites the default value if specify in fn call.
calc(10,20,d=200)    # 230  c=0 becoz default arg
calc(10,20,200)  # 229   d=-1 default arg