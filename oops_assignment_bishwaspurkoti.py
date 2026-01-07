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
    def __init__(self,owner_name):
        self.__owner_name=owner_name
        self.__balance=0.0
        
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("insufficent balance")
    def  withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance -=amount
            return 
        else:
            print("INSUFFICENT FUNDS")        
    def getBalance(self):
        return self.__balance

wallet1=Digital_wallet('bishwas')
wallet1.deposit(1000)
print(wallet1.getBalance())
print(wallet1.withdraw(100),wallet1.getBalance())
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





# Task 2: The "Smart Light Bulb" (State Management)
# Goal: Understand how methods change the "internal state" of an object without the user touching variables directly.
# The Problem:Create a class called SmartBulb.
# Private Attributes: brightness (Integer) and isOn (Boolean).
# The Logic:
# Constructor: The bulb should start "Off" (false) and brightness at 0.
# turnOn(): Sets isOn to true and sets brightness to 100.
# turnOff(): Sets isOn to false and sets brightness to 0.
# dim(value): * If the bulb is Off, print: "Cannot dim a bulb that is off!"
# If the bulb is On, decrease the brightness by the value, but don't let it go below 0.
# getStatus(): Print whether the bulb is on/off and its current brightness level.

class SmartBulb:
    def __init__(self):
        self.__isOn = False       
        self.__brightness = 0

    def turnOn(self):
        self.__isOn = True
        self.__brightness = 100

    def turnOff(self):
        self.__isOn = False
        self.__brightness = 0

    def dim(self, value):
        if not self.__isOn:
            print("Cannot dim, bulb is off!")
        else:
            self.__brightness -= value
            if self.__brightness < 0:
                self.__brightness = 0

    def getStatus(self):
        state = "ON" if self.__isOn else "OFF"
        print(f"Bulb is {state}, Brightness: {self.__brightness}")

bulb = SmartBulb()
bulb = SmartBulb()
bulb.turnOn()
bulb.getStatus() 
bulb.dim(30)
bulb.getStatus()    
bulb.turnOff()
bulb.dim(10)          
bulb.getStatus() 
#------ uses encapsulation to hide the internal mehtod   ------

#create celesius ,fahreheit and kevin 
#the class should have method to set the temperature in one unit 
#and get the temperature in another unit 
#unit encapsulation to hide the internal method for conversion

# class  celesius:
#     def __init__(self,)