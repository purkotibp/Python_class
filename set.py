# # a={10,20,30.40,50}
# # print("homogenous elements",a)
# # print(type(a))
# # b={10,"hello",3.14,True}
# # print("heterogenous element" ,b)
# # print(type(b))

# #---empty set
# empty_set =set() #{} creates a dictionary , not a set 
# print(empty_set)
# print(type(empty_set))
# empty_set.add(3)
# print(empty_set)
# empty_set.update([5,7,5,8,9,1])
# print(empty_set)

# # empty_set.remove(1) # error if element not found
# # print(empty_set)
# # empty_set.discard(0) # error doesnot occur oif the element is not found 
# # print(empty_set)

# removed=empty_set.pop() # pop removes the random number in the set . 
# print("removed",removed)
# print(empty_set)


# #set with duplciate values duplicate are removed automatically)
# # dup ={1,2,3,3,4,5}
# # print(dup) #no duplicate is prined in set . 
# # print(type(dup))
 
# #index calling in set gives error
# # set={10,20,40,30}
# # print(set[2])


#---------set method________-#
# A={1,2,3,5,7,8}
# B={2,4,5,6,7,8,10}

# print("intersection :",A.intersection(B))
# print("Differences A-B :",A.difference(B))
# print("Differences B-A:",B.difference(A))
# print("symmetric Differences:",A.symmetric_difference(B))
# print("\n")
# print(A|B)
# print(A-B)
# print(B-A)
# print(A^B)


#----------SET comparsion
# C={2,3}
# D={2,3,4,5}

# print(C.isdisjoint(D))
# print(D.issuperset(C))
# print(C.isdisjoint({9,7}))

#------Frozenset-----#
fs=frozenset([1,3,2]) # it is Immutable version of the set 
print(fs)
print(type(fs))
# ds=fs[1]
# print(ds)# indexing does not work in this . 
# fs.add(2) 3 # add function doesn't work 
ds=fs.add(2)
print(fs)
