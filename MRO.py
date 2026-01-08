#inheritance---
#------------ Method Resolution Order--------------#

# class AA:
#     def make_sound(self):
#         return "AA sound "
    
# class BB:
#     def make_sound(self):
#         return "BB sound"

# class A(AA):
#     def sound(self):
#         return "A sound"
    
# class B(BB):
#     def sound(self):
#         return "B sound"
    
# class C(A, B):
#     pass

# object = C()
# print(object.make_sound())
# print(C.mro)



#-------task1--------#
class AA:
   def make_sound(self):
        return "AA sound "
    
class BB:
    def make_sound(self):
        return "BB sound"
    
class CC:
    def make_sounde(self):
        return "CC sound"

class A(AA):
    def sound(self):
        return "A sound"
    
class B(BB):
    def sound(self):
        return "B sound"
    
class C(CC):
    def sound(self):
        return "C sound"
    
class C(A, B, C):
    pass

object = C()
print(object.make_sounde())
print(C.mro)

