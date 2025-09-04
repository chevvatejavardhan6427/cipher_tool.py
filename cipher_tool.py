import random
import string
chars=" "+string.punctuation+string.digits+string.ascii_letters
chars=list(chars)
key=chars.copy()
random.shuffle(key)
print(f"chars={chars}")
print(f"key={key}")


#ENCRYPT
message=input("enter any message : ")
encrypt=""
for letter in message:
	Index=chars.index(letter)
	encrypt+=key[Index]
print(f"your encryt = {encrypt}")

#DECRYPT
encrypt=input("enter any encrypt to de code : ")
message=""
for letter in encrypt:
	Index=key.index(letter)
	message+=chars[Index]
print(f"your message = {message}")
