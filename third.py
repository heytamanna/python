#Lists
#[]brackets m likhte h 
marks=[6,45.8,56.9,87.4,]

print(marks)

#type print krwane k liye
print(type(marks))

#indexing values k through kese bhi value ko print krwa skte h
print(marks[3])

#length bhi print krwa skte h
print(len(marks))

#isme diff types k elements ko store kr skte h (float,string ,intetc)

student=["tamanna",21,"himachal ",7.11]
print(student)
print(type(student))
print(len(student))

#isme hm value ko cahnge kr skte h jase tamanna ki jgh tanu iski index value ki help sy
student[0]="tanu"
print(student)

#list slicing
print(student[1:4])

#list methods
'''
list[2,1,3]
list.append (add element)[2,1,3,4]
list.sort()[1,2,3]
list.sort(reverse=True)[3,2,1]
list.reverse()[3,1,2]
list.index(idx.el) =insert element at index
list.pop(indx value)
'''
list=[54,65,23,79]
print(list)
list.append(9)
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.remove(65)
print(list)
list.reverse()
print(list)
list.insert(2,56)
print(list)
list.pop(3)
print(list)

#tuples in python

tup=(43,54,32,5,9,)
print(tup)
print(type(tup))
print(tup[3])

#empty tuple
tup=()
print(tup)
print(type(tup))

#tuples m agr hme single value print krwani h to hm usko akela nhi likh skte uske sth hme , lgana pdta h
tup=(2,)
print(tup)

#slicing
tup=(43,54,32,5,9,)
print(tup[1:3])

#methods
#tup.index(element) isse pta chlta h jo element hmne likha h bo first tym kb aya konse index py aaaya h
#tup.count(element) yeh count kr k btana h k jo element hmne likha h bo kitni baar us tuple m present h
#palindrome hota h jo check krta h jo samne sy or piche sy same hoti h ==for eg.maam isme shuru sy pdegy to bhi maam pdegy or end sy pdegy to bhi maam hoga 
tup=("tam",20,22,21,"hey",21)

print(tup.index(22))
print(tup.count(21))

#questions
movies=[]
movies.append(input("first movie: ")) 
movie2=input("second movie: ")
movie3=input("third movie: ")

movies.append(movie2)
movies.append(movie3)

print(movies)

#question2
list1=[1,2,3,2,1]
list2=["m","a","l","m"]

copy_list1 = list1.copy()
copy_list1.reverse(
    
)

if(copy_list1 == list1):
    print("pallindrom")
else:
    print("not a pallindrome")    
    
copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("pallindrom")
else:
    print("not a pallindrome") 
    
#question 3

grades=("D","A","F","A","A","B","D")       

print(grades.count("A"))

#question 4

list=["D","A","F","A","A","B","D"]
list.sort()
print(list)