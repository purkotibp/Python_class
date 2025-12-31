# # print("what's up")
# # a=20
# # b=30
# # print(sum.(a,b))
# # print(id(a))
# # print(len(a))
# # x

# # def student(name): # passing argument 
# #     print(f"hello,! {name}welcome to my class")
# #     return f"good day,{name}"

# # name="dom"
# # result=student(name)
# # print(result)


# # def iterate_list(name:list) ->list: #  argument should be in list and ->return data type too ..
# #     for valiue in name:
# #         print(value)
# #     return f"good fay,{name}"

# # print(iterate_list(10))

# # #normal
# # def great_student(name,grade):
# #     return f"my name is {name},i study in grade {grade}"
# # print(great_student("bishwas",10))

# # #positional argument
# # def greatstudent(name,grade):
# #     return f"my name is {name},i study in grade {grade}"
# # print(greatstudent(10,"bishwas"))

# # #keyword argument
# # def greatstudent(name=None,grade=None):
# #     return f"my name is {name},i study in grade {grade}"
# # print(greatstudent(grade=10,name="bishwas"))

# # #task1 
# # #create a small function to calculate the volume fo a cuboid 
# # def cuboid(length,breadth,height):
# #     area=length*breadth*height
# #     return f"The area of the cuboid is {area}"
# # print(cuboid(10,20,5))


# #create the list and reverse it using argument 
# # def reve(list):
# #     return list[::-1]

# # listing=[1,2,3,4,5]
# # print(reve(listing))




# # rerepeat naame message multiple  time using Funtion
#  #inside function
# # def repeat():
# #     for i in range(11):
# #         print("oh! hi You are just fired")
# #     return i

# # print(repeat())
# # #outsidee function
# # def repeat(name=None):
# #     n=11

    
# #     for i in range(n):

# #     return i
# # print(repeat("hi you are just fired"))


# # Recursive Function

# # def fibonacci(n):
# #     if n<=1:
# #         return n
# #     else:
# #         return fibonacci(n-1) + fibonacci(n-2)

# # print(fibonacci(7))

# # def fibonacci(n):
# #     if n == 0:        # base case
# #         return 0
# #     elif n == 1:      # base case
# #         return 1
# #     else:
# #         return fibonacci(n-1) + fibonacci(n-2)
# # for i in  
# # # Example usage
# # print(fibonacci(5))

# #------------high order functions-------__#

# # def logger(func):
# #     def wrapper(*args, **kwargs):
# #         print(f"Function {func.__name__} is called with arguments {args}and {kwargs}")
# #         result = func(*args,**kwargs)
# #         print(f"Function {func.__name__} returned {result}")
# #         return result
# #     return wrapper

# # @logger 
# # def divide(x,y):
# #     return x/y

# # print(divide(10,2))

# # def logger(func):
# #     def wrapper(*args, **kwargs):
# #         print(f"Arguments: {args} and {kwargs}")
# #         result = func(*args, **kwargs)
# #         print(f"Result: {result}")
# #         return result
# #     return wrapper

# # @logger
# # def reverse_string(s):
# #     return s[::-1]

# # print(reverse_string("Python", z=3))



# #---------task change in name of Function 
# # def multiplier(factor):
# #     def multiply_by_factor(number):
# #         return number * factor 
# #     return multiply_by_factor

# # multiplier_value= multiplier(5)
# # print(multiplier_value.__name__)
# # print(type(multiplier_value))
# # Result = multiplier_value(10)
# # print(Result)


# #--------map Function-------#
# # built in higher order functions map,filter, reduce 
# # def square(num):
# #     return num **2 
# # number = [1 ,2,3,4,5]
# # squared_number = map(square, number)
# # print(list(squared_number))

# #make divisible by 2 and make it true 
# # def divisible(num):
# #     if (num%2==0):
# #         return True
# #     else:
# #         return False

# # number = [1 ,2,3,4,5]
# # divisible_number = map(divisible, number)
# # print(list(divisible_number))

# # make String Uppercase using high order function

# # def higher(Strings):
# #     return Strings.upper()


# # String=["bishwas,hari,ram,sita"]
# # high=map(higher,String)
# # print(list(high))



# # #find the sum of each nested list and return true or false if sum is greater thjan 10 using map function 
# # def summed(sublist):
    
# #     if sum(sublist)>10:
# #         return True
# #     else:
# #         return False



# # nested_list = [[1,2,3],[4,5],[6,7,8,9]]
# # sum_list=map(summed,nested_list)
# # print(list(sum_list))

# #------------------Filter Function _-----------#

# # def is_even(num):
# #     return num%2==0
# # number = [1,2,3,4,5,6]
# # even_number=filter(is_even,number)
# # print(list(even_number))

# #filter out the words which have length greater than 3 
# # def filteration(string):
# #     return len(string)<=3

# # string=["hello","world","des","rty","tyuio"]
# # filter_string=filter(filteration,string)
# # print(list(filter_string))

# #

# ##___ method 2---------#
# # #sends filtering using dictionary into list 
# # data ={
# #     'name':'alisha',
# #     'name':'bishwaw',
# #     'name':'apple',
# #        }
# # def name_length(item):
# #     return len(item['name'])>3

# # filter_data=filter(name_length,data)
# # print(dict(filter_data))





# # reduce function importing 
# from functools import reduce

# def add(x,y):
#     return x + y 
# number = [1,2,3,4,5]
# sum_of_numbers=reduce(add,number)
# print(sum_of_numbers)


# # find the maximum number from the list using reduce function 
# from functools import reduce
# def max(x,y):
#     if(x>y):
#         return x
#     else:
#         return y


# numbers=[1,65,3,4,5,6,3.5,52,43]
# max_number=reduce(max,numbers)
# print(max_number)