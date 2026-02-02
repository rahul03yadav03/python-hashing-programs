#First import the hashlib
import hashlib


#define a function as string1
def string1(first):
    
    
    #Now create a sha512 hash of the first
    sha512 = hashlib.sha512(first.encode())

    
    #convert the hash to a hexadecimal string
    digest1 = sha512.hexdigest()

    
    #return this digest1
    return digest1
    

#define a function as string2
def string2(second):

    
    #Now create a sha512 hash of the second
    sha512 = hashlib.sha512(second.encode())

    
    #convert the hash to a hexadecimal string
    digest2 = sha512.hexdigest()

    
    #return this digest2
    return digest2



#this block run only when the program is executed directly
if __name__ == "__main__":
    
    
    #Now take input and store it into first_string
    First_string = input("Please enter your first string: ")
    
    
    #Now take input and store it into second_string
    second_string = input("Please enter your second string: ")
    

    #now call to function string1 and store the result into store_first
    store_first = string1(First_string)
    

    #now call to function string2 and store the result into store_second
    store_second = string2(second_string)

    
    #now compare both the string 
    if store_first == store_second:

        
        #if both will be same then run this and print this
        print("Both string have same hash")


    else:

        
        #otherwise come here and run this and print this
        print("BOTH string have different hash")

    


