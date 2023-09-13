from statistics import mean

class School_Class:
    
    def __init__(self):
        self.number=int(input())
        self.age    = list(int(n) for n in input().strip().split())[:self.number]
        self.height = list(float(n) for n in input().strip().split())[:self.number]   
        self.weight = list(float(n) for n in input().strip().split())[:self.number] 
    
    
    def print_age_info(self):
        return (float(mean(self.age)))
    
    def print_height_info(self):
        return (float(mean(self.height)))  
        
    def print_weight_info(self):
        return (float(mean(self.weight)))    
    
        

Class_A = School_Class()
Class_B = School_Class()

# print mean of age,height, and weight of class A
print(Class_A.print_age_info())
print(Class_A.print_height_info())
print(Class_A.print_weight_info())

# print mean of age,height, and weight of class B
print(Class_B.print_age_info())
print(Class_B.print_height_info())
print(Class_B.print_weight_info())


if (Class_A.print_height_info() > Class_B.print_height_info()):
    print("A")
    
if (Class_B.print_height_info() > Class_A.print_height_info()):
    print("B")
    
if (Class_B.print_height_info() == Class_A.print_height_info()):
    if (Class_B.print_weight_info()<Class_A.print_weight_info()):
        print("B")
        
    if (Class_A.print_weight_info()<Class_B.print_weight_info()):
        print("A")
        
if (Class_A.print_height_info() == Class_B.print_height_info() and Class_A.print_weight_info() == Class_B.print_weight_info()):
    print("Same")            