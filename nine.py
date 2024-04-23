#del keyword = used to dlt properties or object

#del s1.name
#del s1

#private and public
class Account:
    def __init__(self,acc_no,account_pass) :
        self.acc_no=acc_no
        self.__account_pass=account_pass #kese bhi account ko private bnane k liye h do underscore lga dete h
     
    def reset_password(self):
        print(self .__account_pass)
            
acc1 =Account(10000,123456)

print(acc1.acc_no)
print(acc1.reset_password())  


#inheritence
#parent to child
    
class Car:
    @staticmethod
    def start():
        print("car started..")
        
    @staticmethod
    def stop():
        print("car stoped..")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

car1 =ToyotaCar("fortuner")
car2 =ToyotaCar("tata punch")   

print(car1.start())        

#inheritence 3 types
#single
#multi_level =base class sy drive class ny li fir ek or drive class ny li
#multiple
#eg of multi-level
class Car:
    @staticmethod
    def start():
        print("car started..")
        
    @staticmethod
    def stop():
        print("car stoped..")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand
        
class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type=type
        
car1 =Fortuner("diesel")
car1.start()

#eg of multiple inheritence

class A:
    varA ="welcome to class A"

class B:
    varB ="welcome to class B"

class C(A,B):
    varC ="welcome to class C"
    
c1=C ()

print(c1.varC)
print(c1.varB)
print(c1.varA)

#super method
#used to access method of the parent class


class Car:
    
    def __init__(self,type):
        self.type =type
        
    @staticmethod
    def start():
        print("car started..")
        
    @staticmethod
    def stop():
        print("car stoped..")

class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
        
car1=ToyotaCar("punch","electric")
print(car1.type)

'''
polymorphism: operator overloading
a+b =addition  ......//a.--add----(b)
a-b =subtraction....//a.--sub---(b)
a*b =multiply......//a.--mul----(b)
a/b =division......//a.--truediv----(b)
a%b =addition.......//a.--mod----(b)
'''
#SAME SYMBOLS KA DIFF DIFF MEANING HONA

print(1+2)   #3   
print("hey" +"tanu")#concatenate
print([1,2,3]+[3,4,5])#merge

#Question1

class Circle:
    def __init__(self,radius):
        self.radius =radius
        
    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2*22/7 * self.radius 
       
c1 =Circle(21)
print(c1.area())
print(c1.perimeter())

#Question2

class Order:
    def __init__(self, item,price):
        self.item=item
        self.price=price
        
    def __gt__(self,ord2): #we use gt for greater 
        return self.price>ord2.price
    
ord1 = Order("chips",40)
ord2 = Order("coffee",30)

print(ord1>ord2)
               
       