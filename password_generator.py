# ------------------------------------------------------------------ PASSWORD GENERATOR -------------------------------------------------------
import random
letters = ['a','b','c', 'd', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v', 'w','x','y','z'
           ,'A', 'B', 'C ','D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', ' X', 'Y', 'Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['@', '#', '$', '&', '*', '!', '~']
print("Welcome To Password Generator!!")
num_letters = int(input("Enter the number of letter for your password generation: \n"))
num_numbers = int(input("Enter the number of digits for your password generation: \n"))
num_symbols = int(input("Enter the number of symbols for your password generation: \n"))
password_list =[]
# WHERE THE RANDOM LETTERS ARE GENERATED
for i in range (1, num_letters +1): #1,2,3,4
    char = random.choice(letters)
    password_list += char

# WHERE THE RANDOM SYMBOLS ARE GENERATED
for i in range(1, num_symbols+1):
   char = random.choice(symbols)
   password_list += char

# WHERE THE RANDOM NUMBERS ARE GENERATED
for i in range (1, num_numbers +1): #1,2,3,4
    char = random.choice(numbers)
    password_list += char
    # password_list.append(char)

print(f"Password Before Password Shuffle: {password_list} ")
random.shuffle(password_list)
print(f"Password Afer Password Shuffle: {password_list} ")

# Initialize password as an empty string
password = ""

# Build the password string using a for loop statement
for char in password_list:
    if char in password_list:  # This condition is always true, so it's just iterating over each character
        password += char

print("Generated Password:", password)