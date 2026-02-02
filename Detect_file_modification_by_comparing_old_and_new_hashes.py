#first import hashlib library
import hashlib


#Here define a functon, this function will make a hash for a given file
def hash_found(file):

    
    #first run this block
    try:
        
        
        #open a file in binary read mode
        with open(file , "rb") as file:
            read_file = file.read()
            

        #create sha512 hash object 
        sha512 = hashlib.sha512()
        

        #and update it with file conetent
        update = sha512.update(read_file)


        #Now get the hexa decimal digest
        digest = sha512.hexdigest()
        

        #return hexa decimal
        return digest
    

    #if try block fail to run then run this block 
    except FileNotFoundError:
        

        #And print this line
        print("Error! No such file found, Please netr a correct file.")
        

#Now again, define a function; it will handle the situtation if user wants to modify in file
def modify_hash(file2):


    
    #again first run this block
    try:


        #take input from user to append to file
        new_content = input("Enter the content which you want to add: ")

        
        #open a file in append mode to modify content
        with open(file2, "a") as file:

            
            #do modification in that file
            new = file.write(new_content)


         #if modification was successful then print this line   
        print(f"file {file2} has modified successfully!")


        
        #after modification, we need to send file2 in "hash_found function" for making it's hashes
        return hash_found(file2)


    #run this block, if try block fail to run
    except FileNotFoundError:


        #print this as an error
        print("Error! No such file found, Please netr a correct file.")




#this block run only when the program is executed directly
if __name__ == "__main__":

    
    #take input from user, here user will enter the file name
    filename = input("Please enter your file name: ")


    #call to function "hash_found" and store the hashes in "old_hash"
    old_hash = hash_found(filename)

    
    #ask user , do he wants to do any modification in  the file or not
    modify_choice = input("Do you want to modify this file(yes/no): ").lower()



    #if user says yes then run this block
    if modify_choice == "yes":


        #and again call to function modify_hash and store the hashes in new_hash
        new_hash = modify_hash(filename)


        #if both the hashes will same then run this block
        if old_hash==new_hash:


            #and print this line
            print("NO Modification! hashes are same ")


            
        #otherwise run this block
        else:


            #and print this line
            print("FILE HAS BEEN MODIFIED! Hashes are not same.")
        



    #if user choose "no" then run elif block 
    elif modify_choice == "no":


        #and print this line
        print("NO Modification! hashes are same")

    
    #if user choose any this else then run this else block
    else:


        #and then, print this line
        print("Invalid choice! Please choose (yes or no): ")


        #exit the program
        exit()

  


        
        

    
