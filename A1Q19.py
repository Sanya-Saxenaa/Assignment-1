#To remove all punctuation from a given string
s = input("Enter the string:")
words = s.split()
list = []
for w in words:
    word = ''.join(char for char in w if char.isalnum())
    list.append(word)
new_string = ' '.join(list)
print(new_string)

