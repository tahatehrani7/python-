def toBinary(number):
    binary_list = []
    while number >= 1:
        binary_list.append(number % 2)
        number = number // 2
    return binary_list[::-1]
input_number = int(input("enter number"))
binary_result = toBinary(input_number)
print(f"{input_number} --->>> {binary_result}")