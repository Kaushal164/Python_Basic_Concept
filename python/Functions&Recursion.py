#function
def calc_sum(num1,num2):
    sum=num1+num2
    print (sum)
    return sum
calc_sum(5,10)

def print_hello():
    print("Hello")
print_hello()    
print_hello()
print_hello()

#average of three numbers
def average(num1,num2,num3):
    avg=(num1+num2+num3)/3
    print(avg)
    return avg
average(10,20,30)

#factorial of a number using function
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter a number: "))
print("Factorial of",num,"is",factorial(num))   

#alternatefactorial of a number 
n=5
fact=1
for i in range(1,n+1):
    fact=fact*i
print("Factorial of",n,"is",fact)

#alternatefactorial of a number using function
def call_fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print("Factorial of",n,"is",fact)
    
call_fact(5)

#converter
def celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius*9/5)+32
    print(fahrenheit)
    return fahrenheit
celsius_to_fahrenheit(25)

#recursion
def show(n):#function name and parameter
    if n == 0: #base case 
        return
    print(n)#recursive case
    show(n-1) #recursive call
show(5)

#write a program to calculate the sum of first n natural numbers using recursion
def sum_natural(n):
    if n == 0:
        return 0
    else:
        return n + sum_natural(n-1)     
num=int(input("Enter a number: "))
print("Sum of first",num,"natural numbers is",sum_natural(num))