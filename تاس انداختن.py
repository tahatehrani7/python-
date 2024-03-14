import random
a = input ()
if a=="a":
    from random import randint 
    b = ''
    random_tas = "1 2 3 4 5 6 "
    for i in range (1):
        x = randint (0 , len(random_tas)-1)
        b = b + random_tas [x]
        print (b)