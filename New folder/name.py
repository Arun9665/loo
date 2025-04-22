

with open('funny.txt', 'w') as file:
    f1:str = file.write("hello world!")
    print(f1)

with open('funny.txt', 'r') as name:
    f2:str = name.read()
    print(f2)
