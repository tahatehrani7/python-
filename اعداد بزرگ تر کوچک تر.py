a = int ( input ("a :"))
b = int ( input ("b :"))
c = int ( input ("c :"))
if a>b and a>c:
    max = a
    print(f"max={a}")
elif b>a and b>c:
    max = b
    print(f"max={b}")
else :
    print(f"max={c}")