info = {
    "key":"value",
    "name":"kaushal",
    "learning":"coding", #we can include any data type(float in key too)in dictinoary or array and lsit to and tuple too
    "age" : 35,
}
print(info)

null_dict={}
null_dict["name"]="apnacollege"
print(null_dict)

#nested 
student={
    "name":"rahul kumar",
    "subjects":{
        "phy":97,
        "chem":98,
        "math":95
    }
}
print(student)
print(student["subjects"])

#dict methods
print(student.keys()) #shows keys(name,subjects)
print(student.values()) #shows value
print(list(student.values()))
print(student.items())
print(student.get("name")) #noerror
#print(student["name2"]) #error

student.update({"city":"delhi"})
print(student)


#set in python
# collection={1,2,3,4}
collection={1,2,2,2,"hello","world","world"} #duplicate value will get ignored and doesnot follow any order                  
print(collection)
print(type(collection))
print(len(collection))#total number of items

collect={}#empty dictionary not set
print(type(collect))

coll=set() #this is balla empty set; syntax
print(type(coll))

#set methods are set.add(),set.remove(),set.clear(),set.pop()
#set are mutable 

colle=set()
colle.add(1)
colle.add(2)
colle.add("apna")
print(colle)

#union and intersection of sets
set1={1,2,3,4}  
set2={3,4,5,6}
set3=set1.union(set2)
print(set3) #{1,2,3,4,5,6}      
set4=set1.intersection(set2)
print(set4) #{3,4}     

#example for dictionary and set
student1={
    "name":"rahul",
    "age":20,
    "subjects":{"math":95,"phy":98}
}   
student2={
    "name":"sonam", 
    "age":22,
    "subjects":{"math":88,"phy":92} 
}
student3={
    "name":"anil",
    "age":21,
    "subjects":{"math":78,"phy":85}
}
students=[student1,student2,student3]
print(students)

subject_set=set()
for student in students:
    for subject in student["subjects"].keys():
        subject_set.add(subject)    
print(subject_set)
#output: {'math', 'phy'}
    

