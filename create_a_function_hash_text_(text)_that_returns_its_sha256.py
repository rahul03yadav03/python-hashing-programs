#firstly import hashlib library
import hashlib


#Now define a function name hash_text
def hash_text(text):

    #Now create sha512 hash for the file
    sha256 = hashlib.sha256(text.encode())

    
    #Now get the hexa decimal digest
    digest = sha256.hexdigest()

    
    #return digest
    return digest





# this block run only when the program is executed directly 
if __name__ == "__main__":


    
    #take input and store it into sentence
    sentence = input("Please enter sentence or words: ")

    #now call to function hash_text and store the result into store_value
    store_value = hash_text(sentence)


    
    #print the hash value of given text or senetnce or word
    print("Here is your sha256 hash of given text: ",store_value)
