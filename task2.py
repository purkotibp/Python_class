# #flatten the tuples data =((2, 3), (4, 3), (1, 5))
# data = ((2, 3), (4, 3), (1, 5))
# flat = ()
# for t in data:
#     for i in t:
#         flat += (i,)
# print(flat)

# #remove duplicate from this numbers = (1, 2, 2, 3, 3, 4, 4, 4, 5)
# numbers = (1, 2, 2, 3, 3, 4, 4, 4, 5)
# after = ()
# for i in numbers:
#     if i not in after:
#         after   += (i,)
 
# print(after)

#flattning 
# data = ((2, 3), (4, 3), (1, 5))
# flat=()
# for i in data:
#     flat+=i
# print(flat)
tupling = ((2, 3), (4, 3), (1, 5))


flatten_tuple =tuple(element for inner_tuple in tupling for element in inner_tuple)
print(flatten_tuple)




