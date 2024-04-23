#TYPES
#1.Text files: .txt,.docx,.log etc
#2.binary files: .mp4,.mov,.png,.jpeg etc
'''
f=open("demo.txt","r")
data = f.read()
print (data)
print(type(data))
f.close()

f=open("demo.txt","r")
data = f.readline()
print (data)
print(type(data))
f.close()

f=open("demo.txt","w")#it replace the data in demo file

f.write("i want to learn python tomorrow")#agr hme iske aagy or lines likhni h to \n lga k hm next line m usko print krwa skte h 
f.close()

# agr hmare pass koi file exist nhi krti to hm use create bhi kr skte h by this method

f = open("sample.txt", "a")
f.close()

#another syntex for opening a file
with open("demo.txt","w")as f:
    data = f.read()
    print(data)
    
#deleting a file
#using os model = yeh phlt sy bne hote h
#import os
#os.remove(filename)

#pip=package instaler for python

import os

os.remove("sample.txt")
#yeh file ko dlt krta h
'''
#QUESTION 1
'''

with open("practice.txt","w")as f:
   f.write("HI everyone\nwe are learning file input and output\n")
   f.write("using java.\nI like programing in java")

#QUESTION 2

with open("practice.txt","r")as f:
    data = f.read()
    
    new_data=data.replace("java","python")
    print(new_data)
    
    with open("practice.txt","w")as f:
        f.write(new_data)
        
#QUESTION 3
word="learning"
with open("practice.txt","r")as f:
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")
 '''       
#QUESTION 4
with open("practice.txt","r")as f:
    data =f.read()
    print(data)
