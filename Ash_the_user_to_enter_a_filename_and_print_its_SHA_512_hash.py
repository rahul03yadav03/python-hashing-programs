#firt import hashlib library
import hashlib


#take input from the user, like the filename
filename = input("Please enter your filename: ")


#first we will try this block
try:
    #here we open the file in binary read which user has input 
    with open(filename, "rb") as file:
        your_file = file.read()


    
    #Now create sha512 hash for the file 
    sha512 = hashlib.sha512(your_file)


    #Now get the hexa decimal digest
    digest = sha512.hexdigest()


    #Now print the result in hash formate
    print("here is your sha512 of the given file: ",digest)

#run this block if filname not found or incorrect
except FileNotFoundError:


    #And print this
    print("Error!File name not found. Please Give me correct file name: ")
    

     
