#create password generator

import random

def password_generator():
    #create a list of 8 random numbers
    password = []
    for i in range(8):
        password.append(random.randint(0,9))

    #create a list of 8 random letters
    for i in range(8):
        password.append(chr(random.randint(97,122)))

    #shuffle the list
    random.shuffle(password)

    #print the list
    print(password)

password_generator()