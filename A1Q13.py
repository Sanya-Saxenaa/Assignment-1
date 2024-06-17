#To calculate age
import datetime
from datetime import datetime

currentyear = datetime.now().year
birthyear = int(input("enter your birth year: "))
age = currentyear - birthyear
print(age)