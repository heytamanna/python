#dictionary and sets 
#theystore values in key = value pairs...........#isme koi order or index values ni hoti

dict={
    "name" :"tamanna",
    "age" : 21,
    "course" :"btech",
    "subjects" : ["python","c++","html"],
    "topics" :("dict","sets")
    }
print(dict["name"]) #agr hme kese specific ko print krwana hota h to hm use key name sy bhi print krwa skte h
#if we want to change our name then we can change that with thw help of given follow :

dict["name"]="Tamannaa"
print(dict)
#if we want to add a value then we can do that also
dict['surname']="choudhary"
print (dict)
#we can create a null dictionary also
null_dict ={}
print(null_dict) #or isme hm koi value bhi add kr skte h....null_dict ={"name"}="Tanu"

#nested dictionary

student = {
    "name" : "Tanu",
    "subjects": {
        "dsa" :97,
        "phy" :78,
        "java" :90
        }
    
}
print(student)
print(student["subjects"])

#dictionar methods
'''
myDict.keys() #isme hme sbi keys print hoti h
myDict.values() #isme hme sbi values print hoti h
myDict.items() #it print in the form of tuple
myDict.gets("key) #print specific key 
myDict.update(newDict) 
'''
student = {
    "name" : "Rajat",
    "subjects": {
        "dsa" :97,
        "phy" :78,
        "java" :90
        }
}
print(student.keys())
print(student.values())
print(student.items())
print(student.get("subjects"))
#isme hm new dic. values bhi add kr skte thy
student.update({"city" :"himachal"})
print(student)

#SETS
#unoederd ,,,,,,NO INDex
set1={2,3,6 ,7,4,1,"hey","hii","bye"} #yeh duplicate values ko ignr krta h agr koi same valuse ek sy jada baar likhi h to bo ek he baar print hogi

print(type(set1))

#empty set = set{} asy likhte h

#SETS METHODS

'''
set.add(el)
set.remove(el) 
set.clear() 
set.pop()#remove random value

'''
collection=set()
collection.add((1,2,3,4,5))
collection.add(2)
collection.add(3)
collection.add("hey")
print(collection)
collection.remove("hey")
print(collection)
print(collection.pop())
collection.clear()
print(collection)

#set.union(set2) #combine both set value and returns new
#set.intersection(set2) #combines comn value and return new

set1={1,2,3,4,5}
set2={3,4,5,6,7}

print(set1.union(set2))

print(set1.intersection(set2))

#question 1
dict ={
    "table":("a piece of furniture","lists of facts & figures"),
    "cat":"a small animal"
}
print(dict)

#question2

subjects={
    "python","java","c++","python","javascript","java","pyhton","java","c++","c"
}
print(len(subjects))


#question3
marks={}
x =int(input("enter marks of phy:" ))
marks.update({"phy" : x})
x =int(input("enter marks of eng:" ))
marks.update({"eng" : x})
x =int(input("enter marks of hindi:" ))
marks.update({"hindi" : x})

print(marks)

#question 4

set={9,"9.0"}#9,9.0 ka same he value hoti h to yeh ek ko he print krta h for that reason we use" "
print(set)