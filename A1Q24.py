#To make a calculator
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2!=0:
        result=num1/num2
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid operator")
print(result)



