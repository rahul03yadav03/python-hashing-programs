#First we need to import hashlib
import hashlib

#Now take the file name as input
filename = input("Please enter your filename to be hashed: ")


try:
    #Now open the given file file in read binary mode
    with open(filename, "rb") as file:
        file_name = file.read()

    #Now craete MD5 hash for the entered file
    md5 = hashlib.md5(file_name)


    #Now get the hexdecimal digest
    digest = md5.hexdigest()


    #Finally print the result
    print("Hers is your md5 of your given filename",digest)

except FileNotFoundError:
    #Handle this case if the file does not exist
    print("Error: !file not found. Please check the filename or path")
