# Task 1: The "Digital Wallet" (Basic Encapsulation)
# Goal: Practice using private variables to prevent unauthorized changes to a balance.
# The Problem:Create a class called Wallet.
# Private Attributes: ownerName (String) and balance (Double).
# The Logic:
# Constructor: Set the owner's name and start the balance at 0.
# deposit(amount): If the amount is greater than 0, add it to the balance.
# withdraw(amount): If the amount is less than or equal to the balance, subtract it. Otherwise, print: "Insufficient funds!"
# getBalance(): A getter method to see the current money.


class Digital_wallet:
    def __init__(self,owner_name,balance=0):
        self.__owner_name=owner_name
        self.__balance=float(balance)
        

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            return self.__balance
        else:
            return("insufficent balance")
        

        



# Task 3: The "Car Fuel System" (Validation Logic)
# Goal: Practice using "Setters" to validate data before saving it to an object.
# The Problem:Create a class called Car.
# Private Attributes: modelName (String) and fuelLevel (Integer).
# The Logic:
# Constructor: Set the modelName and set fuelLevel to 50 (percent).
# drive(): Each time this is called, decrease fuelLevel by 10.
# If fuelLevel reaches 0, print: "Out of fuel! Cannot drive."
# refuel(amount):
# If amount + fuelLevel is more than 100, print: "Tank is overflowing! Setting fuel to 100%." and set it to 100.
# Otherwise, add the amount to the current fuel.
# displayFuel(): Show the remaining percentage of fuel.

class car:
    def __init__(self,modelName):
        self.__modelName = modelName
        self.__fuelLevel = 50#default fuel level

    def __setFuelLevel(self, value):
        if value > 100:
            self.__fuelLevel = 100
        elif value < 0:
            self.__fuelLevel = 0
        else:
            self.__fuelLevel = value

    def drive(self):
        if self.__fuelLevel==0:
            print("Out of fuel! cannot drive")
        else:
            self.__setFuelLevel(self.__fuelLevel - 10)
            
    def refuel(self,amount):
        if self.__fuelLevel<100:
            self.__fuelLevel +=amount
        else:
           print("Tank is overflowing! Setting fuel to 100%.")
        
    def displayFuel(self):
        print(self.__fuelLevel)
    

car1= car('suzuki')
car1.displayFuel()
car1.refuel(50)
car1.displayFuel()
car1.drive()
car1.displayFuel()



#------ uses encapsulation to hide the internal mehtod   ------

#create celesius ,fahreheit and kevin 
#the class should have method to set the temperature in one unit 
#and get the temperature in another unit 
#unit encapsulation to hide the internal method for conversion

# class  celesius:
#     def __init__(self,)