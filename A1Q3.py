num=int(input("Enter a numer:"))
fact=1
for i in range(num,0,-1):
    fact*=i
print("Factorial of",num,"is" ,fact)