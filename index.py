import string
from random import *
print(" ")

for i in range(10):
    char = string.ascii_letters + string. punctuation + string.digits
    index_password = "".join(choice(char) for x in range(randint(8, 20)))
    print(index_password)
    print(" ")
