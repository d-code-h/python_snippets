import random

# variables
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@!`~#$%^&+=:><[]{}()*;/',._-"
all = lower + upper + numbers + symbols
length = 18

password = "".join(random.sample(all, length))

print("Your password is: " + password)