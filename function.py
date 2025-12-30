# print("what's up")
# a=20
# b=30
# print(sum.(a,b))
# print(id(a))
# print(len(a))
# x

# def student(name): # passing argument 
#     print(f"hello,! {name}welcome to my class")
#     return f"good day,{name}"

# name="dom"
# result=student(name)
# print(result)


# def iterate_list(name:list) ->list: #  argument should be in list and ->return data type too ..
#     for valiue in name:
#         print(value)
#     return f"good fay,{name}"

# print(iterate_list(10))

# #normal
# def great_student(name,grade):
#     return f"my name is {name},i study in grade {grade}"
# print(great_student("bishwas",10))

# #positional argument
# def greatstudent(name,grade):
#     return f"my name is {name},i study in grade {grade}"
# print(greatstudent(10,"bishwas"))

# #keyword argument
# def greatstudent(name=None,grade=None):
#     return f"my name is {name},i study in grade {grade}"
# print(greatstudent(grade=10,name="bishwas"))

# #task1 
# #create a small function to calculate the volume fo a cuboid 
# def cuboid(length,breadth,height):
#     area=length*breadth*height
#     return f"The area of the cuboid is {area}"
# print(cuboid(10,20,5))


#create the list and reverse it using argument 
# def reve(list):
#     return list[::-1]

# listing=[1,2,3,4,5]
# print(reve(listing))




# rerepeat naame message multiple  time using Funtion
 #inside function
# def repeat():
#     for i in range(11):
#         print("oh! hi You are just fired")
#     return i

# print(repeat())
# #outsidee function
# def repeat(name=None):
#     n=11

    
#     for i in range(n):

#     return i
# print(repeat("hi you are just fired"))


# Recursive Function

# def fibonacci(n):
#     if n<=1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(7))

# def fibonacci(n):
#     if n == 0:        # base case
#         return 0
#     elif n == 1:      # base case
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# for i in  
# # Example usage
# print(fibonacci(5))

#------------high order functions-------__#

# def logger(func):
#     def wrapper(*args, **kwargs):
#         print(f"Function {func.__name__} is called with arguments {args}and {kwargs}")
#         result = func(*args,**kwargs)
#         print(f"Function {func.__name__} returned {result}")
#         return result
#     return wrapper

# @logger 
# def divide(x,y):
#     return x/y

# print(divide(10,2))

# def logger(func):
#     def wrapper(*args, **kwargs):
#         print(f"Arguments: {args} and {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"Result: {result}")
#         return result
#     return wrapper

# @logger
# def reverse_string(s):
#     return s[::-1]

# print(reverse_string("Python", z=3))



#---------task change in name of Function 
def multiplier(factor):
    def multiply_by_factor(number):
        return number * factor 
    return multiply_by_factor

multiplier_value= multiplier(5)
print(multiplier_value.__name__)
print(type(multiplier_value))
Result = multiplier_value(10)
print(Result)