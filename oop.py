# # #object orient programming
# # #hero class
# # #__init__ it is special function
# # class Hero:
# #     def __init__(self,name,health_power,age):
# #         self.name =name 
# #         self.health_power = health_power
# #         self.age =age 
# #     def decrease_health(self,power):
# #         self.health_power -= power 
# #         return self.health_power
    



# # #creating a object of hero class
# # captain_america = Hero("Steve Rogers",100,150)

# # let=Hero(130,'hellow',230) ## it assign to positional arguments 
# # print(let.name)
# # print(captain_america.name,captain_america.age)
# # captain_america.decrease_health(10)
# # print(captain_america.health_power)




# # #-----------task1-----------#

# # class Dog:
# #     def __init__(self,name,age,color):
# #         self.name=name
# #         self.age= age
# #         self.color= color 

# #     def sound(self,bark):
# #         self.bark= bark
# #         bark=print('bear bear')
# #         return self.bark
# # # creating object
# # husky=Dog('swizy',25,'gray')
# # print(husky.name)
# # print(husky.sound())




# #Encapsulation
# #.__self.balance




# #------ Inheritance-----#
# #inheritance is the mechanism in oop that allows a new class form the super class.
# # method , attibutes, fetching from the super class . 


# #create a class called "smartphone" that inherit from "phone"
# #it should hvbe new attribute called "memory" and a method called"take photos"

# class phone:
#     def __init__(self,type):
#         self.type=type
# class smartphone(phone):
#     def __init__(self,type,memory):
#         # phone().__init__(self,type)tradtional way 
#         super().__init__(type) #modern way 
#         self.memory=memory

#     def takephotos(self): 
#         print("the photo has been taken")
         
# mobile1 =smartphone("samsung","512mb")
# print(mobile1.type)
# mobile1.takephotos()


# #multiple inheritance 
# class Employee:
#     def __init__(self,name):
#         self.name=name

# class Salary:
#     def __init__(Employee,salary):
#         self.Employee=Employee
#         self.salary =salary

# class Payroll(Employee,Salary):
#     def get_salary(self):
#         return self.get_salary
#     def get_name(self):
#         return self.name

# f=Payroll('sammy',120)
# print(f.get_name())
# print(f.get_salary())




class Internship(Employee, FunctionalDesignation, Department):
    def __init__(self, name, designation, dept_name, duration):
        # super() handles the MRO flow to initialize all parent classes
        super().__init__(name=name, designation=designation, dept_name=dept_name)
        self.internship_duration = duration

    def __repr__(self):
        return f"Intern: {self.name} ({self.dept_name} - {self.designation})"

# -------------------method resolution order (MRO)------------#