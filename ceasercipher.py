#take the data to import
data=input("Please enter the data:")
key=input("Please enter the key:")

if(key==int):
    s=key
else:
    s=ord(key)%65

def encrypt(data,s):

    cipher_text=""

    for i in range(len(data)):
        char=data[i]
        
        if(char.isupper()):
            cipher_text+=chr(((ord(char)+s-65)%26)+65)
        elif(char.islower()):
            cipher_text+=chr(((ord(char)+s-97)%26)+97)
    
    return cipher_text

def decrypt(cipher_text,s):
    
    encrypted_data=""

    for i in range(len(cipher_text)):

        char=cipher_text[i]

        if(char.isupper()):
            encrypted_data+=chr(((ord(char)-s-65)%26)+65)
        elif(char.islower()):
            encrypted_data+=chr(((ord(char)-s-97)%26)+97)

    return encrypted_data

encrypted=encrypt(data,s)
print(encrypted)
decrypted=decrypt(encrypted,s)
print(decrypted)
