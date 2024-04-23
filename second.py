#inko hm (strings ko)3 diff. types k qoutes m likh skte h.

str1= "this is a strng"
str2= 'himachal pradesh'
str3= """my name is tamanna"""
print(str3)

#escape sequence charaters.
a = ("my name is tanu .\ni m learning python") #\n used to move in the next line.
b = ("my name is tanu .\ti m learning python")#\t used to give tap space.
print(a)
print(b)

#basic operations
#1 = concatination "hello" + "world" ="helloworld"
str1= "hello"
str2= "world"
str3 = (str1 +str2)
print(str3)
#to isme helloworls sth m print ho jayega

#length of stirng
str1= "hello how r u"
str2= "world"
 
len1=(len(str1))  #yeh str1 ki length ko count krta h sth m jitne space h unko bhi.
print(len1)      

#indexing from 0 to 9
str1= "Tamanna"
print(str1[0])

#slicing 
#isme hm apni string ko tukdo m divide kr skte h or jo last ending index hota h bo include nhi hota h
str1= "hello" #ell kyuki last value mtlv 4 o count nhi hoga
str2= "world"#worl
str3= "morning"#ning

print(str1[1:4])
print(str2[:4])
print(str3[3:])

# - slicing jisme first count[-1] sy start hota h
str1= "Tamanna"
print(str1[-4:-1])#ann

#question 1

name = input("enter your name : ")#isme phly hm input lygy user sy naam ki
print(len(name))

#2 question
e =("hey tanu how many coins do you have . give me the coins")
print(e.count("coins"))

#yeh check krega k coins kitni baar is line m aa rha h

'''
str.endswith("end wrd") yeh check krta h k last ka wrd is wrd k sth end ho rha h ya nhi
str.capitalize()   yeh  first wrd ko capital krta h
str.replace("old","new") yeh purane wrd ko hta k new print krta h
str.find(wrd)   yeh kese word ko find krne k liye use hota h jha py b bo word first tym dikh jata h to bo uski index value ko print krwa deta h
str.count("wrd") yeh kese b word ko total kr k print krta h k bo word kitni bar us sting m aya h

'''

a =("my name is tamanna")
print(a.endswith("na"))
b =("my name is tamanna")
print(b.capitalize())
c =("my name is tamanna")
print(c.replace("tamanna","tanu"))
d =("my name is tamanna")
print(d.find("a"))
e =("my name is tamanna")
print(e.count("m"))

#CONDITIONAL STATEMENTS(if elif)

'''
if(condition):
     statement1
elif(condition):
    statement2
    else:
    statementN
'''
age=5 

if(age==18):
    print("can drive")  
elif(age==21):
    print("can vote")    
elif(age==15):
    print("can run")  
else:
    print("nothing")    
    
print("end of code ")

#example

marks=89

if(marks>=90):
    print("grade A")   
if(90>marks>=80):
    print("grade B")    
elif(80>marks>=70):
    print("grade C")

else:
    grade="D"
    
print("empty")  

#nesting
#mtlv ek statement k andr dusri statement likhna  
age=21

if(age>=18):
    if(age>=75):
        print("look")
    else:
        print("no")
else:
   print ("go")
            
#question 1
num=14

if(num%2==0):
    print("EVEN")
else:
    print("ODD") 
    
#question2
a=3
b=8
c=4
if(a>b and a>c):
    print(a)
elif(b>a and b>c):
    print(b)
else:
    print(c)       

a= int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
d=int(input("enter fourth number: "))

if(a>b and a>c and a>d):
    print(a)
elif(b>a and b>c and b>d):
    print(b)
elif(c>a and c>b and c>d):
    print(c) 
else:
    print(d)        
       
#question 3

x=21

if(x % 7==0):
    print("multiple")
else:
    print("not a multiple")    
    