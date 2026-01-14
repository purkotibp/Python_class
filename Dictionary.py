# # # #dictionary is a mutable data type which is build and stores key balue pairs . 
# # # empty_dict={}
# # # print(empty_dict)
# # # print(type(empty_dict))

# # # # onluy immutanble data type can be dictionary's key and ist be unique 
# # # first_dictionary={'name':'bishwas','age'=22}
# # # print(first_dictionary.value())
# # # print(first_dictionary.keys())



# #---- hashing 
# first=hash('age')
# second={'name':'bishwas','age':26}
# # print(second)

# # # print(second.items())

# # # for key,value in second.items():
# # #     print(key)
# # #     print(value)

# # # accessing elements form dictinary
# # name = second['name'] #hard coded fetching (if sure it exists)
# # print(name)

# # #accessing using get() method
# # name= second.get('name') # soft coded fetching (if not sure )
# # print(name)

# # # qustiin
# # dict_1 = {'name':'abcd','age':26}
# # #is- used ofmemory address checking . 
# # dict_2={'age':26,'name':'efgh'}
# # print(id(dict_1))

# # print(dict_1==dict_2)
# # print(id(dict_1==dict_2))
# # print(dict_1 is dict_2)
# # print(id(dict_1 is dict_2))

# #merging the dictionaries 
# #1. union merge 
# # result_dict = dict_1 | dict_2
# # print(result_dict)
# # print(id(result_dict))
# # duplicate name is there the right hand(dict2 ) that will be in union . not the first one . like "name"

# # 2. update merge 
# # dict_1.update(dict_2)
# # print(dict 
# # print(id(dict_1))

# #3. intersection merge 
# dict_1 = {'name':'abcd','age':26}
# #is- used ofmemory address checking . 
# dict_2={'age':26,'name':'efgh'}
# # result_dict =dict_2 and  dict_1 # no intersection megre we can do only and that is +
# # print(result_dict)
# # print(id(result_dict))

# #4. keyword arguments merge
# result_dict={**dict_1,**dict_2}
# print(result_dict)

# #5. Removing key value 
# dict_3 = {'name':'bishwas','age':26}
# #value =dict_3.pop ('name')
# #print(values)
# #print(dict_3)
# value =dict_3.popitem()
# print(value)
# print(dict_3)

# #key value 
# dict_3['name']='Ram'
# print(dict_3)


