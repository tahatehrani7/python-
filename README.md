# aval number-
def primenumber (n):
    for i in range(2 , n):
        if n % i == 0:
            return "not aval"
    else:
        return  "aval"    
a = int (input("enter namber: "))
n = a
print(primenumber(a))
