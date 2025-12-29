# # # ##arthematic oerators 

# # # #addtition opertators 
# # # a=20
# # # b=10

# # # sum=a+b
# # # difference=b-a
# # # multiplication=a*b
# # # Division=b/a
# # # print(sum)
# # # print(difference)
# # # print(multiplication)
# # # print(Division)

# # # a=10
# # # b=20
# # # d=a%b #modulos
# # # c=a//b #floor division operators 
# # # f=a **b #exponential operators
# # # print(c)
# # # print(d)

# # # #comparision operators
# # # a==b
# # # c= a!=b #not equal to 
# # # a>b #greater than 
# # # a<b #less than 
# # # a<=b
# # # b>=a  


# # #logical operator
# # #and
# # a=True 
# # b=False
# # c=a and b # both need s to be true
# # print(c)

# # #or 
# # a=True 
# # b=False
# # c=a or b # any treurn but of the first 
# # print(c)

# # #not
# # a=True 
# # b=False
# # c=a not b # both need s to be true
# # print(c)

# #task:1
# # listing=[1,2,3,4] #true
# # set={} # False]
# # if listing and set:
# #     print('True')
# # else:
# #     print('false')


# # #task:2
# # list=[1,2,3,4]
# # if not list:
# #     print('true')
# # else:
# #     print('false')


# #assignment operator
# # a=10
# # a+=20
# # print(a)

# # b=10
# # b-=20
# # print(b)

# # c=10
# # c*=20
# # print(c)

# # d=10
# # d/=20
# # print(d)

# a=100
# a//=20
# print(a)

# b=10
# b**=2
# print(b)

# c=10
# c%=20
# print(c)
#membership operator 
#in
# a="tri"
# b="string"
# c= a in b
# print(c)

# #not in
# a="tri"
# b="string"
# c= a not in b
# print(c)

# use in operator in dictionary key or values to check the memebrship 
# a='name'
# b={'name1':'hbishwassbh'}
# c = a in b.key()
# print(c)

a={'name1':'hbishwassbh'}
if 'nam' in a.keys():
    print("true")
else:
    print("false")


# a = {'name':'samir', 'age':21}
# if 'name' in a.keys():
#     print("True")
# else:
#     print(False)

#Bitwise Operators 

a=2
b=3
print(a|b)# or 
print(a&b)# AND
print(a^b)# NOT
print(-b)  #equivalent to -(x-1)
