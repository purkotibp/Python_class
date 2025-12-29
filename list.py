

# # # a=[1,2,3,4,5,6,7]
# # # #first element 
# # # print(a[0])
# # # #last element 
# # # print(a[-1])
# # # #middle element 

# # # print(a[3])

# # # #get reverst of the list
# # # print(a[::-1])

# # # a.append("hello")#append
# # # print(a)
# # # a.insert(3,"bishwas") #insert
# # # print(a)
# # # print(len(a)) #6 because len count from the first of the number 
# # # print(id(a))

# # # #task
# # # b=[1,2,3,4]
# # # b.insert(4,"bishwas")# the position is counted in indexing format . 
# # # print(b)
# # # # #due to direct printing . 

# # # print(id(b))

# # my_list=[1,2,3]
# # your_list=[4,5,6]
# # # print(my_list+your_list)
# # print(id(my_list))
# # # print(id(my_list+your_list))
# # # #OR #memory address gets changed due to concatination
# # # merge_list=my_list+your_list 
# # # print(merge_list)
# # # print(id(merge_list))

# # my_list.extend(your_list) #extend
# # print(my_list)
# # print(id(my_list))

# mylist=[4,2,6,2,6]
# mylist.sort()
# print(mylist)

# mylist.sort(reverse=True)
# print(mylist)

# mylist.reverse()

# print(mylist)

#always occurance at first in duplicate 
list=[4,8,2,3,6]
print(list.index(4))
# list.remove(4)
# print(list)

# value=list.pop()
# print(list)
value=list.pop(list.index(4))  # index first one is removes 
print(list)
#removes duplicate
set_value= set(list)
print(list(set_value))