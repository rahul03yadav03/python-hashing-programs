#firstly, import a library name hashlib
import hashlib


#define a function name hash_found
def hash_found(file):

    
    #now open  file in binary mode
    with open(file, "rb") as new_file:


        #read entire content in bytes
        read = new_file.read()

    #create sha512 hash object
    sha512 =  hashlib.sha512()


    #update the file
    update = sha512.update(read)

    #now get final hash in hexdigest formate
    digest= sha512.hexdigest()

    #now return the digest
    return digest



#main programn start here
if __name__ == "__main__":


    #now make a  empty dictionary
    hash_dictionary = {}


    
    #infinit loop (run until user stops)
    while True:

        
        #now ask the user, how many files he want to give
        file_number = int(input("Please enter the numbner of file which you want to hash: "))


        
        #loop for each file
        for i in range(file_number):


            
             #ask user to enter file name
            filename = input(f"Please enter the name of your file {i+1}: ")


            #first run this block
            try:
                
                #calculate hash and store it in dictionary
                hash_dictionary[filename] = hash_found(filename)

                
                #success message
                print(f"{filename} hashed successfully!")

            #run this block if try fails
            except FileNotFoundError:


                #if file does not exist, then print this
                print(f"File {filename} not found!")


                
        #asku user if they wants to hash more file
        choice = input("Do you want to hash any other file? (yes or no): ").lower()



        
        #if user say anything other than "yes", exit loop
        if choice != "yes":
            break

#print final dictionary containing filenames and hashes
    print("\n Final File -> Hash Dictionary:")
    for file, hash_value in hash_dictionary.items():
        print(f"{file}  :  {hash_value}")





        

    
    
