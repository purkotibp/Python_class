# # Advance concept of Dictionary
# # easy to serialize and deseralize 
# # json= java script oject notation
# # python native datatype is dicationary 
# # create a dictionary about the emolpyee data in nested form 


# # employee={
# #         'name':'bishwas',
# #         'name':22,
# # }
# # # get hash of first key in dicitionary 

# # print(hash('name'))
# # print(hash('name'))

# # employee['name']='shirshir'
# # print(employee).get('name')

    
# # # compehension:-loop=iterator , range 
# # iterator= current state fo being iteration
# # iterable = the one which will be itterating


# # size = 10
# # data_list=list(range(size))
# # data_dict= ((i,i) for i in range(size))

# #use list comprehemsion to create a list of prime number 
# # #list of prime numbe less than 10 

# # num= int(input("enter the number: "))
# # if num<=1:
# #     print("it is not a prime number }")

# # for i in range(2,num):
# #     if num%i==0:
# #         print("it is not prime number")
# #         break
# #     else:
# #         print("it is a prime number")

# # size=int(input("Enter number for listing in list "))
# # data_of_prime=[i for i in range(size)]


# #----------  CHECK THE TIME-COMPLEXITY ----------------#

# import  timeit
# import random
# size = 100000
# data_list=list(range(size))
# data_dict= {i:i for i in range(size)}

# search_items = [random.randint(0,size*2) for _ in range(100)] #creating a random 100 number so , that we can search 

# def search_in(container):
#     for item in search_items:
#         _ = item in container #in checks the existance of (container)
#         return None # why ? because return breaks the loop .and print only once . 
# list_time = timeit.timeit(lambda: search_in (data_list),number=1000) # "number" is how many times the iteration occurs . 
# dict_time = timeit.timeit(lambda: search_in (data_dict),number=1000)
# print(list_time) 
# print(dict_time)






