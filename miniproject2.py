import random
import string
pass_len = int(input("Enter the desired password length: "))

charValues = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
   password+=  random.choice(charValues)

print("your password is : ",password)