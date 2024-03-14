import random

def generate_password():

    first_name = input("enter first_name: ")
    last_name = input("enter last_name: ")

    full_name = first_name + last_name

    full_name = full_name.lower().replace(" ", "")

    password = full_name + str(random.randint(1000, 9999))

    print("yuor password ", password)

generate_password()