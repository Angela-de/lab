#listcomprehension
from functools import *
names = ["sam", "john", "james"]
print (map(len, names))

def too_old(x):
    return x > 30
ages = [22, 25, 29, 34, 56, 24, 12]
print (list(filter(too_old, ages)))

#creating  postive numbers from a list
print("\n")
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [n for n in numbers if n > 0]
print (newlist)

#creating postive numbers from a list ...another way
print("\n")
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
for p in numbers:
    if p>=0:
        print(p)
        
        
#retun only even numbers
print("\n")
numbers = [1,56,234,87,4,76,24,69,90,135]
newlist = [n for n in numbers if n%2==0]
print (newlist)

# returning only even numbers..another way
print("\n")
def is_even(x):
    return n % 2 == 0 
enum =[1,56,234,87,4,76,24,69,90,135] 
print(enum)

#creating a list containing tuples of uppercase version except "is"

print("\n")
words = ["hello", "my", "name", "is", "Sam"]
newlist = [(w.upper(),len(w)) for w in words if w != "is"]
print(newlist)

#creating a list containing tuples of uppercase version 

print("\n")
words = ["hello", "my", "name", "is", "Sam"]
newlist = [(w.upper(),len(w)) for w in words]
print(newlist)

print("\n")
#fold

total = reduce(lambda item, running_total: item + running_total, [1, 2, 3, 4, 5])
print(total)

print("\n")
#fold
total2 = reduce(lambda item, running_total: item * running_total, [1, 2, 3, 4, 5])
print(total2)

print("\n")
#write a function to join strings
def join_strings():
    words = ["hello", "world"]
    helloworld =" " .join(words) 
    return helloworld
print(join_strings())

