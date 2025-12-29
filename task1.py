#Create a list of color:['red','green','blue']
color=['Red','Green','Blue']
print(color)

#Access the second element of the list 
print(color[1]) # the list starts form 0 so 1 is second index of list . 

#Update the first element of the list to yellow .
color.insert(0,'Yellow')
print(color)

#Slice list to get last two elements.
sliced=color[2::]
print(sliced)

#Get length of the list 
print(len(color))