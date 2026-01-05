#object orient programming
#hero class
#__init__ it is special function
class Hero:
    def __init__(self,name,health_power,age):
        self.name =name 
        self.health_power = health_power
        self.age =age 
    def decrease_health(self,power):
        self.health_power -= power 
        return self.health_power
    



#creating a object of hero class
captain_america = Hero("Steve Rogers",100,150)

let=Hero(130,'hellow',230) ## it assign to positional arguments 
print(let.name)
print(captain_america.name,captain_america.age)
captain_america.decrease_health(10)
print(captain_america.health_power)




#-----------task1-----------#

class Dog:
    def __init__(self,name,age,color):
        self.name=name
        self.age= age
        self.color= color 

    def sound(self,bark):
        self.bark= bark
        bark=print('bear bear')
        return self.bark
# creating object
husky=Dog('swizy',25,'gray')
print(husky.name)
print(husky.sound())

