print("Tamanna is my name")
print(2*2)
print(5+3)

#for variables
name = "Tanu"
age =21
cost =50
print ('my name is ' ,name)
print ('the cost of mango is ' ,cost )

#data types
name = "Tanu"
age =21
cost =50.5

#types use hota h data types ka pta lgane k liye k yeh konsa data type h 
print(type(name)) #word ya koi bhi sentence.
print(type(age)) #numerical values hoti h jo - bhi ho skti h or + bhi
print(type(cost)) # decimal 

#data types
'''
int= (- or +)
float(34.5.76)4
boolean(True or False)
str(" hsudihu" or 'xjnaush')
none(empty koi bhi value nhi)

'''
name = input("enter your name: ")#user sy input lyny k liye input likhte h
age =int(input("enter age; "))
marks =float(input("enter marks; "))

print("Hello " , name)
print("Your age is  " , age)
print("marks " , marks)

#  1 question
#intput 2 numbers & print their sum

num1=int(input("enter first no : " ))
num2=int(input("enter second no: " ))

print(num1+num2)
#  2 question
# WAP to input 2 int no. a and b,print True if a is greate than or equal to b.if not then  false.

num1=int(input("enter first no : " ))
num2=int(input("enter second no: " ))
 
print(num1>=num2)