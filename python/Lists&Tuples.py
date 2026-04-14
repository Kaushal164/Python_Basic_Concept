# marks1=94.4
# marks2=87.5
# marks3=95.2
# marks4=66.34
# marks5=45.1

#alternative
marks= [94.4,87.5,95.2,66.34,45.1]
print(marks)
print(type(marks)) #class list ho 
print(len(marks))
print(marks[0])
print(marks[1])

student=["karan",95.4,17,"delhi"]
print(student[0])
student[0]="arjun"    #in list data can be changed 
print(student) 

str="hello"
print(str[0])
#str[0]="y"   error occur bexause it cant be changed it is a string 

#list slicing 
mark=[85,94,76,63,48]
print(mark[1:4]) #from 1 to 3     same from previous str slicing 

#list methods function
list=[2,1,3]
list.append(4) #add number 
print(list)
print(list.sort())  #ascending order
print(list)
print(list.sort(reverse=True))  #descending order
print(list)
list.reverse() # reverse
print(list)
list.insert(1,5) #add 5
print(list)
list.remove(2) #remove elemement 2
print(list)
list.pop(2) #remove the index 2 from the lsit 
print(list)

list=["banana","litchi","apple"]
print(list)
print(list.sort())  #ascending order
print(list)
print(list.sort(reverse=True))  #descending order
print(list)
# it supports characters too eg, [a,b,c,d,e]


#tuples in python   list is changable,tuple is not changeable like string 

tup=(2,1,3,1) #this is tuple enclosed by()
print(type(tup))
print(tup[0])
print(tup[1])

print(tup.index(2)) #return index of first occurrence
print(tup.count(2)) #counts total occurrences

#example to enter names of 3 movies and store in the list 
# movies=[]
# mov1=input("enter first movie")
# mov2=input("enter second movie")
# mov3=input("enter third movie")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

# movies=[]
# mov=input("enter first movie")
# movies.append(mov)
# mov=input("enter second movie")
# movies.append(mov)
# movg=input("enter third movie")
# movies.append(mov)
# print(movies)

movies=[]
movies.append(input("enter first movie"))
movies.append(input("enter second movie"))
movies.append(input("enter third movie"))
print(movies)

#palindrome 
list1=[1,2,1]
list2=[1,2,3]

copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("palindrome")
else:
    print("not palindrome")
        


















