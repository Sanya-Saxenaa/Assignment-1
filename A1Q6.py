#To read and print the contents of a file
f=open(q6.txt, 'r') 
content = file.read()
for i in content:
    print(i)
f.close()