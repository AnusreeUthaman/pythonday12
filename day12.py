#FUNCTIONS-(a block of reusable code)
#it is a block of code that can be executed multiple times from different parts of a program.

#syntax:
#def funtion_name(parameters):
    #code to be executed

#def- it is keyword that indicates the start of a function definition.

#greet()-function name

#Parameters-(used to pass information into functions)
#parameters are the variables that are defined in the function defintion and are used to receive input values when the function is called

#1.positional parameters-defined without the default valiue and must be passed in the correct position.

#2.keyword parameters-defined with the default valiue and can be passed using the parameters name.

#3.default parameters-have a default value if not provided.

#4.variable parameters-accept any number of arguments using *args or **kwargs


def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# 1.Positional parameters
greet("John", 30)#Hello, John! You are 30 years old.

#2. Keyword parameters
greet(name="John", age=30)#Hello, John! You are 30 years old.

# 3.Default parameters
def greet(name, age=30):
    print(f"Hello, {name}! You are {age} years old.")
greet("John")#Hello, John! You are 30 years old.

# 4.Variable parameters
def sum_numbers(*numbers):
    return sum(numbers)
print(sum_numbers(1, 2, 3, 4, 5))#15




#Arguments-(the values passed to a function when it is called.)

#1.positional arguments-passed in the order they are defined

#2.keyword arguments-passed using the parameters name,regardless of order.

#3.default arguments-have a default value if not provided

#4.variable arguments-accept any number of arguments using *args or **kwargs


def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")#Hello, John! You are 30 years old.

# 1.Positional arguments
greet("John", 30)#Hello, John! You are 30 years old.

# 2.Keyword arguments
greet(name="John", age=30)#Hello, John! You are 30 years old.

# 3.Default arguments
def greet(name, age=30):
    print(f"Hello, {name}! You are {age} years old.")
greet("John")

# 4.Variable arguments
def sum_numbers(*numbers):
    return sum(numbers)
print(sum_numbers(1, 2, 3, 4, 5))#15



# Argument unpacking
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")
args = ["John", 30]
greet(*args)
kwargs = {"name": "John", "age": 30}
greet(**kwargs)


#construct
#actual value
#argument


def greet():
    print("Hello")---#parameters
greet()#Hello

def greet():
    print("Hello")
greet()#Hello
greet()#Hello
greet()#Hello


def greet():
    print("Hello")
print(greet())#Hello
              #None


def greet():
    return "Hello"
print(greet())#Hello


def greet():
    print("good morning")
print(greet())#good morning
              #None



def greet(name):
    return f"Hi {name},good morning"
print(greet("anusree"))-function calling 


def greet(name):
    return f"Hi {name},good morning"
print(greet("anusree"))#Hi anusree,good morning

#positional argument
def greet(name,place):
    print(f"hi{name}")
    print(f"Are you from {place}")
greet("anusree","kerala")#-postional argument #hi anusree
                                              #Are you from kerala 

def greet(name,place):
    print(f"hi {name} are you from {place}")
greet("anusree","kerala")#hi anusree are you from kerala


def greet(name,place):
    print(f"hi{name}")
    print(f"Are you from {place}")
greet("kannur","anu")

#keyword argument
def greet(name,place):
    print(f"hi{name}")
    print(f"Are you from {place}")
greet(name="anusree",place="kerala")-#keyword argument o/p:#hi anusree
                                                           #Are you from kerala

def greet(name,place):
    print(f"hi {name} are you from {place}")
greet(name="anusree",place="kerala")#hi anusree are you from kerala







