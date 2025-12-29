# # t1=(1,2,3)
# # t2=("python",3.14,True)
# # print(t1)
# # print(t2)

# #creating a tuples
# # #emply tuples
# # empty=()
# # print(empty)
# # print(type(empty))

# #single Element Tuple (comma is mandatory)
# # single=(10,)
# # print(type(single))
# # print(single)

# # #without comma-> NOT. a tuple 
# # not_tuple = (10)
# # print(type(not_tuple))
# # print(not_tuple)

# ##-------------Tuples exercise -------------------##
#     #create a tuples of 10 elements 
# #method1 (list_comphrension)
# tuple1=(1,2,3,4,5,6,7,8,9,10)
# # print("the elements of the 10 in tuples ",tuple1)
# #     #multiply the each elements at multiple of 2 ])
Mltiplied_elements = (i * 2 for i  in tuple1)
Result_tuple = tuple(Multiplied_elements)
print(Result_tuple)
#method2
# # result_tuple=()
# # for element in tuple1:
# #     result_tuple+=(2,)
# #     print(result_tuple)

# #prove it : tuple is immutable 
# print(id(tuple1))
# tuple1+=(60,10)
# print(id(tuple1))


#----------------
# t1=(23,"python","bishwas",3.12,["list",21,'apple'])
# print(t1)
# # t1[4].append("87")
# t1[4].insert(2,"hello")# inserstion inside the list 

# print(t1)
# mytuple=99# removing the selected list 
# t1[4][0]=mytuple
# print(t1)'

#accessing the dept value and print
data = ((1,2),(3,4),(5,(1,2)))
depth=data[2][1][1]
print(depth)