print("hello world","kaushal")
print(23)
print(23+45)
name = "kaushal"
age = 43
price = 25.99
print(name)
print("my name is:",name)
age2=age 
print(age2)

print(type(name))
print(type(age))
print(type(price))  

a=2
b=5 
sum=a+b
print(sum)  
print(a==b)  #false
print(a!=b) #true 

num=10
num += 10 
print(num)

print("hello world") 
# print("hello world")   
# print("hello world")   ctrl+/ direct to get cmt easily 

#logical operators 
print(not False) #true print hunxa
print(not True)#false 

a=50
b=30 
print(not a>b)

val1=True
val2=True
print("and operator:", val1 and val2)

#type conversion 
a=2
b=4.25
sum=a+b
print(sum)

a=int("2")#string lai int ma lagyo(type cast)
b=4.25
print(a+b)

a=3.14
a=str(a)
print(type(a))
                                                    
#input
input("enter your name:")  
                                                  
name=input("enter your name:")
print("welcome",name)

val=input("enter some value:")
print(type(val),val) #always use string value wehen input in python

#we need to do type casting for that 
val=int(input("enter some value:"))
print(type(val),val)

name=input("enter name:")
age=input("enter age:")
marks=input("enter marks:")

print("welcome",name)
print("age:",age)
print("marks:",marks)

#example1 
a=int(input("first number:"))
b=int(input("second number:"))
sum=a+b
print("sum is:",sum)

#example2
side=int(input("enter side of a square:"))
Area=side*side
print("area of square:",Area)

#wap to input 2foating point numbers and print their average 
a=float(input("first number:"))
b=float(input("second number:"))
print("avg:",(a+b)/2)

#which one is greater
a=int(input("first number:"))
b=int(input("second number:"))
print(a>=b)

