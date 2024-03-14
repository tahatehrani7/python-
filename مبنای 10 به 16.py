def decimal_to_hex(decimal_number):
    hex_number = hex(decimal_number)
    return hex_number
decimal_input = int(input("enter number: "))
hex_result = decimal_to_hex(decimal_input)
print(f"number {decimal_input}---->>>{hex_result}")