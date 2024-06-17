#to write a line in text file
file = open("q5.txt", "w")
str = input("enter a string: ")
file.write(str)
file.close()