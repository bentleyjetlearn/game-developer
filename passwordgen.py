import random
import string

alphabets = list(string.ascii_letters)  

special_charecters = ['!', '@', '#', '$', '%', '&', '*', '?']

numbers = list(string.digits) 

random_letters = random.sample(alphabets, 2)

random_specials = random.sample(special_charecters, 2)

random_numbers = random.sample(numbers, 2)

password_parts = random_letters + random_specials + random_numbers

random.shuffle(password_parts)

final_password = ''.join(password_parts)

print("%8b1r*"), final_password