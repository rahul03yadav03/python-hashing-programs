#Firstly import hashlib
import hashlib


#now take the input from the user
password = input("Please enter your password to be hashed: ")


#Now create SHA-256 hash for the entered password
sha256 = hashlib.sha256(password.encode())


#Now get the hexdecimal digest
digest = sha256.hexdigest()


#Finally print the result
print("Here is your SHA-256 hash for your given string: ",digest)
