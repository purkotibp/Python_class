# #sum of natural number using recursive function
# def natural_number(n):
#     if n==1:
#         return 1
#     else:
#         return (n)+natural_number(n-1)
    
# print(natural_number(5))

# #task2 # from the list find the smallest number using the recursive function.

# list=[22,11,10,18,56,34]
# def small(list):
#     if list==1:
#         return 
# 
# 
#find the next possible leap year using recursive function


def Leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

year = 2021
print(Leap_year(year))

