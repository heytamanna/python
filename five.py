#LOOPS  ==== used to repeate instructions

#while loops,for loops
'''
count =1
while count<=5 :
    print("hello")
    count+=1
    
    #second example
    
i=1
while i<=3 :
    print("how are you")
    i+=1
    
'''

#print no. 1 to 10
i=1
while i<=10:
    print(i)
    i+=1

print("okkk")  
   
#print no. 10 to 1 
t=10
while t>=1:
    print(t)
    t-=1  

print("bye")
 
#question 1
i=1
while i<=100:
    print(i)
    i+=1

print("khlas")
 
#question 2
i=100
while i>=1:
    print(i)
    i-=1
    
print("done") 
       
#question 3
i=3
while i<=30:
    print(i)
    i+=3
print("khtm")     

#question 4

num= [1,4,9,16,25,36,49,64,81,100]
           
idx =0
while idx < 10:   
    print(num[idx])
    idx += 1  

# question 4....2part

name = ["tanu","tam","tom","tim","jim"]

idx=0
while idx<5:
    print(name[idx])
    idx+=1

#question 5

#find  value of the x
tup= (1,4,36,16,25,36,49,64,36,100)
x=36
 
i=0
while i<len(tup):
    if(tup[i]==x):
        print("found at index", i)
    else:
        print("finding..")    
    i+=1

#keywords
#break (end of program)   
#continue (used for skiping)
 
 #break eg
tup= (1,4,36,16,25,36,49,64,36,100)
x=36
i=0
while i<len(tup):
    if(tup[i]==x):
        print("found at index", i)
        break 
    else:
        print("finding..")    
    i+=1

#continue eg.
i=0
while i <=10: 
    if(i==3 ): 
        i+=1
        continue
    print(i)
    i+=1
    
#print  odd numbers 1to10
i=1
while i<=10:
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1
print("finish")   

#print even numbers 1to10
i=1
while i<=10:
    if(i%2!=0):
        i+=1
        continue
    print(i)
    i+=1  
print("finish")

#for loop

nums=[1,2,3,4,5]

for value in nums:
    print(value)
        
print("loop ended")

#for loop use in tuple
tup =(6,5,7,3,8)   
for values in tup:
    print(values)

print("loop ended")

#for loop use in string

str=("tanu","tamanna","tam","tim")

for characters in str:
    print(characters)
    
print("loop ended")

#question 1 

list= [1,4,36,16,25,36,49,64,36,100]  
for elements in list:
     print(elements)

print("loop ended")

#question 2

tup= (1,4,36,16,25,36,49,64,36,100)
x=16
idx=0
for elements in tup:
    if (elements==x):
        print("found x at idx " ,idx)
        break
    idx+=1

#RANGE() 3 ways to write

#1st  way
sequence=range(5)
for i in sequence:
    print(i)#isme jo ending no.hota h bo include nhi hota h.
    
#isko hm asy bhi likh skte h
for i in range(8):
    print(i)
        
#2nd way
for i in range(2,8):#start and ending point k bich ka print hoga
    print(i)

for i in range(2,8,2):#2 mtlv isme 2 ,2 ka gap aayega kyuki hmne isme 2 likha h
    print(i)   

#question 1

for i in range(1,101):
    print(i)

print("loop end")

#question 2

for i in range(100,0,-1):
    print(i)

print("loop end")

#question 3

n=int(input("enter the no:"))

for i in range(1,11):
    print(n*i)
    
#pass statement

for i in range(5):
    pass
print("hey")

#question 1 for while loop
#find sum of n natural no.

n = 5
sum = 0
i=1
while i<=n:
    sum += i
    i+=1
print("total sum is =",sum)
