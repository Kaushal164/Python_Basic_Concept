#string adn conditional staterment 
str1="this is a string.\nwe are creating it on python." #here \n is for to break the sentence
str2='kasuhal'
str3="""this is a string"""
print(str1)
print(str2+str3) #concanetation
print(len(str2)) #length of string 

#indexing 0,1,2,3,4,5,6......
str="apna college" 
ch = str[0]
print(ch)
print(str[2])

#slicing in python for machine learning(acesing part of a string)
str="apnacollege"
print(str[1:4]) #1 is start, 4 is end but while printing it will not include 4th
#also to print upto the last index you can write as len(str) like,
print(str[5:len(str)])
print(str[:4]) #[0:4]
print(str[5:]) #[5:len(str)]
#slicing negative indexing if apple=-5,-4,-3,-2,-1
str="apple"
print(str[-3:-1])

#string function 
str="i am studying from python in my from college"
print(str.endswith("ege")) #.endswith will determine if it ends with text or not 
print(str.endswith("app"))

print(str.capitalize()) #it capitalize first word in the text
print(str)

print(str.replace("o","a")) #replace
print(str.replace("python","javascript"))

print(str.find("o")) #find o for the first time in the sentence
print(str.find("python"))
print(str.find("Q"))

print(str.count("from")) #how many time 

#example wap to input user's first name and print its length 
name=(input("enter your first name:"))
print("length:",len(name))

#example to find the occurrence of '$' in a string 
string=input("enter string:")
print("occurrence of $:",string.count("$"))

#conditional statement in python 
# age=21
# if(age>=18):
#     print("can vote")
#     print("can drive")
    
# light="green"
# if(light=="red"):
#     print("stop")
# elif(light=="green"):
#     print("go")
# elif(light=="yellow"):
#     print("look")   

# num=5
# if(num>2):
#     print("greater than 2")
# if(num>3):                            #both execute
#     print("greater than 3")

num=5
if(num>2):
    print("greater than 2") 
elif(num>3): #only above execute 
    print("greater than 3")
    
light="g"
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")  
else:
    print("light is broken")      
    
#example   
marks=int(input("enter student marks:"))
if(marks>=90):
    grade="A"
elif(marks >=80 and marks<90):
    grade="B"  
elif(marks >=70 and marks<80):
    grade="c"   
else:
    grade="D"
print("grade of the student",grade) 

#odd or even 
num=int(input("enter number:"))
rem=num%2
if(rem==0):
    print("EVEN")
else:
    print("ODD")    
    
                  
        
     
 
    

    
        







