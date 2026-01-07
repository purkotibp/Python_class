#--------task1--------------#
#-----task related to multiple inheritance
#Functional Designation type multiple inheritance
#create a class internship that inherits from employee and functional designation and department class
#get add a new attribute called "internship duration"
#get all the interns related to specific department and functional arguments
#get the longest survival of an intern in a paraticular department and functional Designation 
#get the total number in a particular department and function designation 
  #searching and filterning :---- with container . 

class Department:
    def __init__(self,department_name):
        self.department_name=department_name



class Employee:
    def __init__(self,name):
        self.name=name
        
class Designation:
    def __init__(self,designation_name):
        self.designation_name=designation_name

class Internship(Employee,Designation,Department):
    def __init__(self,name,designation_name,department_name,duration):
        super().__init__()

    def calculate_longest_duration(self,Duration):
        if self.Internship_Duration>=Duration:
            return(f"the longest duration period of {self.Internship_Duration}")

        else:
            return(f"{self.Internship_Duration}{False}")
        
