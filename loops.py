# # # # for x in range(2,11,2):
# # # #     print(f"even number:{x}")


# # # # while "condition":
# # # #     "do something"
# # # #     ""condition change"


# # # # for i in range(10):
# # # #     print(i)
# # # #     if i%2==0:
# # # #         print(f"even number:{i}")
# # # #         continue 
# # # #     print(f"odd number :{i}")


# # # # task1
# # # # b=" 5"
# # # # for i in range(10):
# # # #     if b==4:
# # # #         break
# # # #     print(b)


# # # # a=10
# # # # for i in range (11):
# # # #     if(i == "5"):
# # # #         break
# # # #     print(i)

# # # # #task2
# # # # list=[10,20,30,"bishwas",3.14,None]
# # # # for i in list:
# # # #     if (i==None):
# # # #         print("Invalid")
# # # #         break
# # # # print(i)



# # # #make a list of integer and find the smallest number using loop conditon from the given 
# # # a= [60,20,30,40,50,50]
# # # smallest = a[0]
# # # for i in range(1, len(a)): 
# # #     if(i<a):
        

# # # list = [2,5,8,1,5,6]
# # # sum=0
# # # for i in list:
# # #     sum+=i
# # # print(sum)

# # # #bubble sort 
# # # list=[10,60,22,40,4,7,2]
# # # n=len(list)
# # # for i in range(n):
# # #     for j in range(0,n-i,1):
# # #         if list[j]>list[j+1]:
# # #             list[j],list[j+1]=list[j+1],list[j]
# # # print(list)
# # # print(f"{list[0]}")
# # # print (f"{list[i]}")
# # # #time complexity 
# # # linear 0(n)
# # # n**2-c (in 2 nested loop)

# # #find max and min . 7,56,98,23,53,12,33,]
# # a= [1,7,56,98,23,53,12,33,]
# # infinite_low_number= float('-inf')
# # infinite_high_number= float('inf')

# # max_value =float('-inf')
# # for n in a:
# #     if n>max_value:
# #         max_value=n
# # print(max_value)


# # min_value=float('inf')
# # for n in a: 
# #     if n<min_value:
# #         min_value=n
# # print(min_value)


# # lowest=float('inf') 
# # highest=float('-int')
# # for i in a:
# #     if i <lowest:
# #         lowest=i
# #     if i> highest:
# #         highest=i
# # print("the highest number is", highest)
# # print("the lowest number is",lowest)

# #task 1 # reverse the string inside the list 
# # listing =['ram','shyam','hari','asmin','keshav']
# # for i in listing:
# #     list=i[::-1]
# #     print(list)
# #tas1 duplicate #reverse the string inside the list of the list
# listing =['ram','shyam','hari','asmin','keshav']
# listing=listing[::-1]
# for i in range(len(listing)):

#     listing[i]=listing[i][::-1]
# print(listing)