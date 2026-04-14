#types of all file operations
#open, read, write, close, append, delete, rename

#open a file
f=open("C:\\Users\\aryan\\Downloads\\python basic yt\\demo.txt","r") #w for write mode, r for read mode, a for append mode
data=f.read() #read the file
print(data)

line1=f.readline() #read a single line from the file
print(line1)  
f.close()  

#append means to add data to the end of the file
f=open("C:\\Users\\aryan\\Downloads\\python basic yt\\demo.txt","a") #open the file in append mode
f.write("\nThis is a new line added to the file.") #write a new line to the file
f.close() #close the file
         
#python automatically create file if it does not exist when we open it in write mode
f=open("C:\\Users\\aryan\\Downloads\\python basic yt\\newfile.txt","w") #open a new file in write mode
f.write("This is a new file created by python.") #write some data to the file   
f.close() #close the file   

f=open("C:\\Users\\aryan\\Downloads\\python basic yt\\demo.txt","r+") #open the file in read mode    
f.write("abc") #write some data to the file
f.close() #close the file

