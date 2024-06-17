#To calculate max and min
list = []
n=int(input("Enter number of elements:"))
i=0
while i<n:
  value = input("Enter a list value : ")
  list.append(value)
  i+=1
print("Max:",max(list))
print("Min:",min(list))