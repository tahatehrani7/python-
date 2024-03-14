import os 
dir_name = input ("enter name: ")
if not os.path.exists (dir_name):
    os.mkdir (dir_name)
    print (f"dir name = {dir_name}")
else:
    print (f"filed name = {dir_name}")