# # #ABSTRACT CLASS CANN0T BE INITIATED 

# #ABSTRACTION using the polymorphism . 
# # from abc import ABC, abstractmethod 


# # class Shape(ABC):
# #     @abstractmethod
# #     def area(self):
# #         pass 

# # class circle(Shape):
# #     def area(self,radius):
# #         return 3.14 * radius * radius 
    
# # print(circle().area(10))


# #------------ task1 --------------_#
# #class work in abstraction
# #create a coffe machine abstact class with abstract method makecoffe
# #create two sunclasses of cofee machine: latte machine and mochaamchine 
# #implement abstract method make_coffe in latte macine and mocha mmachine
# #create an instance of latte machine and mocha machine 
# #call make_coffe on both instances 


# # from abc import ABC, abstractmethod
# # class coffee_machine(ABC):
# #     @abstractmethod
# #     def make_coffee(self):
# #         pass

# # class LatteMachine(coffee_machine):
# #     def make_coffee(self,add_sugar=1):
# #         add_sugar=add_sugar
# #         return "Latte_coffee made"

# # class Mocha_machine(coffee_machine):
# #     def make_coffee(self,less_sugar=2):
# #         less_sugar=less_sugar
# #         return "Mocha_machine"
    
# # latte=LatteMachine()
# # print(latte.make_coffee(2))

# # mocha=Mocha_machine()
# # print(mocha.make_coffee(3))




# #----------encapsulation and acheiving abstraction ----. 


# # class coffee:
# #     def __init__ (self):
# #         self.water_level=100
        
# #     def make_coffee(self):
# #         print("The office processing is starting ........")
# #         self._heat_water()
# #         self._grind_bean()
# #         self._brew()

# #     def _heat_water(self):
# #         print("the water is heating..........")

# #     def _grind_bean(self):
# #         print("the coffee is hiding .........")
        
# #     def _brew(self):
# #         print("the coffee is brewing ............ ")

# # my_coffee=coffee()
# # my_coffee.make_coffee()




# # task-2------------


# class Text_App:
#     def __init__(self):
#         self.time=1

#     def text_msg(self):
#         print("the messaged recieved.")
#         self._message_sent()
#         self._message_deliverd()
#         self._message_seen()


#     def _message_sent(self):
#         print("Write a message")

#     def _message_deliverd(self):
#         print("the message is sent and deliverd")
    
#     def _message_seen(self):
#         print("the message is seen")

# messenger=Text_App()
# messenger.text_msg()


