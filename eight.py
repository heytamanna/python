#oops in python
#reduntancy + reusability
#class & object in python
#creating class

class Student:
    name="Tam"
    
#creating object

s1=Student()
print(s1.name)    


s2=Student()
print(s2.name)   

#CONSTRUCTURE
class Student:
    
  def __init__(self,name,marks):#this is a constructor
      self.name = name
      self.marks = marks
      print("adding a new name in database ..")# yeh  hr nyi object k sth call hota h
    
s1=Student("Tamanna",98)
print(s1.name,s1.marks)    


s2=Student("Ankita",89)
print(s2.name,s2.marks)  

#question1

class Student:
   def __init__(self,name,marks):
      self.name = name
      self.marks = marks
  
   def get_avg(self):
      sum=0
      for val in self.marks:
          sum+=val
      print("hi",self.name, "your avg score is:", sum/3)


s1=Student("tamanna",[87,56,98])
s1.get_avg()    
# we can change our attribute value also
s1.name="tam"
s1.get_avg() 

#static methods

#dont use self parameters

class Student:
   def __init__(self,name,marks):
      self.name = name
      self.marks = marks
      
   @staticmethod
   def hello():
       print("hello")
   
   
   def get_avg(self):
      sum=0
      for val in self.marks:
          sum+=val
      print("hi",self.name, "your avg score is:", sum/3)


s1=Student("tamanna",[87,56,98])
s1.get_avg() 

print("hello")   

#question2

class Account:
    def __init__(self,bal,acc) :
        self.balance=bal
        self.account_no=acc
        
    #debit method
    def debit(self,amount):
        self.balance-=amount
        print ("Rs.",amount,"was debited")
        
        
    #credit method
    def credit(self,amount):
        self.balance+=amount
        print ("Rs.",amount,"was credited")
        
    def get_balance(self):
        return self.balance
     
acc1 =Account(10000,123456)
acc1.debit(1000)
acc1.credit(2500)
print(acc1.balance)
print(acc1.account_no)