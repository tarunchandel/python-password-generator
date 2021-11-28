import string
import random

print("Welcome to the PyPassword Generator.")
letters_num = int(input("How many letters would you like in your password?"))
symbols_num = int(input("How many symbols woul you like?"))
numbers_num = int(input("How many numbers would you like?"))
password = ""
for i in range(letters_num):
  password += random.choice(string.ascii_letters)

for i in range(symbols_num):
  password += random.choice(string.punctuation)
  
for i in range(numbers_num):
  password += random.choice(string.digits)
  

password = list(password)
random.shuffle(password)
password = ''.join(password)

print(f"Here is your password: {password}")
#print(string.ascii_letters, string.ascii_lowercase, string.ascii_uppercase, string.digits, string.printable)