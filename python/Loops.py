#while loops
# i = 0
# while i < 5:      
#     print(i)
#     i += 1  
      
# for loops
# for i in range(5):    
#     print(i)
# for i in range(1, 10, 2): #start,stop,step
#     print(i)  
# for i in range(10, 0, -1):
#     print(i)

#nested loops
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, j)

count=1
while count <= 5:
    print("kaushal") #print the name 5 times
    count += 1  

i=1 
while i <= 5:
    print(i) #print the numbers from 1 to 5
    i += 1 
print("Loop finished")

#print numbers from 1 to 100
i=1
while i <= 100:
    print(i)
    i += 1  
#print numbers from 100 to 1
i=100
while i >= 1: #stopping condition  
    print(i)
    i -= 1

#print the multiplication table of a number n 
n = int(input("Enter a number: "))
i = 1   
while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1

#print the elemenys of the following list using while loop
#numbers = [1,4,9,16,25,36,49,64,81,100]
numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1  
  
#search for a number x in this tuple using loops
#numbers = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
numbers = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter a number to search: "))
found = False   
i = 0
while i < len(numbers):
    if numbers[i] == x:
        found = True
        break
    i += 1  
if found:
    print(x, "found in the tuple.",i)    
else:
    print(x, "not found in the tuple.",i) 

#break and continue
i=1
while i <= 10:
    if i == 5:
        break #loop will stop when i is 5
    print(i)
    i += 1

i=0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue #skip the even numbers
    print(i) #print only odd numbers    
    
    
     
           
 




    
    
    