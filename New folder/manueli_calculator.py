try:
    class calculator:

     def add(a, b):
        return a + b
    
     def subtrack(a, b):
        return a - b
    
     def multiply(a, b):
        return a * b
    
     def divide(a, b):
        if b != 0:
            return a / b
        
        else:
            return "cannot divide by gero"
        
    
     print("1. add")
     print("2. subtrack")
     print("3. multiply")
     print("4. divide")
    
     choise = input("enter yours choise (1/2/3/4/5/) -:")

     num = float(input("enter first values -:"))
     num1 = float(input("enter second values -:"))

     if choise=='1':
        print("result:", add(num, num1))

     elif choise=='2':
        print("result:", subtrack(num, num1))

     elif choise=='3':
        print("result:", multiply(num, num1))

     elif choise=='4':
        print("result:", divide(num, num1) )

     else:
        print(" error calcultion mode")

    calculator()



except ValueError as e:
    print(e)