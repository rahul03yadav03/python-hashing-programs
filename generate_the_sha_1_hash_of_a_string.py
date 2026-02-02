#First we need to import hashlib
import hashlib


#Now take the input from the user
string = input("Please enter your string: ")


#Now create sha1 hash for the entered string
sha_1 = hashlib.sha1(string.encode())


#Now get the hexadecimal digest
digest = sha_1.hexdigest()


#Finally print the result
print("Here is your SHA-1 hash of your given string: ", digest)
