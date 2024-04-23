#Functions

def calculate(a,b):
    sum=a+b
    print(sum)
    return sum
calculate(4,6)
#other lines of code
calculate(4,8)
#other lines of code
calculate(4,10)

#another methd
#def = function defination
def calculate(a,b):#parameters
    return a+b
sum =calculate(3,4)#idr fxn ko call krte h,(1,2,) jo yeh 1,2, h inko hm arguments bolte h
print(sum)

#another methd
def print_hello():#agr hme hello print krwana h to
    print("hello")
print_hello()
print_hello()

#avarage of 3 no

def cal(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg
cal(1,2,3)

#TYPES
#BUILT-IN FUNTIONS
#yeh bo fxn hote h jo aready bne ho  python k andr 
'''
print() yeh simply print krta h jo hmne likha ho
len()yeh length btata h kese b chiz ki
type()yeh type btata h
range() yrh range btata h isme start point fir stop point or fir step point k hme usme kitne steps ka space lena h
'''
#USER DEFINED FUNCTIONS
#yeh bo fxn hote h jo hm bnate h jo user bnata h

#DEFAULT PARAMETERS
#esi values jb hmare pass koi argument pass nhi hota 

def cal(a,b=2):
    
    print(a*b)
    return a*b

cal(1)#koi value pass nhi kregy  

#question 1
nums=[2,54,76,23,4,21]
cities=["kashmir","himachal","punjab","haryana","roorkee"]
def print_len(nums):
    print (len(nums))
print_len(nums)    
print_len(cities)

#question2 
cities=["kashmir","himachal","punjab","haryana","roorkee"]

def print_len(list):
    print (len(list))

def print_list(list):
    for item in list:
        print(item,end=" ")
print_list(cities)
print()

#question 3

def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact *= i
    print(fact)   
    
cal_fact(5) 

#question 4

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val,"USD=",inr_val,"INR")

converter(1)

#RECURSION = fxn jb khud ko call kre

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
    
show(5)

#RECURSION THROUGH FACTORIAL

#factorial of n
def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1)*n
print(fact(4))

#QUESTION 
def cal_sum(n):
    if(n==0):
        return 0
    return cal_sum(n-1)+n
sum=cal_sum(5)
print(sum)