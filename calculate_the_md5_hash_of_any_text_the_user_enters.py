#Firt we need to import hashlib
import hashlib  


#Take the input from the user
text = input("Please enter your text:  ")


#Now create md5 hash for the entered text
md5 = hashlib.md5(text.encode())



#Now get the hexdecimal digest
digest = md5.hexdigest()


#Finally print the  result
print("Here is your md5 hash of your given text: ", digest)
