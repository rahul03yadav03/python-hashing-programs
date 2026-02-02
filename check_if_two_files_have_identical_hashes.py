#firstly we need to import hashlib library
import hashlib

#now define a function name file1
def file1(first_file):
    

    #open first file in read binary formate
    with open(first_file , "rb") as file:
        your_first_file = file.read()


    #Now create sha512 hash for the file
    sha512 = hashlib.sha512(your_first_file)


    #Now get the hexa decimal digest
    digest1 = sha512.hexdigest()

    
    #now return digest1 
    return digest1


#now define a function name file2
def file2(second_file):
    
    
    #open second file in read binary formate 
    with open(second_file, "rb") as file:
        your_second_file = file.read()

        
    #Now create sha512 hash for the file
    sha512 = hashlib.sha512(your_second_file)

    
    #Now get the hexa decimal digest
    digest2 = sha512.hexdigest()

    
    #now return digest2
    return digest2


#this block run only when the program is executed directly
if __name__ == "__main__":

    

    #ask user to input name of the file and store the file in filename1
    filename1 = input("Please enter your first file: ")


    #again, ask user to input name of the file and store the file in filename2
    filename2 = input("Please enter your second file: ")
    

    #call to function file1 and store result into first_hash_stored_value
    first_hash_stored_value = file1(filename1)

s
    #call to fnction file2 and store result into second_hash_stored_value
    second_hash_stored_value = file2(filename2)
    
    #here we compare if both file have same hash or not, if they thave same then run this block
    if first_hash_stored_value == second_hash_stored_value:
        

        #and print this
        print("Both file have the same hash value")


        
    #if the hash value are differnt then run this block
    else:

        
        #and print this
        print("Both have different hash value")





        
