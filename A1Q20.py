#To take a list of numbers as input and print sum
s = input("Enter a list of numbers separated by spaces: ")
nums = s.split()
numbers = [int(num) for num in nums]
total = sum(numbers)
print(f"The sum of the numbers is: {total}")
