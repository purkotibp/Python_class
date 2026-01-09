# #ABSTRACT CLASS CANN0T BE INITIATED 
# from abc import ABC, abstractmethod 


# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass 

# class circle(Shape):
#     def area(self,radius):
#         return 3.14 * radius * radius 
    
# print(circle().area(10))


#------------ task1 --------------_#
#class work in abstraction
#create a coffe machine abstact class with abstract method makecoffe
#create two sunclasses of cofee machine: latte machine and mochaamchine 
#implement abstract method make_coffe in latte macine and mocha mmachine
#create an instance of latte machine and mocha machine 
#call make_coffe on both instances 


from abc import ABC, abstractmethod
class coffee_machine(ABC):
    @abstractmethod
    def make_coffee(self):
        pass

class LatteMachine(coffee_machine):
    def make_coffee(self,add_sugar=1):
        add_sugar=add_sugar
        return "Latte_coffee made"

class Mocha_machine(coffee_machine):
    def make_coffee(self,less_sugar=2):
        less_sugar=less_sugar
        return "Mocha_machine"
    
latte=LatteMachine()
print(latte.make_coffee(2))

mocha=Mocha_machine()
print(mocha.make_coffee(3))