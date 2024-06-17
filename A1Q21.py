#To find the count of occurance of an element
data_list = []
n=int(input("Enter number of elements:"))
i=0
while i<n:
  value = input("Enter a list value : ")
  data_list.append(value)
  i+=1

find = input("Enter the element to count: ")
count = 0
for item in data_list:
    if item == find:
      count += 1

print("The element",find,"occurs",count,"times")