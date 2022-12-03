#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

Eazy Level - Order not randomised:
e.g. 4 letter, 2 symbol, 2 number = JduE&!91

total_length=nr_letters+nr_symbols+nr_numbers
#print(total_length)
letters_written=0
numbers_written=0
symbols_written=0
password=[]
for char in range(0, total_length+1):
  if letters_written < nr_letters:
    password.append(letters[random.randint(0, len(letters)-1)])
    letters_written+=1
  elif letters_written == nr_letters and symbols_written < nr_symbols:
    password.append(symbols[random.randint(0, len(symbols)-1)])
    symbols_written+=1
  elif letters_written == nr_letters and symbols_written == nr_symbols and numbers_written<nr_numbers:
    password.append(numbers[random.randint(0, len(numbers)-1)])
    numbers_written+=1

pwd_text=""

print(pwd_text.join(password))
  



# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# pwd_length=nr_letters+nr_numbers+nr_symbols
# #print(pwd_length)


# letters_written=[]
# symbols_written=[]
# numbers_written=[]
# written=[letters_written, symbols_written, numbers_written]

# for char in range(0, nr_letters):
#   letters_written.append(letters[random.randint(0,len(letters)-1)])
# for char in range(0, nr_numbers):
#   numbers_written.append(numbers[random.randint(0,len(numbers)-1)])
# for char in range(0, nr_symbols):
#   symbols_written.append(symbols[random.randint(0,len(symbols)-1)])
  
# print(written)


# #letters_taken=0
# #symbols_taken=0
# #numbers_taken=0
# password=""

# for char in range(0, pwd_length):
#   if len(letters_written)==0:
#     del letters_written
#   elif len(symbols_written)==0:
#     del symbols_written
#   elif len(numbers_written)==0:
#     del numbers_written
#   set_choice=random.randint(0, len(written)-1)
#   print(set_choice)
#   password+=str(written[set_choice].pop(random.randint(0, len(written[set_choice])-1)))
  
#   print(password)
#   #random.randint(0, len(nr_letters))
#   #if len(letters_taken)>0
  




