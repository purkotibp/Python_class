#different types of method decorators in ops 
#1. class method
#2. static method 
#3. instance method


class Student:
    school_name ="asmita" # class attribute
    def __init__ (self,name,age,check_height):
        self.name=name
        self.age=age #object attibute
        self.check_height=check_height

    @classmethod
    def change_school_name(cls, new_name): #.cls represent class nad 
        cls.school_name =new_name


   # @instancemethod
    def check_height(self):
        self.check_height=10
        return f"the height is {self.check_height}"


    @staticmethod
    def check_percentage (percentage): #it doens;t requires the self,cls .it just represents as it normal function
        # grade checking
        if percentage >=90:
            return "A"
        if percentage >=80:
            return "B"
        if percentage >=70:
            return 'C'
        
first_student=Student("bishwas",18)
print(first_student.check_percentage(80))



# ------------------task 1--------
#using instance class and static methods 
# create a class called "vechile"
#create a class mehtod called "change_model" that change the model of the vechile "
# create a static_method called check_speed" that checks the speed of the vechile.
# create a instance method called "drive" that drives the vechile..


class Vechile:
    vechile_model="car"
    def __init__(self,name,drive):
        self.name=name
        self.drive=drive


    def drive(self):
        return"the care is driven"
    
    @classmethod
    def change_model(cls,new_model):
        cls.vechile_model=new_model
        return cls.vechile_model

    @staticmethod
    def check_speed(km_per_hour):
        if km_per_hour>=80:
            return"over_speed"
        elif km_per_hour>=60:
            return"good_speed"
        elif km_per_hour>=40:
            return"normal_speed"

        else:
            return"normal_speed"
        
car1=Vechile('mercedes',)
print(car1.check_speed(70))