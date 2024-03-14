def decimal_to_octal(decimal_number):
    octal_number = oct(decimal_number)
    return octal_number
decimal_input = int(input(" enter number: "))
octal_result = decimal_to_octal(decimal_input)
print(f"number {decimal_input}--->>>{octal_result}")
