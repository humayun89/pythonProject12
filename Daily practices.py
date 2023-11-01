# Use of format :
from typing import List

name = "Humayun"
age = 34
print ("My name is {} and i am {} years old".format(name,age))

# while loop and format:
i = 3000
while i<10000:
    i+=150
    print("i is :{}".format(i))
# Using range function in for loop :
for i in range (0,10):
    i+=1
    print("i value is {}" .format(i))

# Range funciotn in list with format:
for i in list(range (0,10)):
    print("i value is {}" .format(i))
# Power operation :
x= list(range(1,500))
out=[ ]
for num in x:
    out.append(num**3)
print(out)
print([num**4 for num in x])
# defining a function:
def my_func(name):
    print('Hello '+  name)
my_func('Humayun')
# Defining some mathematical problem :
def square(num):
    return (num**2)
output=square(5)
print(output)






